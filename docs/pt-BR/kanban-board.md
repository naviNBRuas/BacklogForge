# Quadro Kanban — Gerenciamento do Projeto BacklogForge

*(Artefato 1 do trabalho prático: "descrição do processo de gerenciamento contendo informação acerca do quadro e dos cartões usados")*

## Por que Kanban aqui

Projeto individual, com um conjunto conhecido e finito de artefatos a entregar (ver `README.md`) mais o desenvolvimento do protótipo. Kanban foi escolhido (é exigência do enunciado) por: visualizar todo o trabalho pendente/em andamento num único quadro, limitar o trabalho em progresso (importante para 1 pessoa só — evita abrir muitas frentes), e permitir que "artefato de documentação" e "tarefa de código" convivam no mesmo fluxo.

## Colunas do Quadro e Propósito de Cada Uma

| # | Coluna | Propósito |
|---|---|---|
| 1 | **Backlog** | Todo o trabalho identificado mas ainda não priorizado para ser iniciado. Entrada de novas ideias/tarefas conforme surgem. |
| 2 | **A Fazer (To Do)** | Trabalho já priorizado e pronto para ser puxado — pré-requisitos resolvidos, escopo claro o suficiente para começar. |
| 3 | **Em Progresso (In Progress)** | Trabalho sendo executado agora. **WIP limit = 1** (projeto solo — evita troca de contexto). |
| 4 | **Em Revisão (Review)** | Trabalho tecnicamente pronto, aguardando autorrevisão contra os critérios do enunciado antes de considerar concluído (ex.: reler o artefato comparando com a lista de critérios de avaliação do PDF). |
| 5 | **Concluído (Done)** | Trabalho revisado e finalizado — pronto para compor a entrega final (ZIP). |

> Fluxo: `Backlog → A Fazer → Em Progresso → Em Revisão → Concluído`. Cartões só voltam para trás (ex.: Revisão → A Fazer) se a autorrevisão encontrar um problema.

## Cartões — Formato

Cada cartão registra: **Nome**, **Descrição**, **Responsável** (sempre o autor, projeto individual), **Prioridade** (Alta/Média/Baixa), **Estimativa** (P/M/G — pequeno/médio/grande, dado o escopo acadêmico), **Datas** (criação / conclusão).

> **Este quadro é vivo**: seu estado (coluna "Status") reflete o progresso real do trabalho no momento da última atualização, e a seção "Histórico de Movimentação" abaixo registra cada transição de coluna com data — não é apenas uma descrição estática do processo, é a ferramenta efetivamente usada para gerenciar este projeto.

## Cartões

