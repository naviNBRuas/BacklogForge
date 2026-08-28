# Projeto de Interface com o Usuário (Storyboards + Wireframes)

*(Artefato 6 do trabalho prático: "projeto de interface com o usuário", representado por storyboards compostos por wireframes — esboços simples de tela.)*

> Cada storyboard cobre um cenário-chave de uso do sistema, como uma sequência de telas (wireframes). Os wireframes são esboços de baixa fidelidade (ASCII), suficientes para comunicar layout e fluxo, não o visual final.

## Storyboard 1 — Cadastro, Login e Primeiro Projeto

*Cenário: um novo usuário cria uma conta, entra no sistema e cria seu primeiro projeto (US-01, US-02, US-05).*

```
┌─ Tela 1: Cadastro ──────────────┐   ┌─ Tela 2: Login ─────────────────┐
│ BacklogForge                    │   │ BacklogForge                    │
│                                  │   │                                  │
│ E-mail:    [______________]     │──▶│ E-mail:    [______________]     │
│ Senha:     [______________]     │   │ Senha:     [______________]     │
│ Confirmar: [______________]     │   │                                  │
│                                  │   │            [ Entrar ]           │
│            [ Criar conta ]      │   │  Não tem conta? Criar conta     │
│  Já tem conta? Entrar           │   │                                  │
└──────────────────────────────────┘   └──────────────┬───────────────────┘
                                                        ▼
┌─ Tela 3: Meus Projetos (vazio) ─────────────────────────────────────┐
│ BacklogForge          [meu@email.com ▾]  [Sair]                     │
│                                                                        │
│  Meus Projetos                                    [ + Novo Projeto ] │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  Nenhum projeto ainda. Crie o primeiro!                       │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────┬──────────────────────────────────┘
                                   ▼ (clica em "+ Novo Projeto")
┌─ Tela 4: Criar Projeto ──────────────────────────────────────────────┐
│  Nome:        [___________________________]                          │
│  Descrição:   [___________________________]                          │
│               [___________________________]                          │
│                                            [ Cancelar ] [ Criar ]     │
└───────────────────────────────────────────────┬──────────────────────┘
                                                  ▼
┌─ Tela 5: Página do Projeto ──────────────────────────────────────────┐
│ ← Meus Projetos    Projeto: "Sistema de Vendas"      [Editar][Excluir]│
│  [ Product Backlog ]  [ Sprints ]  [ Épicos ]                         │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  Product Backlog (0 histórias)              [+ Nova História]│   │
│  └──────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────┘
```

## Storyboard 2 — Criar História de Usuário com Critérios e Estimativa

*Cenário: o PO cria uma história no Product Backlog, adiciona critérios de aceitação e atribui story points/MoSCoW/RICE (US-15, US-24, US-28 a US-31).*

```
┌─ Tela 1: Product Backlog ───────────┐   ┌─ Tela 2: Nova História ────────────┐
│ Product Backlog     [+ Nova História]│──▶│ Como: [_______________________]   │
│  (lista vazia ou com histórias)      │   │ Eu quero: [___________________]   │
│                                       │   │ Para: [_______________________]   │
│                                       │   │              [Cancelar] [Salvar]  │
└───────────────────────────────────────┘   └────────────────┬─────────────────┘
                                                                ▼
┌─ Tela 3: Detalhes da História ───────────────────────────────────────────┐
│ ← Voltar    "Como cliente eu quero... para..."                           │
│                                                                            │
│  Story Points: [ 5 ▾]   MoSCoW: [ M ▾]   Épico: [ (nenhum) ▾]            │
│                                                                            │
│  RICE:  Reach [___]  Impact [3 ▾]  Confidence [100% ▾]  Effort [5 ▾]     │
│  Score RICE calculado: 60                                    [ Salvar ]  │
│                                                                            │
│  Critérios de Aceitação                              [+ Novo Critério]   │
│  ┌────────────────────────────────────────────────────────────────┐    │
│  │ (lista vazia)                                                    │    │
│  └────────────────────────────────────────────────────────────────┘    │
└───────────────────────────────────────────┬──────────────────────────────┘
                                             ▼ (clica "+ Novo Critério")
┌─ Tela 4: Novo Critério de Aceitação ───────────────────────────────────┐
│  Dado:   [_____________________________________]                      │
│  Quando: [_____________________________________]                      │
│  Então:  [_____________________________________]                      │
│                                          [ Cancelar ] [ Salvar ]        │
└─────────────────────────────────────────────────────────────────────────┘
```

## Storyboard 3 — Planejar uma Sprint (Mover Histórias entre Backlogs)

*Cenário: o PO cria uma sprint e move histórias do Product Backlog para ela (US-11, US-19).*

```
┌─ Tela 1: Aba "Sprints" do Projeto ──────┐   ┌─ Tela 2: Nova Sprint ────────────┐
│  Sprints                [+ Nova Sprint] │──▶│ Nome:  [___________________]    │
│  (lista vazia)                          │   │ Início: [___] Fim: [___]        │
│                                          │   │              [Cancelar][Criar]  │
└──────────────────────────────────────────┘   └────────────────┬─────────────────┘
                                                                  ▼
┌─ Tela 3: Product Backlog (com histórias) ────────────────────────────────┐
│  ☐ US-1 "Como cliente..."          RICE 60   [Mover para ▾: Sprint 1]    │
│  ☐ US-2 "Como PO..."               RICE 40   [Mover para ▾: Sprint 1]    │
│                                              [ Mover selecionadas ]       │
└──────────────────────────────────────┬─────────────────────────────────┘
                                        ▼
┌─ Tela 4: Sprint 1 (com histórias movidas) ───────────────────────────────┐
│ ← Sprints    Sprint 1 (01/09 – 14/09)                                    │
│  US-1 "Como cliente..."   RICE 60   [Devolver ao Product Backlog]        │
└────────────────────────────────────────────────────────────────────────┘
```

## Storyboard 4 — Painel do Administrador (RBAC + Auditoria)

*Cenário: uma conta com papel `admin` monitora usuários, projetos e o log de auditoria (US-33 a US-36).*

```
┌─ Tela 1: Login (conta admin) ───┐   ┌─ Tela 2: Painel do Administrador ───────────┐
│ E-mail: [admin@...]             │──▶│ [Painel Admin]      [meu@email.com ▾][Sair] │
│ Senha:  [_________]             │   │  [ Usuários ]  [ Projetos ]  [ Log de       │
│         [ Entrar ]              │   │                              Auditoria ]     │
└───────────────────────────────────┘   └───────────────┬───────────────────────────┘
                                                          ▼
┌─ Tela 3: Log de Auditoria ────────────────────────────────────────────────┐
│  Filtrar por: Usuário [___▾]  Ação [___▾]  Período [___] a [___] [Filtrar]│
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ 2026-08-28 14:02  ana@x.com   create   user_story #12               │ │
│  │ 2026-08-28 13:58  ana@x.com   login                                 │ │
│  │ 2026-08-28 13:50  bob@x.com   login_failed                          │ │
│  └────────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────────────┘
```

> Nota: uma conta `user` comum que tente acessar `/admin/*` diretamente pela URL recebe uma tela de erro 403 (Acesso Negado), não redirecionamento silencioso — reforça visualmente o RBAC descrito em `non-functional-requirements.md` §3.
