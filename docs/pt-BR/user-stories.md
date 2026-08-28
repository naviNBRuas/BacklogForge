# Backlog de Histórias de Usuário

*(Artefato 4 do trabalho prático: "especificação de requisitos funcionais por meio de histórias de usuário".)*

> Cobre os 19 requisitos numerados em [`docs/spec/ESW-TRABALHO-PRATICO.md`](../spec/ESW-TRABALHO-PRATICO.md) (seção 2). Cada história segue o formato `Como [papel] eu quero [ação] para [benefício]`; cada critério de aceitação segue `Dado/Quando/Então`. Papéis usados: **Usuário** (qualquer pessoa autenticada), **Product Owner (PO)** e **Desenvolvedor** (papéis dentro de um projeto — ver `vision-and-scope.md`).
>
> Cada história traz: Story Points (série 0,1,2,3,5,8,13,21,34,55), MoSCoW (M/S/C/W) e RICE (R×I×C/E). Estes três campos priorizam o *desenvolvimento* deste backlog (são atributos de gerenciamento do próprio trabalho, não do sistema construído) — o sistema deve, por sua vez, permitir que o usuário final atribua esses mesmos campos às histórias que ele cadastrar (requisitos 14–19).

## Épico 1 — Autenticação e Conta de Usuário

*Cobre requisitos (2), (3).*

### US-01 — Criar conta
Como **usuário**, eu quero criar uma conta com e-mail e senha, para poder acessar o sistema.

- **Critério de aceitação 1**: Dado que estou na tela de cadastro, quando informo e-mail, senha e confirmação de senha válidos, então minha conta é criada e a senha é armazenada com hash (nunca em texto puro).
- **Critério de aceitação 2**: Dado que informo um e-mail já cadastrado, quando envio o formulário de cadastro, então recebo uma mensagem de erro e a conta não é duplicada.

**Story Points**: 3 · **MoSCoW**: M (Must) · **RICE**: R=100, I=3, C=100%, E=3 → **100**

### US-02 — Autenticar-se
Como **usuário**, eu quero fazer login com e-mail e senha, para acessar os serviços do sistema.

- **Critério de aceitação 1**: Dado que possuo uma conta, quando informo e-mail e senha corretos, então sou autenticado e redirecionado à lista dos meus projetos.
- **Critério de aceitação 2**: Dado que informo credenciais incorretas, quando envio o formulário de login, então recebo uma mensagem de erro e permaneço não autenticado.

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=2 → **150**

### US-03 — Restringir acesso a usuários autenticados
Como **usuário**, eu quero que rotas de dados exijam login, para que meus projetos fiquem protegidos de acesso não autorizado.

- **Critério de aceitação 1**: Dado que não estou autenticado, quando tento acessar qualquer rota de projeto/backlog/história, então sou redirecionado à tela de login.
- **Critério de aceitação 2**: Dado que estou autenticado, quando acesso uma URL de projeto que não me pertence, então recebo erro de acesso negado (403/404), não os dados de outro usuário.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=3 → **67**

### US-04 — Encerrar sessão (logout)
Como **usuário**, eu quero encerrar minha sessão, para impedir que outra pessoa continue logada no meu lugar.

- **Critério de aceitação 1**: Dado que estou autenticado, quando clico em "Sair", então minha sessão é encerrada e sou redirecionado à tela de login.

**Story Points**: 1 · **MoSCoW**: S (Should) · **RICE**: R=100, I=1, C=100%, E=1 → **100**

## Épico 2 — Projetos

*Cobre requisito (4).*

### US-05 — Criar projeto
Como **usuário**, eu quero criar um projeto com nome e descrição, para começar a organizar seu backlog.

- **Critério de aceitação**: Dado que estou autenticado, quando preencho nome (obrigatório) e descrição e envio o formulário, então o projeto é criado, associado a mim, e um Product Backlog vazio é criado automaticamente para ele.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=3 → **100**

