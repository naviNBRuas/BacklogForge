# Architecture Notebook

*(Artefato 5 do trabalho prático: "descrição da arquitetura do software".)*

## 1. Objetivos de Arquitetura

- Manter a arquitetura **simples e explícita**: cada decisão deve ser justificável e descritível neste documento, evitando "mágica" de framework que dificulte a explicação (ver `tech-stack.md`, justificativa Flask vs. Django).
- Garantir que **RBAC e auditoria sejam transversais**, aplicados de forma consistente em toda rota de dados, não implementados ad hoc por tela.
- Suportar o vocabulário de domínio do enunciado (Projeto → Product Backlog / Sprint Backlog → História de Usuário → Critério de Aceitação, com Épico como agrupador transversal) como **modelo de dados de primeira classe**, não como campos genéricos de um sistema de tarefas.
- Ser executável e demonstrável localmente por uma única pessoa, sem infraestrutura além de Python + SQLite.

## 2. Suposições

- Volume de dados compatível com uso individual/acadêmico (dezenas de projetos, centenas de histórias) — não há suposição de escala multi-tenant de produção.
- O avaliador (professor) executará o protótipo localmente ou assistirá ao vídeo de demonstração — não há suposição de alta disponibilidade.
- Apenas um processo Flask em execução por vez durante a demonstração (sem necessidade de lock distribuído sobre o SQLite).

## 3. Dependências

- **Framework web**: Flask (roteamento, templates Jinja2, contexto de requisição).
- **ORM/Banco**: Flask-SQLAlchemy sobre SQLite — o modelo de dados (seção 6) depende diretamente do mapeamento objeto-relacional do SQLAlchemy.
- **Autenticação/Sessão**: Flask-Login — a Seção 5 (RBAC) depende do `current_user` e do ciclo de vida de sessão que essa biblioteca gerencia.
- **Segurança de formulário**: Flask-WTF (CSRF, validação) — toda view de escrita depende de um `FlaskForm` correspondente.
- **Cabeçalhos/cookies seguros**: Flask-Talisman — aplicado uma vez, na inicialização da aplicação (`create_app`), afetando todas as respostas.
- **Hash de senha**: argon2-cffi.
- **Criptografia em repouso**: cryptography (Fernet).
- Ver `tech-stack.md` para a lista completa e a justificativa de cada escolha.

## 4. Requisitos que Influenciam a Arquitetura

- **NFR de segurança** (`non-functional-requirements.md`, seção 3) força a existência de uma camada de autorização centralizada (não espalhada por template) e de um mecanismo de auditoria transversal.
- **Requisito (5) do enunciado** ("só pode existir um Product Backlog por projeto") é modelado como restrição de unicidade no banco (chave estrangeira `project_id` única na tabela `product_backlogs`), não apenas validado na aplicação.
- **Requisito (8)** ("mover histórias entre backlogs") implica que uma História de Usuário pertence a **um** backlog por vez, mas o tipo de backlog (Product ou Sprint) pode variar — modelado com uma associação polimórfica simples (ver seção 6).

## 5. Decisões de Arquitetura, Restrições e Justificativas

| Decisão | Justificativa | Restrição aceita |
|---|---|---|
| Arquitetura monolítica em camadas (routes → services → models), sem microsserviços | Escopo e prazo acadêmico; um único desenvolvedor | Não escala horizontalmente — aceitável, fora do escopo (ver NFR §8) |
| RBAC implementado como decorator (`@require_role("admin")`) aplicado nas rotas, não como checagem manual espalhada | Centraliza a regra de autorização num único ponto, testável isoladamente | Toda rota nova precisa lembrar de aplicar o decorator — mitigado com uma checklist de PR/checklist de revisão do próprio Kanban (coluna "Em Revisão") |
| Log de auditoria como tabela própria (`audit_logs`), gravada por um serviço central (`audit.log(user, action, entity)`) chamado explicitamente nas operações de escrita | Evita depender de triggers de banco (menos portável) e mantém a decisão de "o que auditar" no código Python, fácil de descrever aqui | Chamada de auditoria pode ser esquecida em uma nova operação de escrita — mitigado concentrando todas as operações de escrita em métodos de serviço (seção 6), não diretamente nas rotas |
| Criptografia em repouso via um `TypeDecorator` do SQLAlchemy (campo customizado `EncryptedString`) | Torna a cifragem transparente ao restante do código — quem lê/escreve o campo não precisa saber que ele é cifrado | Índices/buscas por igualdade no campo cifrado não são eficientes — aceitável pois os campos sensíveis não são usados em filtros/buscas |
| Um único Product Backlog por projeto criado automaticamente na criação do projeto (não exposto como criação manual) | Reflete o requisito (5) do enunciado diretamente no fluxo, sem tela extra desnecessária | Nenhuma — decisão sem trade-off relevante |