| Nome | Descrição | Responsável | Prioridade | Estimativa | Status | Criado em | Concluído em |
|---|---|---|---|---|---|---|---|
| Descrição do processo Kanban | Este documento (`kanban-board.md`) | autor | Alta | P | Concluído | 2026-08-27 | 2026-08-28 |
| Documento de visão e escopo | `vision-and-scope.md` — problema, stakeholders, escopo | autor | Alta | P | Concluído | 2026-08-27 | 2026-08-28 |
| Backlog de histórias de usuário (requisitos funcionais) | Épicos + histórias + critérios de aceitação cobrindo os 19 requisitos do enunciado | autor | Alta | G | Concluído | 2026-08-28 | 2026-08-28 |
| Especificação de requisitos não funcionais | Documento formal de NFRs (usabilidade, segurança, portabilidade, normas etc.) | autor | Alta | M | Em Progresso | 2026-08-27 | — |
| Architecture notebook | Descrição da arquitetura (objetivos, suposições, dependências, decisões, mecanismos, abstrações, impacto de Flask/SQLAlchemy/Jinja2) | autor | Alta | M | A Fazer | 2026-08-27 | — |
| Projeto de interface (storyboards + wireframes) | Um storyboard por cenário-chave de uso; wireframes simples por tela | autor | Média | M | Backlog | 2026-08-27 | — |
| Projeto físico de banco de dados | Diagrama + descrição de tabelas/colunas/chaves/relacionamentos | autor | Alta | M | Backlog | 2026-08-27 | — |
| Setup do projeto Flask | Estrutura de pastas, dependências, banco SQLite inicial, autenticação básica | autor | Alta | M | Backlog | 2026-08-27 | — |
| Implementação — Épico 1: Autenticação (US-01 a US-04) | Conta, login, restrição de acesso, logout | autor | Alta | M | Backlog | 2026-08-28 | — |
| Implementação — Épico 2: Projetos (US-05 a US-08) | CRUD de Projetos | autor | Alta | M | Backlog | 2026-08-28 | — |
| Implementação — Épico 3: Product Backlog (US-09, US-10) | CRUD de Product Backlog (1 por projeto) | autor | Alta | P | Backlog | 2026-08-28 | — |
| Implementação — Épico 4: Sprint Backlogs (US-11 a US-14) | CRUD de Sprint Backlogs (N por projeto) | autor | Alta | M | Backlog | 2026-08-28 | — |
| Implementação — Épico 5: Histórias de Usuário (US-15 a US-19) | CRUD + movimentação entre backlogs | autor | Alta | G | Backlog | 2026-08-28 | — |
| Implementação — Épico 6: Épicos (US-20 a US-23) | CRUD de Épicos + vínculo com histórias | autor | Média | M | Backlog | 2026-08-28 | — |
| Implementação — Épico 7: Critérios de Aceitação (US-24 a US-27) | CRUD, formato Dado/Quando/Então | autor | Alta | M | Backlog | 2026-08-28 | — |
| Implementação — Épico 8: Estimativa e Priorização (US-28 a US-32) | Story points, MoSCoW, RICE + cálculo e ordenação | autor | Alta | M | Backlog | 2026-08-28 | — |
| Implementação — Épico 9: RBAC, Segurança e Auditoria (US-33 a US-38) | Papéis Usuário/Administrador, criptografia em repouso, logging técnico e log de auditoria, painel do Administrador | autor | Alta | G | Backlog | 2026-08-28 | — |
| Protótipo funcional + vídeo de demonstração | Gravação cobrindo um cenário de sucesso por serviço | autor | Alta | M | Backlog | 2026-08-27 | — |
| Descrição da infraestrutura de implantação | Hardware/software/serviços necessários | autor | Média | P | Backlog | 2026-08-27 | — |
| Empacotar entrega (ZIP + teste de descompactação) | Nome `ESW-<matrícula>.ZIP`, checar integridade e ausência de vírus | autor | Alta | P | Backlog | 2026-08-27 | — |

> WIP atual (coluna Em Progresso): **1/1** — respeitando o limite. Novos cartões são adicionados ao Backlog conforme subtarefas emergem (ex.: os 8 cartões de implementação acima nasceram da quebra do Backlog de histórias de usuário em épicos, quando esse cartão foi concluído).

## Histórico de Movimentação

| Data | Cartão | De → Para | Observação |
|---|---|---|---|
| 2026-08-27 | Descrição do processo Kanban | Backlog → Em Progresso | Rascunho inicial do quadro. |
| 2026-08-27 | Documento de visão e escopo | Backlog → A Fazer | Rascunho iniciado em paralelo. |
| 2026-08-28 | Descrição do processo Kanban | Em Progresso → Em Revisão → Concluído | Estrutura de colunas/cartões validada contra os critérios de avaliação (item 01 do enunciado). |
| 2026-08-28 | Documento de visão e escopo | A Fazer → Em Progresso → Em Revisão → Concluído | Removida marcação de rascunho; conteúdo já cobria os pontos do critério de avaliação (item 02). |
| 2026-08-28 | Backlog de histórias de usuário | Backlog → Em Progresso → Em Revisão → Concluído | 32 histórias em 8 épicos escritas cobrindo os 19 requisitos; tabela de rastreabilidade conferida linha a linha. |
| 2026-08-28 | Especificação de requisitos não funcionais | Backlog → A Fazer → Em Progresso | Puxado para próximo, já que é o único artefato de "requisitos" ainda pendente e é pré-requisito conceitual da arquitetura. |
| 2026-08-28 | Implementação — Épicos 1 a 8 | (criados diretamente no Backlog) | Cartões de implementação derivados da quebra do backlog de histórias de usuário em épicos. |
| 2026-08-28 | Escopo: RBAC/segurança/logging | Fora de Escopo → Dentro do Escopo | Decisão do autor de tornar papéis (Usuário/Administrador) um controle de acesso real, com criptografia em repouso e logging/auditoria — atualizado em `vision-and-scope.md`, `tech-stack.md`; gerou o cartão "Implementação — Épico 9" e 6 novas histórias (US-33 a US-38) no backlog de histórias. |

## Próximo Passo Recomendado

Com o backlog de histórias de usuário concluído, o cartão em progresso é a **Especificação de requisitos não funcionais** — pré-requisito natural do **Architecture notebook** (próximo da fila em "A Fazer"), já que decisões de arquitetura respondem a requisitos não funcionais (desempenho, segurança, portabilidade etc.).
