# Engenharia de Software — Trabalho Prático

> Convertido do arquivo original `ESW-TRABALHO-PRÁTICO.pdf` (protegido por senha) para Markdown, para facilitar consulta durante o desenvolvimento. Este é o enunciado oficial da disciplina — texto preservado na íntegra, apenas reformatado.

## 1. Introdução

O trabalho consiste em construir artefatos por meio de processo de desenvolvimento iterativo e incremental. Para subsidiar a construção dos artefatos solicitados, podem ser acessados sistemas de software existentes. Por exemplo, acesso a sistemas existentes pode facilitar a construção de artefatos resultantes de atividades da disciplina requisitos de software.

## 2. Requisitos do Software

O sistema de software tem o propósito de prover suporte à gestão de requisitos em projetos onde histórias de usuário são usadas. A seguir, requisitos desse sistema de software:

1. Interface com o usuário embasada em texto (text user interface) ou gráfica (graphic user interface).
2. Para acessar os serviços disponibilizados, cada usuário deve criar uma conta e depois ser autenticado.
3. Uma vez autenticado, o usuário tem acesso aos serviços providos pelo sistema de software.
4. Possibilitar criação, leitura, atualização e exclusão de projetos.
5. Possibilitar criação, leitura, atualização e exclusão de product backlogs (pode existir só um product backlog por projeto).
6. Possibilitar criação, leitura, atualização e exclusão de sprint backlogs (podem existir vários sprint backlogs por projeto).
7. Possibilitar criação, leitura, atualização e exclusão de histórias de usuário (ao ser criada, história de usuário deve ser associada a product backlog).
8. Possibilitar a movimentação de histórias de usuário entre backlogs.
9. Prover o formato padrão para história de usuário: **Como um [papel] eu quero [ação] para [benefício]**.
10. Possibilitar criação, leitura, atualização e exclusão de épicos.
11. Possibilitar vinculação de histórias de usuário a épicos.
12. Possibilitar criação, leitura, atualização e exclusão de critérios de aceitação de histórias de usuário.
13. Prover o formato padrão para critério de aceitação de história de usuário: **Dado [contexto inicial ou o estado do sistema antes da ação acontecer] quando [ação ou evento específico que o usuário executa] então [resultado esperado ou a consequência daquela ação]**.
14. Possibilitar atribuição de pontos de história (story points) a histórias de usuário.
15. Pontos de história (story points) podem ter os valores 0, 1, 2, 3, 5, 8, 13, 21, 34 ou 55.
16. Possibilitar atribuição de etiqueta MoSCoW (M, S, C, W) a história de usuário.
17. Possibilitar atribuição de critério RICE (Reach, Impact, Confidence, Effort) a história de usuário.
18. Critério Reach (Alcance) deve ser número de usuários; critério Impact (Impacto) deve ser 3 (massivo), 2 (alto), 1 (médio), 0.5 (baixo) ou 0.25 (mínimo); critério Confidence (Confiança) deve ser valor percentual 100 (alta), 80 (média) ou 50 (baixa); critério Effort (Esforço) deve ser valor de pontos de história (0, 1, 2, 3, 5, 8, 13, 21, 34 ou 55).
19. Possibilitar o cálculo de pontuação segundo o critério RICE pela fórmula **(R × I × C) / E**.

Aos requisitos relacionados, podem ser acrescentados outros considerados necessários ao atendimento das necessidades das partes interessadas.

## 3. Artefatos a Serem Construídos e Entregues

1. Descrição do processo de gerenciamento contendo informação acerca do quadro e dos cartões usados.
2. Documento de visão e escopo (vision).
3. Especificação de requisitos não funcionais por meio de artefato para esse fim (system-wide requirements).
4. Especificação de requisitos funcionais por meio de histórias de usuário (user story).
5. Descrição da arquitetura do software (architecture notebook).
6. Projeto de interface com o usuário.
7. Projeto físico de banco de dados.
8. Protótipo do sistema e vídeo demonstrando teste de sistema do protótipo.
9. Descrição da infraestrutura de implantação (infrastructure) contemplando hardware, software e serviços.

## 4. Instruções

