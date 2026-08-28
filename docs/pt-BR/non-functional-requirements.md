# Especificação de Requisitos Não Funcionais (System-Wide Requirements)

*(Artefato 3 do trabalho prático: "especificação de requisitos não funcionais por meio de artefato para esse fim". Cobre requisitos funcionais adicionais não capturados em histórias de usuário, atributos de qualidade, interfaces, conformidade, restrições, licenciamento e documentação.)*

## 1. Requisitos Funcionais Não Cobertos por Histórias de Usuário

A maior parte dos requisitos funcionais está em [`user-stories.md`](user-stories.md). Os itens abaixo são funcionais mas de natureza transversal (não pertencem a uma única história):

- **Criação automática de dados dependentes**: ao criar um projeto, o Product Backlog correspondente é criado automaticamente (ver US-05); ao excluir um projeto, todos os dados dependentes são excluídos em cascata (ver US-08); ao excluir um Sprint Backlog, suas histórias retornam ao Product Backlog em vez de serem excluídas (ver US-14).
- **Validação de valores de domínio fechado**: story points, MoSCoW e RICE só aceitam os valores definidos no enunciado (seção 2, itens 15–18) — validado tanto na interface quanto no servidor (nunca confiar apenas no `<select>` do HTML).
- **Seed da conta administradora**: na primeira execução da aplicação, uma conta com papel `admin` é criada/promovida a partir de variáveis de ambiente (`ADMIN_EMAIL`, `ADMIN_PASSWORD`), sem endpoint público equivalente.

## 2. Atributos de Qualidade

| Atributo | Requisito |
|---|---|
| **Usabilidade** | Todas as telas de CRUD seguem o mesmo padrão de navegação (listar → ver detalhes → editar/excluir com confirmação); mensagens de erro de validação aparecem junto ao campo problemático; navegação por breadcrumb (Projeto → Backlog → História). |
| **Desempenho** | Cada página de listagem (projetos, backlogs, histórias) deve carregar em menos de 1s com até 100 histórias por backlog em ambiente de desenvolvimento local — escala compatível com SQLite e uso individual/acadêmico, sem exigir otimizações de produção em larga escala. |
| **Confiabilidade** | Nenhuma exclusão (projeto, backlog, história, épico, critério) ocorre sem confirmação explícita do usuário; toda exclusão em cascata é intencional e documentada (ver seção 1). |
| **Manutenibilidade** | Código organizado por camada (rotas/views, modelos, formulários) seguindo a convenção padrão do Flask; sem lógica de negócio embutida em templates Jinja2. |
| **Portabilidade** | Roda em qualquer ambiente com Python 3.10+ instalado; banco de dados é um único arquivo SQLite, sem dependência de serviço de banco externo. |
| **Auditabilidade** | Toda mutação de dado de negócio (criar/editar/excluir qualquer entidade) e todo evento de autenticação (login, logout, falha de login) gera um registro de auditoria (ver Épico 9, `user-stories.md`). |
| **Testabilidade** | Regras de validação (valores de story points/MoSCoW/RICE, fórmula RICE, RBAC) isoladas em funções puras/módulos de serviço, testáveis sem subir um servidor HTTP completo. |

## 3. Requisitos de Segurança

- **Autenticação**: sessão gerenciada por `Flask-Login`; nenhuma rota de dados acessível sem sessão válida (US-03).
- **Senhas**: hash com Argon2 (`argon2-cffi`); nunca armazenadas ou logadas em texto puro; nunca incluídas em respostas de erro (US-37).
- **Autorização (RBAC)**: papéis `user` e `admin`; verificação de papel feita no servidor (decorator/middleware), nunca apenas ocultando elementos de UI (US-33, US-34).
- **CSRF**: todo formulário POST/PUT/DELETE protegido por token CSRF (`Flask-WTF`) (US-37).
- **Cookies de sessão**: `HttpOnly`, `Secure` (obrigatório em produção com HTTPS), `SameSite=Lax` ou mais restritivo (US-37).
- **Cabeçalhos HTTP de segurança**: `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY` (ou equivalente `frame-ancestors`), via `Flask-Talisman`.
- **Criptografia em repouso**: campos marcados como sensíveis cifrados com Fernet (AES-128 autenticado) antes de gravar no SQLite; chave de criptografia fora do controle de versão, injetada via variável de ambiente (US-38).
- **Isolamento entre usuários**: um usuário nunca acessa dados de projeto de outro usuário, exceto o Administrador em modo somente-monitoramento (US-03, US-34).
- **Registro de tentativas de autenticação**: toda falha de login é auditada com e-mail tentado e timestamp, nunca com a senha tentada (US-35).

