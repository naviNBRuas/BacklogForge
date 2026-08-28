# Visão e Escopo (Vision and Scope) — Rascunho

> Rascunho inicial para orientar o backlog. Deve ser revisado/expandido para virar o artefato formal "Documento de visão e escopo" exigido na entrega.

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
| Professor/avaliador (ESW) | Avalia o sistema como trabalho prático da disciplina |

## Ambiente dos Futuros Usuários

- Acesso via navegador web, desktop (não há requisito de app mobile).
- Uso individual ou em pequenos times — cada conta vê os projetos de que participa (no MVP: cada usuário só vê seus próprios projetos, sem multiusuário colaborativo — ver "Fora de Escopo").

## Necessidades Atendidas

- Estruturar requisitos de um projeto usando o vocabulário de histórias de usuário sem depender de planilhas ad hoc.
- Mover histórias entre backlogs (produto ↔ sprints) conforme o planejamento avança.
- Priorizar por dois métodos complementares: **MoSCoW** (qualitativo) e **RICE** (quantitativo).

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

## Requisitos Não Funcionais (resumo — detalhar no artefato de NFR)

- Usabilidade: CRUDs devem seguir um padrão de navegação consistente entre as entidades.
- Portabilidade: rodar em qualquer ambiente com Python 3 instalado (SQLite embutido).
- Segurança básica: senha nunca armazenada em texto puro; sessão exigida para todas as rotas de dados.

## Fora de Escopo (MVP)

- Colaboração multiusuário em tempo real no mesmo projeto (ex.: múltiplos POs editando simultaneamente).
- Notificações/e-mail.
- Integração com ferramentas externas (Jira, GitHub Issues).
- Aplicativo mobile nativo.

## Elementos da Solução Proposta

Aplicação web monolítica (Flask + SQLite), autenticação por sessão, CRUD server-rendered para cada entidade do domínio, e uma view de cálculo/exibição do score RICE por história.