1. Realizar o trabalho individualmente ou em equipe com até cinco participantes.
2. Preferencialmente armazenar os artefatos em uma plataforma que possibilite o controle de versões.
3. Procurar adotar modelos (templates) na construção dos artefatos solicitados.
4. Preencher os documentos com clareza.
5. Revisar cada artefato (ortografia etc.) antes da entrega.
6. Prover documento informando quais artefatos foram construídos por cada membro da equipe.
7. Fornecer os documentos textuais em arquivos no formato PDF.
8. Adotar método Kanban no gerenciamento do projeto.
9. Criar quadro Kanban com colunas apropriadas.
10. Prover descrição de propósito de cada coluna do quadro Kanban.
11. Criar cartões para gerenciamento do projeto por meio do método Kanban.
12. Prover informação sobre cada cartão criado.
13. Especificação de requisito não funcional de prover informação sobre normas, padrões, métricas etc.
14. Criar histórias de usuário adotando modelo (Como ….. Eu quero ….. Para …..).
15. Descrição da arquitetura do software deve prover informação sobre elementos, relacionamentos etc.
16. Descrição da arquitetura do software deve informar impacto de ferramentas usadas (templates, bibliotecas etc.).
17. Representar projeto de interface com o usuário por storyboard composto por wireframes.
18. Construir cada wireframe como esboço simples de tela.
19. Representar projeto físico do banco de dados por diagrama e texto.
20. Para cada tabela, informar nome, colunas, chaves, relacionamentos com outras tabelas etc.
21. Para cada tabela prover descrição textual do seu propósito.
22. Projetar e construir protótipo do sistema.
23. Fornecer vídeo que demonstre correto funcionamento do protótipo por meio de teste de sistema.
24. Teste de sistema demonstrado no vídeo deve conter um cenário de sucesso para cada serviço provido.
25. Descrição da infraestrutura deve descrever hardware, software e serviços para sistema ser posto em produção.
26. Incluir todos os artefatos construídos em um arquivo ZIP e atribuir o nome `ESW-A-B-C-D-E-F.ZIP` ao arquivo.
27. No nome do arquivo ZIP, A, B, C, D, E e F devem ser os números de matrícula dos autores do trabalho.
28. Testar se o arquivo pode ser descompactado com sucesso e se não há vírus no mesmo.
29. Enviar o arquivo dentro do prazo.
30. Não cumprimento de requisitos resulta em redução de nota do trabalho.

## 5. Critérios de Avaliação

| # | Atividade | Peso | Comentário |
|---|---|---|---|
| 01 | Gerenciamento do projeto | 1 | Descritas atividades realizadas no gerenciamento do projeto. Adotado método Kanban. Criado quadro Kanban com colunas apropriadas. Provida descrição do propósito de cada coluna. Criados cartões para gerenciamento do projeto. Provida informação sobre cada cartão criado. |
| 02 | Visão e escopo | 1 | Descrito o problema resolvido pelo sistema de software. Descrita a posição que o sistema pretende ocupar no mercado. Descritas as partes interessadas (stakeholders) e suas responsabilidades. Descrito o ambiente de trabalho dos futuros usuários. Descritas as necessidades atendidas pelo sistema. Descritas resumidamente as funcionalidades a serem providas. Descritos resumidamente requisitos não funcionais. Descritos resumidamente elementos da solução proposta pela equipe de desenvolvimento. |
| 03 | Requisitos não funcionais | 1 | Descritos requisitos funcionais que não tenham sido especificados nas histórias de usuário. Descritos atributos de qualidade requeridos (usabilidade, desempenho etc.). Descritos requisitos quanto à interface com o usuário. Descritos requisitos quanto à interface com dispositivos externos. Descritos requisitos quanto à interface do sistema com outros sistemas. Relacionados aspectos aos quais o sistema deve estar conforme (normas, leis etc.). Documento relaciona restrições a serem observadas quando do projeto (design). Descritos aspectos de licenciamento. Descritos requisitos quanto à documentação. |
| 04 | Histórias de usuário | 1 | Cada requisito funcional descrito por história de usuário. Cada história de usuário é descrita segundo perspectiva do usuário final. Cada história de usuário escrita em linguagem informal. Cada história de usuário adota modelo (Como ….. Eu quero ….. Para …..). |
| 05 | Arquitetura | 1 | Descritos objetivos de arquitetura. Descritas suposições relativas à arquitetura. Descritas dependências consideradas na definição da arquitetura. Descritos requisitos relativos à arquitetura. Descritas decisões, restrições e justificativas relativas à arquitetura. Descritos mecanismos de arquitetura. Descritas abstrações relativas à arquitetura. Descrita arquitetura segundo determinadas perspectivas. Provida informação sobre impacto das ferramentas usadas (frameworks etc.) na arquitetura. |
| 06 | Interface com o usuário | 1 | Projeto de interface composto por storyboards. Cada storyboard descreve cenário de uso do sistema. Cada storyboard composto por sequência de wireframes. Cada wireframe é esboço simples de tela. |
| 07 | Banco de dados | 1 | Projeto físico do banco de dados composto por diagrama e texto. Fornecido diagrama que identifica tabelas e relacionamentos entre tabelas. Para cada tabela, é informado nome, colunas, chaves, relacionamentos etc. Para cada tabela é fornecida descrição textual do propósito da tabela. |
| 08 | Protótipo | 2 | Protótipo de acordo com o projeto (design). Protótipo demonstra sistema integrado (apresentação, negócio, armazenamento etc.). Protótipo provê as funcionalidades corretamente. |
| 09 | Infraestrutura de implantação | 1 | Provida informação sobre software necessário à implantação. Provida informação sobre hardware necessário à implantação. Provida informação sobre serviços necessários à implantação. |

Cada atividade é avaliada em uma escala de 0%, 25%, 50%, 75% ou 100%, ponderada pelo peso indicado.