## 4. Requisitos de Interface com o Usuário

- Interface gráfica (GUI) via navegador — atende ao requisito (1) do enunciado.
- Layout responsivo o suficiente para uso em desktop (não há requisito de suporte mobile — ver `vision-and-scope.md`, Fora de Escopo).
- Formulários exibem erros de validação de forma clara, próximos ao campo, sem recarregar a página em branco.
- Ações destrutivas (excluir projeto/backlog/história/épico/critério) sempre pedem confirmação explícita antes de executar.
- Painel de Administrador visualmente distinto das telas de projeto comuns, para deixar claro que o usuário está fora do contexto de um projeto específico.

## 5. Requisitos de Interface com Dispositivos Externos

Não aplicável — o sistema não integra com dispositivos externos (sensores, hardware específico, impressoras etc.). Único "dispositivo" é o navegador do usuário, já coberto na seção 4.

## 6. Requisitos de Interface com Outros Sistemas de Software

Não aplicável no MVP — o sistema é autocontido, sem integração com APIs externas (ver `vision-and-scope.md`, Fora de Escopo: "Integração com ferramentas externas"). Não há webhooks, importação/exportação para outros sistemas nem SSO externo nesta versão.

## 7. Conformidade (Normas, Padrões, Métricas)

- **OWASP Top 10** (2021) usado como checklist de referência para as decisões de segurança da seção 3 (injeção, quebra de autenticação, exposição de dados sensíveis, controle de acesso quebrado, configuração incorreta de segurança).
- **OWASP ASVS** (nível 1) como referência informal para os controles de autenticação/sessão implementados.
- **PEP 8** como padrão de estilo de código Python.
- **Semantic Versioning** não se aplica a este trabalho acadêmico (sem múltiplas versões públicas do pacote), mas o histórico de commits do Git segue mensagens descritivas por mudança lógica.
- Nenhuma norma legal específica (ex.: LGPD) é tratada em profundidade, por se tratar de protótipo acadêmico sem dados reais de terceiros — mas os princípios de minimização de dados e proteção de senha (seção 3) já seguem o espírito de proteção de dados pessoais.

## 8. Restrições de Projeto (Design)

- Deve ser executável localmente com `flask run`, sem infraestrutura de nuvem obrigatória para a demonstração (ver `infrastructure.md`).
- Banco de dados único (SQLite) — decisão consciente que restringe escrita concorrente pesada, aceitável dado o uso individual/acadêmico (ver `tech-stack.md`).
- Sem SPA/build step de frontend — todas as páginas são server-rendered com Jinja2, para manter a arquitetura simples de descrever no architecture notebook.
- Prazo do trabalho acadêmico limita o escopo ao que está descrito em `vision-and-scope.md` (ver Fora de Escopo).

## 9. Aspectos de Licenciamento

- Repositório e código publicados sob licença **MIT** (a definir/adicionar arquivo `LICENSE` no repositório) — permissiva, adequada para um trabalho acadêmico de portfólio público no GitHub.
- Todas as bibliotecas listadas em `tech-stack.md` (Flask, SQLAlchemy, Flask-Login, Flask-WTF, Flask-Talisman, argon2-cffi, cryptography, python-dotenv) são open source com licenças permissivas (BSD/MIT/Apache-2.0), compatíveis com uso e redistribuição do projeto.

## 10. Requisitos de Documentação

- Documentação de planejamento entregue em pt-BR (`docs/pt-BR/`) para a disciplina, com espelho em inglês (`docs/en/`) para o repositório público no GitHub — ver `README.md`.
- Cada artefato exigido pelo enunciado (seção 3 de `docs/spec/ESW-TRABALHO-PRATICO.md`) corresponde a um arquivo versionado e rastreável no Git, com histórico de mudanças.
- README do repositório mantém um checklist de entrega atualizado conforme os artefatos são concluídos.
- Comentários de código reservados para decisões não óbvias (por que, não o quê) — sem docstrings extensas ou comentários redundantes com o próprio código.
