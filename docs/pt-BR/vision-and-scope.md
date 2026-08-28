# Visão e Escopo (Vision and Scope)

*(Artefato 2 do trabalho prático: "documento de visão e escopo".)*

## Problema

Equipes que usam histórias de usuário para gerenciar requisitos (times ágeis, Scrum/Kanban) precisam de um lugar único para registrar e priorizar: projetos, backlogs (de produto e de sprint), épicos e histórias de usuário — com critérios de aceitação, estimativa (story points), prioridade (MoSCoW) e priorização por valor/esforço (RICE). Hoje isso é feito em planilhas ou ferramentas genéricas (Trello, Notion) que não modelam nativamente esse vocabulário específico (épico → história → critério de aceitação, com pontuação e MoSCoW/RICE já embutidos).

## Posição no Mercado

Uma ferramenta **enxuta e especializada**, no espaço entre uma planilha (sem estrutura) e um Jira completo (pesado, caro, complexo). Equivalente em espírito a ferramentas simples de backlog para times pequenos/estudos de caso acadêmicos.

## Partes Interessadas (Stakeholders)

| Stakeholder | Responsabilidade |
|---|---|
| Usuário (autenticado) | Cria/gerencia seus próprios projetos, backlogs e histórias |
| Product Owner (papel dentro de um projeto) | Prioriza o Product Backlog, define MoSCoW/RICE |
| Desenvolvedor (papel dentro de um projeto) | Consulta/atualiza histórias atribuídas a sprints |
| Administrador (papel global do sistema) | Monitora todos os usuários, projetos e logs de auditoria; não participa do trabalho de um projeto específico |
| Professor/avaliador (ESW) | Avalia o sistema como trabalho prático da disciplina |

## Ambiente dos Futuros Usuários

- Acesso via navegador web, desktop (não há requisito de app mobile).
- Uso individual ou em pequenos times — cada conta vê os projetos de que participa (no MVP: cada usuário só vê seus próprios projetos, exceto o Administrador, que tem visão global — ver "Controle de Acesso por Papéis" abaixo e "Fora de Escopo").

## Necessidades Atendidas

- Estruturar requisitos de um projeto usando o vocabulário de histórias de usuário sem depender de planilhas ad hoc.
- Mover histórias entre backlogs (produto ↔ sprints) conforme o planejamento avança.
- Priorizar por dois métodos complementares: **MoSCoW** (qualitativo) e **RICE** (quantitativo).
- Garantir que dados de conta e de projeto fiquem protegidos (senha com hash forte, dados sensíveis cifrados em repouso, sessão segura) e que ações relevantes do sistema fiquem auditáveis (log de quem fez o quê e quando).
- Dar a um papel de Administrador visibilidade sobre todo o sistema (usuários, projetos, logs), sem misturar essa responsabilidade com o trabalho de PO/Desenvolvedor dentro de um projeto.

## Funcionalidades (resumo — detalhamento vira histórias de usuário)

1. Conta de usuário + autenticação.
2. CRUD de Projetos.
3. CRUD de Product Backlog (1 por projeto).
4. CRUD de Sprint Backlogs (N por projeto).
5. CRUD de Histórias de Usuário (formato `Como/Eu quero/Para`), associadas ao Product Backlog na criação.
6. Mover histórias entre backlogs.
7. CRUD de Épicos + vínculo história↔épico.
8. CRUD de Critérios de Aceitação por história (formato `Dado/Quando/Então`).
9. Atribuir story points (série 0,1,2,3,5,8,13,21,34,55).
10. Atribuir etiqueta MoSCoW (M/S/C/W).
11. Atribuir critério RICE (Reach, Impact, Confidence, Effort) e calcular a pontuação `(R×I×C)/E`.
12. Controle de acesso por papéis (RBAC): papel **Administrador** com painel de monitoramento (usuários, projetos, logs de auditoria).
13. Log de auditoria das ações relevantes do sistema (quem fez o quê, quando).

## Controle de Acesso por Papéis (RBAC)

Diferente do rascunho inicial, o MVP passa a ter um controle de acesso por papéis real (não apenas um rótulo):

- **Usuário** (papel padrão de qualquer conta): acesso total de leitura/escrita aos seus próprios projetos e a tudo dentro deles (PO e Desenvolvedor, na prática, são o mesmo usuário desempenhando funções diferentes dentro de um projeto solo — o sistema não impõe uma segunda conta por papel).
- **Administrador**: papel global, atribuído a uma conta específica (não por projeto). Não acessa o conteúdo de projetos de outros usuários para editá-lo, mas tem um painel de monitoramento com: lista de todos os usuários e projetos do sistema, e o log de auditoria completo. Esse papel existe para fins de administração/observabilidade do sistema, não para participar do trabalho ágil em si.
- A primeira conta administradora é definida por *seed*/configuração (ex.: variável de ambiente) na primeira execução — não existe endpoint público de "virar admin".

## Requisitos Não Funcionais (resumo — detalhado em `docs/pt-BR/non-functional-requirements.md`)

- **Usabilidade**: CRUDs devem seguir um padrão de navegação consistente entre as entidades.
- **Portabilidade**: rodar em qualquer ambiente com Python 3 instalado (SQLite embutido).
- **Segurança**: senha nunca armazenada em texto puro (hash forte, ex.: `bcrypt`/`argon2`); dados sensíveis cifrados em repouso; proteção CSRF em formulários; cookies de sessão seguros (`HttpOnly`, `Secure`, `SameSite`); cabeçalhos HTTP de segurança; controle de acesso por papéis (RBAC) aplicado em toda rota sensível, não só na tela de login.
- **Auditabilidade**: log estruturado de eventos de segurança e de mudança de dados (criação/edição/exclusão em qualquer entidade, login/logout, falhas de autenticação), com timestamp e usuário responsável, consultável pelo Administrador.

## Fora de Escopo (MVP)

- Colaboração multiusuário em tempo real no mesmo projeto (ex.: múltiplos POs editando simultaneamente com atualização ao vivo).
- Papéis de PO/Desenvolvedor como permissões distintas *dentro* de um mesmo projeto (continuam sendo rótulos narrativos das histórias de usuário — a permissão técnica real é: dono do projeto vs. Administrador).
- Notificações/e-mail.
- Integração com ferramentas externas (Jira, GitHub Issues).
- Aplicativo mobile nativo.

## Elementos da Solução Proposta

Aplicação web monolítica (Flask + SQLite), autenticação por sessão com controle de acesso por papéis (Usuário/Administrador), senhas com hash forte e dados sensíveis cifrados em repouso, log de auditoria persistente, CRUD server-rendered para cada entidade do domínio, e uma view de cálculo/exibição do score RICE por história. Ver `docs/pt-BR/tech-stack.md` para as bibliotecas específicas de segurança/logging.
