# Roteiro do Vídeo de Demonstração

*(Apoio às Instruções 23–24 do enunciado: o vídeo deve demonstrar o funcionamento correto do protótipo, com um cenário de sucesso para cada serviço provido. Este roteiro garante que nenhum serviço fique de fora da gravação.)*

> Sugestão: gravar em uma única sessão contínua, seguindo a ordem abaixo — ela corresponde ao fluxo natural de uso do sistema (Épicos 1 a 9 do backlog de histórias).

## Checklist de Cenários (um por serviço)

- [ ] **1. Autenticação** — criar conta (US-01), tentar acessar `/projects/` sem login e ser redirecionado (US-03), logar (US-02), sair (US-04).
- [ ] **2. Projetos** — criar um projeto (US-05), ver na listagem (US-06), editar nome/descrição (US-07).
- [ ] **3. Product Backlog** — abrir o Product Backlog criado automaticamente (US-09), editar suas notas (US-10).
- [ ] **4. Sprint Backlogs** — criar uma sprint (US-11), abrir a lista de sprints do projeto (US-12), editar a sprint (US-13).
- [ ] **5. Histórias de Usuário** — criar uma história no Product Backlog no formato Como/Quero/Para (US-15), ver seus detalhes (US-16), editar (US-17), mover para a sprint criada (US-19).
- [ ] **6. Épicos** — criar um épico (US-20), abrir a lista de épicos (US-21), vincular a história do passo 5 ao épico (US-23).
- [ ] **7. Critérios de Aceitação** — adicionar um critério Dado/Quando/Então à história (US-24), ver a lista de critérios (US-25), editar o critério (US-26).
- [ ] **8. Estimativa e Priorização** — atribuir story points, MoSCoW e critérios RICE à história (US-28 a US-30), mostrar a pontuação RICE calculada automaticamente (US-31), ordenar o Product Backlog por RICE e por MoSCoW (US-32).
- [ ] **9. RBAC, Segurança e Auditoria** — logar como Administrador (conta seed), abrir o painel `/admin` (US-33, US-34), mostrar o log de auditoria contendo as ações gravadas nos passos anteriores (US-35, US-36); tentar acessar `/admin` com a conta comum e mostrar o erro 403 (reforça RBAC).
- [ ] **Exclusões** (opcional, mas recomendado): excluir um critério, uma história, um épico, uma sprint (mostrando que as histórias retornam ao Product Backlog) e, por fim, o projeto inteiro (mostrando a exclusão em cascata).

## Observações Técnicas para a Gravação

- Rodar localmente com `flask --app run.py run` (ver `README.md`, seção "Running Locally") — não é necessário implantar em produção para o vídeo.
- Mostrar a barra de endereço do navegador em cada transição de tela, para deixar claro que se trata de páginas reais servidas pelo Flask (não mockups).
- Ao demonstrar o RBAC (passo 9), deixar explícito que são duas contas diferentes (usuário comum vs. administrador) — por exemplo, mostrando o e-mail logado no canto superior direito antes e depois de trocar de conta.