### US-06 — Listar e visualizar projetos
Como **usuário**, eu quero ver a lista dos meus projetos e abrir os detalhes de um deles, para acompanhar seu progresso.

- **Critério de aceitação**: Dado que tenho um ou mais projetos, quando acesso a tela inicial, então vejo todos os meus projetos listados; ao abrir um, vejo seus dados, seu Product Backlog e seus Sprint Backlogs.

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=2 → **100**

### US-07 — Editar projeto
Como **usuário**, eu quero atualizar nome/descrição de um projeto, para manter as informações corretas.

- **Critério de aceitação**: Dado que sou dono do projeto, quando altero nome/descrição e salvo, então os novos dados são persistidos e refletidos na listagem.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=100, I=1, C=100%, E=2 → **50**

### US-08 — Excluir projeto
Como **usuário**, eu quero excluir um projeto que não uso mais, para manter minha lista organizada.

- **Critério de aceitação 1**: Dado que sou dono do projeto, quando confirmo a exclusão, então o projeto e todos os seus dados dependentes (backlogs, histórias, épicos, critérios) são removidos.
- **Critério de aceitação 2**: Dado que solicito a exclusão, quando o sistema pede confirmação, então a exclusão só ocorre após confirmação explícita.

**Story Points**: 3 · **MoSCoW**: S · **RICE**: R=60, I=1, C=80%, E=3 → **16**

## Épico 3 — Product Backlog

*Cobre requisito (5).*

### US-09 — Visualizar o Product Backlog do projeto
Como **PO**, eu quero visualizar o Product Backlog do meu projeto, para ver todas as histórias ainda não movidas para uma sprint.

- **Critério de aceitação**: Dado que o projeto existe, quando acesso sua aba "Product Backlog", então vejo todas as histórias associadas a ele, ordenadas por prioridade (RICE ou MoSCoW).

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=2 → **100**

### US-10 — Editar dados do Product Backlog
Como **PO**, eu quero editar informações do Product Backlog (ex.: descrição/observações), para documentar seu propósito.

- **Critério de aceitação**: Dado que o Product Backlog existe (é criado junto com o projeto), quando edito sua descrição e salvo, então a alteração é persistida.

**Story Points**: 1 · **MoSCoW**: C (Could) · **RICE**: R=100, I=0.5, C=80%, E=1 → **40**

> Não há história de "criar/excluir Product Backlog" isolada: o requisito (5) determina que existe **exatamente um** Product Backlog por projeto, criado junto com ele (US-05) e removido junto com ele (US-08) — não faz sentido de negócio criar/excluir separadamente.

## Épico 4 — Sprint Backlogs

*Cobre requisito (6).*

### US-11 — Criar Sprint Backlog
Como **PO**, eu quero criar um novo Sprint Backlog dentro de um projeto, para planejar o trabalho de uma sprint.

- **Critério de aceitação**: Dado que estou na página do projeto, quando informo nome/período da sprint e confirmo, então um novo Sprint Backlog vazio é criado e listado entre os sprints do projeto.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=3 → **100**

### US-12 — Listar e visualizar Sprint Backlogs
Como **usuário**, eu quero ver todos os Sprint Backlogs de um projeto e abrir cada um, para acompanhar o planejamento das sprints.

- **Critério de aceitação**: Dado que o projeto tem um ou mais sprints, quando acesso sua aba de sprints, então vejo todos listados; ao abrir um, vejo as histórias nele contidas.

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=2 → **100**

### US-13 — Editar Sprint Backlog
Como **PO**, eu quero editar nome/período de um Sprint Backlog, para corrigir o planejamento.

- **Critério de aceitação**: Dado que o sprint existe, quando altero seus dados e salvo, então as mudanças são persistidas.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=90, I=1, C=80%, E=2 → **36**

### US-14 — Excluir Sprint Backlog
Como **PO**, eu quero excluir um Sprint Backlog, para remover uma sprint cancelada ou criada por engano.

