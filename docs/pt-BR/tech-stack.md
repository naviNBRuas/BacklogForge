# Decisão de Stack Técnica

## Escolha

- **Backend**: Python 3 + **Flask** (micro-framework — pouca configuração, direto ao ponto para um projeto solo).
- **Frontend**: **server-rendered** com **Jinja2** (templates do próprio Flask) + CSS simples. Sem SPA (React/Vue) — evita build tooling, bundlers e complexidade de estado no cliente que não trazem benefício para o escopo do trabalho.
- **Banco de dados**: **SQLite** — arquivo único, zero configuração de servidor, suficiente para um protótipo de demonstração, e serve diretamente como base para o artefato exigido "projeto físico de banco de dados".
- **Autenticação**: sessão simples do Flask (`flask-login` ou equivalente manual) + hash de senha (`werkzeug.security`).
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
- `Flask-Login` (sessão/autenticação)
- `Flask-WTF` (formulários + validação + proteção CSRF)
- `Werkzeug` (hash de senha — já vem com o Flask)
