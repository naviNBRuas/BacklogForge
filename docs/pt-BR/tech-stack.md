# Decisão de Stack Técnica

## Escolha

- **Backend**: Python 3 + **Flask** (micro-framework — pouca configuração, direto ao ponto para um projeto solo).
- **Frontend**: **server-rendered** com **Jinja2** (templates do próprio Flask) + CSS simples. Sem SPA (React/Vue) — evita build tooling, bundlers e complexidade de estado no cliente que não trazem benefício para o escopo do trabalho.
- **Banco de dados**: **SQLite** — arquivo único, zero configuração de servidor, suficiente para um protótipo de demonstração, e serve diretamente como base para o artefato exigido "projeto físico de banco de dados".
- **Autenticação e autorização**: sessão do Flask via `Flask-Login`, com controle de acesso por papéis (RBAC — Usuário/Administrador) e hash de senha forte (`argon2` via `argon2-cffi`, com `werkzeug.security` como fallback).
- **Criptografia em repouso**: `cryptography` (Fernet, AES-128 autenticado) para campos sensíveis no banco; chave de criptografia vinda de variável de ambiente (`python-dotenv` em desenvolvimento), nunca commitada.
- **Segurança de aplicação web**: `Flask-WTF` (CSRF em todos os formulários), `Flask-Talisman` (cabeçalhos de segurança HTTP, cookies `Secure`/`HttpOnly`/`SameSite`, força HTTPS em produção).
- **Logging e auditoria**: módulo `logging` da biblioteca padrão com `RotatingFileHandler` para logs de aplicação; tabela dedicada `audit_logs` (via SQLAlchemy) para o log de auditoria de negócio (quem fez o quê, quando), consultável pelo Administrador.
- **Versionamento**: Git (requisito do enunciado — "plataforma que possibilite controle de versões").

## Por que essa combinação (dada a restrição: individual, web, "caminho mais simples")

| Alternativa considerada | Por que não |
|---|---|
| React/Next.js + API REST separada + Postgres | Duas camadas (frontend/backend) para manter sozinho; build tooling; overkill para 1 pessoa e um protótipo de demonstração |
| Node.js + Express + EJS + SQLite | Válido também, mas Flask tem menos boilerplate para CRUD simples e Jinja2 é mais direto que EJS para quem já pensa em Python |
| Django | Framework completo (admin, ORM, auth prontos) — poderia acelerar, mas tem mais "mágica"/convenções para aprender; Flask deixa a arquitetura mais explícita para o "architecture notebook" exigido |

**Trade-off aceito**: Flask exige montar manualmente peças que o Django dá de graça (auth, admin), mas isso é desejável aqui — o trabalho pede para **descrever decisões de arquitetura**, o que é mais natural quando as escolhas são explícitas.

## Requisitos do Enunciado que a Stack Atende Diretamente

- **(1) interface TUI ou GUI** → GUI via navegador (páginas Flask/Jinja2).
- **Projeto físico de banco de dados** → schema SQLite, com tabelas para `usuarios`, `projetos`, `product_backlogs`, `sprint_backlogs`, `epicos`, `historias_usuario`, `criterios_aceitacao`.
- **Protótipo + vídeo de teste de sistema** → app Flask local rodável com `flask run`, fácil de gravar em tela.
- **Infraestrutura de implantação** → hospedagem simples possível (ex.: Render, Railway, PythonAnywhere, ou execução local para a demo) — a ser detalhado no artefato de infraestrutura.

## Bibliotecas Previstas (a confirmar durante a implementação)

- `Flask`
- `Flask-SQLAlchemy` (ORM leve sobre SQLite — facilita descrever o projeto físico do banco e evita SQL cru espalhado pelo código)
- `Flask-Login` (sessão/autenticação + carregamento do usuário e seu papel a cada requisição)
- `Flask-WTF` (formulários + validação + proteção CSRF)
- `Flask-Talisman` (cabeçalhos de segurança HTTP e cookies seguros)
- `Werkzeug` (utilitários de segurança — já vem com o Flask)
- `argon2-cffi` (hash de senha com Argon2, recomendação atual da OWASP)
- `cryptography` (cifragem simétrica de campos sensíveis em repouso)
- `python-dotenv` (carregar segredos — `SECRET_KEY`, chave de criptografia — de variáveis de ambiente em desenvolvimento)

## Segurança, RBAC e Logging (detalhado em `docs/pt-BR/non-functional-requirements.md`)

- **RBAC**: dois papéis no MVP — `user` (padrão, dono de seus próprios projetos) e `admin` (papel global, visão de monitoramento). Aplicado via decorator (`@login_required` + verificação de papel) em toda rota sensível, não confiado apenas à UI.
- **Encryption at rest**: campos considerados sensíveis (a definir caso a caso — nenhum dado ultra-sensível existe no domínio além de credenciais, mas o padrão fica pronto para uso, ex.: notas privadas de um projeto) cifrados com Fernet antes de gravar no SQLite.
- **Logging**: dois tipos — (1) log técnico de aplicação (erros, requisições) via `logging`/`RotatingFileHandler`, para depuração; (2) log de auditoria de negócio (login, logout, falha de autenticação, criação/edição/exclusão de qualquer entidade), persistido em tabela própria e exposto num painel apenas ao Administrador.