- **Critério de aceitação**: Dado que o sprint existe, quando confirmo a exclusão, então o sprint é removido e suas histórias retornam automaticamente ao Product Backlog (não são apagadas).

**Story Points**: 3 · **MoSCoW**: S · **RICE**: R=70, I=1, C=80%, E=3 → **19**

## Épico 5 — Histórias de Usuário

*Cobre requisitos (7), (8), (9).*

### US-15 — Criar história de usuário
Como **PO**, eu quero criar uma história de usuário no formato `Como/Eu quero/Para`, para registrar um requisito funcional do sistema sendo planejado.

- **Critério de aceitação 1**: Dado que estou no Product Backlog de um projeto, quando preencho papel, ação e benefício e salvo, então a história é criada e associada automaticamente ao Product Backlog do projeto.
- **Critério de aceitação 2**: Dado que deixo algum dos três campos vazio, quando tento salvar, então recebo um erro de validação e a história não é criada.

**Story Points**: 5 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=5 → **60**

### US-16 — Listar e visualizar histórias
Como **usuário**, eu quero ver a lista de histórias de um backlog e abrir os detalhes de cada uma, para acompanhar seu conteúdo, estimativa e critérios.

- **Critério de aceitação**: Dado que o backlog tem histórias, quando o acesso, então vejo todas listadas com papel/ação/benefício resumidos; ao abrir uma, vejo seus critérios de aceitação, story points, MoSCoW e RICE.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=3 → **67**

### US-17 — Editar história de usuário
Como **PO**, eu quero editar o papel/ação/benefício de uma história, para corrigir ou refinar seu texto.

- **Critério de aceitação**: Dado que a história existe, quando altero seu texto e salvo, então a nova versão é persistida.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=90, I=1, C=90%, E=2 → **41**

### US-18 — Excluir história de usuário
Como **PO**, eu quero excluir uma história de usuário obsoleta, para manter o backlog limpo.

- **Critério de aceitação**: Dado que a história existe, quando confirmo a exclusão, então ela e seus critérios de aceitação associados são removidos.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=70, I=1, C=80%, E=2 → **28**

### US-19 — Mover história entre backlogs
Como **PO**, eu quero mover uma história do Product Backlog para um Sprint Backlog (e vice-versa), para planejar o que será feito em cada sprint.

- **Critério de aceitação 1**: Dado que uma história está no Product Backlog, quando seleciono um Sprint Backlog de destino e confirmo, então a história passa a pertencer a esse sprint e some da listagem do Product Backlog.
- **Critério de aceitação 2**: Dado que uma história está em um Sprint Backlog, quando escolho "devolver ao Product Backlog", então ela retorna a ele.

**Story Points**: 5 · **MoSCoW**: M · **RICE**: R=100, I=3, C=90%, E=5 → **54**

## Épico 6 — Épicos

*Cobre requisitos (10), (11).*

### US-20 — Criar épico
Como **PO**, eu quero criar um épico com nome e descrição, para agrupar histórias relacionadas a um tema maior.

- **Critério de aceitação**: Dado que estou no projeto, quando informo nome/descrição do épico e salvo, então o épico é criado e listado no projeto.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=80, I=1, C=80%, E=2 → **32**

### US-21 — Listar e visualizar épicos
Como **usuário**, eu quero ver os épicos de um projeto e as histórias vinculadas a cada um, para entender o progresso de um tema maior.

- **Critério de aceitação**: Dado que existem épicos com histórias vinculadas, quando abro um épico, então vejo sua descrição e a lista de histórias associadas.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=80, I=1, C=80%, E=2 → **32**

### US-22 — Editar e excluir épico
Como **PO**, eu quero editar ou excluir um épico, para corrigir seu conteúdo ou removê-lo se não fizer mais sentido.

