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

## Cartões Iniciais

| Nome | Descrição | Responsável | Prioridade | Estimativa | Status |
|---|---|---|---|---|---|
| Descrição do processo Kanban | Este documento (`kanban-board.md`) | autor | Alta | P | Em Progresso |
| Documento de visão e escopo | `vision-and-scope.md` — problema, stakeholders, escopo | autor | Alta | P | A Fazer (rascunho já iniciado) |
| Especificação de requisitos não funcionais | Documento formal de NFRs (usabilidade, segurança, portabilidade, etc.) | autor | Alta | M | Backlog |
| Backlog de histórias de usuário (requisitos funcionais) | Épicos + histórias + critérios de aceitação cobrindo os 19 requisitos do enunciado | autor | Alta | G | Backlog |
| Architecture notebook | Descrição da arquitetura (elementos, relacionamentos, impacto de Flask/SQLAlchemy/Jinja2) | autor | Alta | M | Backlog |
| Projeto de interface (storyboards + wireframes) | Um storyboard por cenário-chave de uso; wireframes simples por tela | autor | Média | M | Backlog |
| Projeto físico de banco de dados | Diagrama + descrição de tabelas/colunas/chaves/relacionamentos | autor | Alta | M | Backlog |
| Setup do projeto Flask | Estrutura de pastas, dependências, banco SQLite inicial, autenticação básica | autor | Alta | M | Backlog |
| CRUD de Projetos | Implementação da entidade Projeto | autor | Alta | M | Backlog |
| CRUD de Product Backlog | Implementação (1 por projeto) | autor | Alta | M | Backlog |
| CRUD de Sprint Backlogs | Implementação (N por projeto) | autor | Alta | M | Backlog |
| CRUD de Histórias de Usuário + movimentação entre backlogs | Inclui formato Como/Quero/Para | autor | Alta | G | Backlog |
| CRUD de Épicos + vínculo com histórias | | autor | Média | M | Backlog |
| CRUD de Critérios de Aceitação | Formato Dado/Quando/Então | autor | Alta | M | Backlog |
| Story points, MoSCoW e RICE | Campos + cálculo automático do score RICE | autor | Alta | M | Backlog |
| Protótipo funcional + vídeo de demonstração | Gravação cobrindo um cenário de sucesso por serviço | autor | Alta | M | Backlog |
| Descrição da infraestrutura de implantação | Hardware/software/serviços necessários | autor | Média | P | Backlog |
| Empacotar entrega (ZIP + teste de descompactação) | Nome `ESW-<matrícula>.ZIP`, checar integridade e ausência de vírus | autor | Alta | P | Backlog |

> Este quadro evolui ao longo do trabalho — novos cartões são adicionados ao Backlog conforme subtarefas emergem (ex.: cada história de usuário do próprio sistema pode virar um cartão de implementação quando chegar sua vez).

## Próximo Passo Recomendado

Com o quadro criado, o próximo cartão a puxar para "Em Progresso" é o **Documento de visão e escopo** (já rascunhado em `vision-and-scope.md`) e, em paralelo/logo a seguir, o **Backlog de histórias de usuário** — que é o maior artefato e a base para todo o resto (arquitetura, UI, banco de dados derivam dele).