## 6. Mecanismos de Arquitetura

- **Camada de rotas (views)**: recebe a requisição HTTP, valida entrada via `Flask-WTF`, delega para a camada de serviço, renderiza o template Jinja2 ou redireciona.
- **Camada de serviço**: funções puras/orquestradoras (ex.: `project_service.create_project(user, data)`) que aplicam regras de negócio (criação em cascata do Product Backlog, validação de valores fechados de story points/MoSCoW/RICE, cálculo do score RICE) e chamam o serviço de auditoria.
- **Camada de modelo (SQLAlchemy)**: entidades do domínio (seção 7) e o `TypeDecorator` `EncryptedString` para campos sensíveis.
- **Mecanismo de autorização**: decorator `@login_required` (Flask-Login) + decorator próprio `@require_role(role)` que verifica `current_user.role`; decorator `@require_project_owner` que verifica se o `current_user` é dono do projeto acessado (evita um usuário acessar recurso de outro via manipulação de URL).
- **Mecanismo de auditoria**: serviço `audit_service.log(actor, action, entity_type, entity_id)` chamado ao final de toda operação de escrita bem-sucedida nos serviços de negócio; consultado apenas pela rota `/admin/audit-logs`, protegida por `@require_role("admin")`.
- **Mecanismo de cálculo RICE**: função pura `calculate_rice(reach, impact, confidence, effort)` retornando `(reach * impact * confidence) / effort`, usada tanto na exibição quanto na ordenação do backlog (requisito 19).

## 7. Abstrações Relativas à Arquitetura

Entidades do domínio (elementos) e seus relacionamentos (mapeados 1:1 para as tabelas do projeto físico de banco de dados, ver `database-design.md`):

- `User` (1) — (N) `Project` (dono)
- `Project` (1) — (1) `ProductBacklog`
- `Project` (1) — (N) `SprintBacklog`
- `Project` (1) — (N) `Epic`
- `UserStory` pertence a exatamente um backlog (`ProductBacklog` **ou** `SprintBacklog`, nunca ambos) e opcionalmente a um `Epic`
- `UserStory` (1) — (N) `AcceptanceCriterion`
- `AuditLog` referencia um `User` (autor) e, de forma genérica (tipo + id), a entidade afetada

A abstração central é a **História de Usuário como agregado**: story points, MoSCoW e critérios RICE são atributos dela mesma (não entidades separadas), enquanto Critérios de Aceitação são uma entidade filha com ciclo de vida dependente (excluídos em cascata com a história).

## 8. Arquitetura Segundo Perspectivas

- **Perspectiva lógica** (módulos): `auth/`, `projects/`, `backlogs/`, `stories/`, `epics/`, `admin/` — cada um com `routes.py`, `services.py`, `forms.py`; `models.py` e `extensions.py` (instâncias de SQLAlchemy/Login/Talisman) compartilhados na raiz do pacote.
- **Perspectiva de processo**: uma única requisição HTTP síncrona por vez tratada pelo servidor de desenvolvimento do Flask (`flask run`); sem processamento assíncrono/background jobs no MVP.
- **Perspectiva de dados**: ver `database-design.md` — um arquivo SQLite único, sem replicação.
- **Perspectiva de implantação**: ver `infrastructure.md` — processo Flask único, servido localmente ou por um serviço simples (Render/PythonAnywhere) atrás de HTTPS.
- **Perspectiva de segurança**: ver `non-functional-requirements.md` §3 — autenticação, RBAC, CSRF, cookies seguros, cabeçalhos HTTP, criptografia em repouso e auditoria atravessam todas as demais perspectivas.

## 9. Impacto das Ferramentas Usadas na Arquitetura

- **Flask** (vs. Django): por não ter ORM/auth/admin embutidos, força a arquitetura em camadas explícitas descrita na seção 6 — decisão consciente para tornar a arquitetura mais fácil de descrever e defender neste documento (ver `tech-stack.md`).
- **Flask-SQLAlchemy**: define o padrão de acesso a dados (Active Record-like via `db.Model`), influenciando a camada de serviço a manipular objetos ORM em vez de SQL cru.
- **Flask-Login**: impõe o padrão `UserMixin` + `LoginManager.user_loader`, o que molda como o papel (`role`) do usuário é carregado a cada requisição (via `current_user.role`).
- **Flask-WTF**: impõe que toda rota de escrita tenha uma classe `Form` correspondente, o que naturalmente força validação centralizada por formulário em vez de checagens manuais espalhadas nas views.
- **Flask-Talisman**: aplicado uma única vez na fábrica da aplicação (`create_app`), afeta globalmente cabeçalhos/cookies de todas as respostas sem exigir mudança nas views individuais.
- **Jinja2** (server-rendered, sem SPA): elimina a necessidade de uma API JSON separada e de build tooling de frontend, mantendo a arquitetura em uma única camada de apresentação.