- **Critério de aceitação 1**: Dado que o épico existe, quando altero seus dados e salvo, então a alteração é persistida.
- **Critério de aceitação 2**: Dado que excluo um épico, quando confirmo, então o épico é removido e as histórias vinculadas a ele permanecem no sistema, apenas desvinculadas.

**Story Points**: 2 · **MoSCoW**: C · **RICE**: R=60, I=0.5, C=80%, E=2 → **12**

### US-23 — Vincular história a um épico
Como **PO**, eu quero vincular uma história de usuário a um épico, para relacioná-la a um objetivo maior do produto.

- **Critério de aceitação 1**: Dado que existe ao menos um épico no projeto, quando abro uma história e seleciono um épico, então a história passa a exibir esse vínculo.
- **Critério de aceitação 2**: Dado que uma história está vinculada a um épico, quando removo o vínculo, então a história permanece existindo, apenas sem épico associado.

**Story Points**: 3 · **MoSCoW**: S · **RICE**: R=80, I=1, C=80%, E=3 → **21**

## Épico 7 — Critérios de Aceitação

*Cobre requisitos (12), (13).*

### US-24 — Criar critério de aceitação
Como **PO**, eu quero adicionar critérios de aceitação a uma história no formato `Dado/Quando/Então`, para deixar claro quando a história pode ser considerada pronta.

- **Critério de aceitação 1**: Dado que estou na página de uma história, quando preencho contexto, ação e resultado esperado e salvo, então um novo critério é criado e listado nessa história.
- **Critério de aceitação 2**: Dado que deixo algum dos três campos vazio, quando tento salvar, então recebo um erro de validação.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=3 → **67**

### US-25 — Listar critérios de uma história
Como **usuário**, eu quero ver todos os critérios de aceitação de uma história, para entender completamente o que precisa ser validado.

- **Critério de aceitação**: Dado que a história tem um ou mais critérios, quando abro seus detalhes, então todos os critérios aparecem listados na ordem em que foram criados.

**Story Points**: 1 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=1 → **200**

### US-26 — Editar critério de aceitação
Como **PO**, eu quero editar um critério de aceitação existente, para corrigir ou refinar sua descrição.

- **Critério de aceitação**: Dado que o critério existe, quando altero seu texto e salvo, então a nova versão é persistida.

**Story Points**: 2 · **MoSCoW**: S · **RICE**: R=90, I=1, C=90%, E=2 → **41**

### US-27 — Excluir critério de aceitação
Como **PO**, eu quero excluir um critério de aceitação obsoleto, para manter a história com critérios relevantes.

- **Critério de aceitação**: Dado que o critério existe, quando confirmo a exclusão, então ele é removido da história.

**Story Points**: 1 · **MoSCoW**: S · **RICE**: R=70, I=1, C=90%, E=1 → **63**

## Épico 8 — Estimativa e Priorização (Story Points, MoSCoW, RICE)

*Cobre requisitos (14), (15), (16), (17), (18), (19).*

### US-28 — Atribuir story points a uma história
Como **PO**, eu quero atribuir pontos de história a uma história de usuário, para estimar seu esforço relativo.

- **Critério de aceitação 1**: Dado que estou editando uma história, quando seleciono um valor de story points, então só os valores 0, 1, 2, 3, 5, 8, 13, 21, 34 ou 55 estão disponíveis para escolha.
- **Critério de aceitação 2**: Dado que tento enviar um valor fora dessa série (ex.: via requisição manual), quando o sistema valida, então a atribuição é rejeitada com erro de validação.

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=2 → **100**

### US-29 — Atribuir etiqueta MoSCoW a uma história
Como **PO**, eu quero atribuir uma etiqueta MoSCoW (M, S, C ou W) a uma história, para comunicar sua prioridade qualitativa ao time.

- **Critério de aceitação**: Dado que estou editando uma história, quando seleciono uma das quatro opções (Must, Should, Could, Won't) e salvo, então a etiqueta é exibida junto à história nas listagens.

**Story Points**: 2 · **MoSCoW**: M · **RICE**: R=100, I=2, C=100%, E=2 → **100**

### US-30 — Atribuir critérios RICE a uma história
Como **PO**, eu quero atribuir Reach, Impact, Confidence e Effort a uma história, para calcular sua prioridade quantitativa.

- **Critério de aceitação 1**: Dado que estou editando uma história, quando informo Reach (número de usuários), Impact (3, 2, 1, 0.5 ou 0.25), Confidence (100%, 80% ou 50%) e Effort (0,1,2,3,5,8,13,21,34,55), então os valores são salvos.
- **Critério de aceitação 2**: Dado que informo um valor de Impact, Confidence ou Effort fora das opções válidas, quando tento salvar, então recebo um erro de validação.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=3 → **100**

### US-31 — Calcular e exibir a pontuação RICE
Como **PO**, eu quero que o sistema calcule automaticamente a pontuação RICE de uma história, para não precisar calcular manualmente `(R×I×C)/E`.

- **Critério de aceitação 1**: Dado que uma história tem Reach, Impact, Confidence e Effort preenchidos, quando visualizo a história (ou a listagem do backlog), então a pontuação RICE calculada é exibida.
- **Critério de aceitação 2**: Dado que Effort é maior que zero e os demais campos têm valores válidos, quando o cálculo é executado, então o resultado é exatamente `(Reach × Impact × Confidence) / Effort`.

**Story Points**: 3 · **MoSCoW**: M · **RICE**: R=100, I=3, C=100%, E=3 → **100**

### US-32 — Ordenar backlog por prioridade
Como **PO**, eu quero ordenar as histórias de um backlog por pontuação RICE (ou por etiqueta MoSCoW), para decidir rapidamente o que atacar primeiro.

- **Critério de aceitação**: Dado que o backlog tem histórias com RICE calculado, quando escolho "ordenar por RICE", então as histórias aparecem da maior para a menor pontuação.

**Story Points**: 3 · **MoSCoW**: C · **RICE**: R=90, I=1, C=80%, E=3 → **24**

## Resumo por Prioridade MoSCoW

| MoSCoW | Histórias |
|---|---|
| **Must (M)** | US-01, US-02, US-03, US-05, US-06, US-09, US-11, US-12, US-15, US-16, US-19, US-24, US-25, US-28, US-29, US-30, US-31 |
| **Should (S)** | US-04, US-07, US-08, US-13, US-14, US-17, US-18, US-20, US-21, US-23, US-26, US-27 |
| **Could (C)** | US-10, US-22, US-32 |
| **Won't (this release)** | — (nenhuma identificada fora do escopo do MVP descrito em `vision-and-scope.md`) |

## Rastreabilidade com os Requisitos do Enunciado

| Requisito (enunciado, seção 2) | Histórias |
|---|---|
| (1) Interface TUI/GUI | Atendido pela stack (ver `tech-stack.md`), não gera história própria — é uma NFR. |
| (2), (3) Conta e autenticação | US-01, US-02, US-03, US-04 |
| (4) CRUD de Projetos | US-05 a US-08 |
| (5) CRUD de Product Backlog | US-09, US-10 |
| (6) CRUD de Sprint Backlogs | US-11 a US-14 |
| (7) CRUD de Histórias de Usuário | US-15 a US-18 |
| (8) Mover histórias entre backlogs | US-19 |
| (9) Formato padrão da história | US-15 (critério de aceitação 1) |
| (10) CRUD de Épicos | US-20 a US-22 |
| (11) Vincular história a épico | US-23 |
| (12) CRUD de Critérios de Aceitação | US-24 a US-27 |
| (13) Formato padrão do critério de aceitação | US-24 (critério de aceitação 1) |
| (14), (15) Story points | US-28 |
| (16) Etiqueta MoSCoW | US-29 |
| (17), (18) Critérios RICE | US-30 |
| (19) Cálculo da pontuação RICE | US-31 |
