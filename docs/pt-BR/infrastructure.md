# Descrição da Infraestrutura de Implantação

*(Artefato 9 do trabalho prático: "descrição da infraestrutura de implantação, contemplando hardware, software e serviços".)*

## 1. Hardware

| Cenário | Requisito |
|---|---|
| Execução local (demonstração/avaliação) | Qualquer máquina capaz de rodar Python 3.10+: 1 vCPU, 512 MB de RAM e ~100 MB de disco livre já são suficientes (aplicação leve, SQLite embutido). |
| Implantação hospedada (opcional, produção) | Instância mínima de um provedor gratuito/baixo custo (ex.: 512 MB–1 GB de RAM) é suficiente dado o volume de uso individual/acadêmico (ver `non-functional-requirements.md` §8). |

## 2. Software

| Camada | Software necessário |
|---|---|
| Runtime | Python 3.10 ou superior |
| Gerenciador de pacotes | `pip` (+ `venv` para isolamento do ambiente) |
| Framework e bibliotecas | Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, Flask-Talisman, argon2-cffi, cryptography, python-dotenv (lista completa e versões em `requirements.txt`, a ser criado junto com o código) |
| Banco de dados | SQLite (embutido no Python — nenhuma instalação de servidor de banco separada) |
| Servidor de aplicação (produção) | `gunicorn` (ou equivalente WSGI) atrás de um proxy reverso, se implantado publicamente — para demonstração local, `flask run` é suficiente |
| Servidor web/proxy (produção) | Opcional: Nginx (ou o proxy do próprio provedor de hospedagem) para TLS/HTTPS e cabeçalhos adicionais |
| Sistema operacional | Qualquer um com suporte a Python 3 (Linux, macOS, Windows) — sem dependência de SO específico |
| Controle de versão | Git + GitHub (repositório público deste projeto) |

## 3. Serviços

| Serviço | Propósito | Necessário para... |
|---|---|---|
| Repositório Git remoto (GitHub) | Versionamento e histórico de mudanças (requisito de instrução 2 do enunciado) | Sempre |
| HTTPS/TLS (certificado) | Exigido pelas NFRs de segurança (`Secure` cookies, HSTS via Flask-Talisman) sempre que a aplicação for exposta fora de `localhost` | Apenas em implantação hospedada, não na demonstração local |
| Hospedagem de aplicação (opcional) | Ex.: Render, Railway ou PythonAnywhere — plano gratuito/hobby é suficiente para o volume esperado | Apenas se optar por demonstrar via URL pública em vez de vídeo/execução local |
| Armazenamento do arquivo SQLite | Disco persistente do próprio serviço de hospedagem (ou disco local, na demonstração) | Sempre — não há serviço de banco de dados gerenciado separado no MVP |

## 4. Variáveis de Ambiente e Segredos

Nenhum segredo é commitado no repositório (ver `.gitignore`). As seguintes variáveis são necessárias em tempo de execução:

| Variável | Propósito |
|---|---|
| `SECRET_KEY` | Chave de assinatura de sessão do Flask. |
| `DATABASE_URL` | Caminho do arquivo SQLite (default local se omitida). |
| `ENCRYPTION_KEY` | Chave Fernet para o mecanismo `EncryptedString` (ver `architecture-notebook.md` §5). |
| `ADMIN_EMAIL` / `ADMIN_PASSWORD` | Usadas apenas na primeira execução, para promover/criar a conta administradora inicial (ver `vision-and-scope.md` § RBAC). |

Em desenvolvimento local, essas variáveis são carregadas de um arquivo `.env` (via `python-dotenv`), que nunca é versionado.

## 5. Passos de Implantação (Resumo)

1. Provisionar o ambiente (local ou hospedado) com Python 3.10+.
2. Clonar o repositório e instalar dependências (`pip install -r requirements.txt`).
3. Definir as variáveis de ambiente da seção 4.
4. Executar as migrações/criação inicial do schema (`flask db upgrade` ou equivalente, a definir junto com o código).
5. Iniciar a aplicação: `flask run` (demonstração local) ou `gunicorn app:app` atrás de um proxy com HTTPS (hospedagem).
6. Verificar que a conta administradora inicial foi criada com sucesso e que o painel `/admin` está acessível apenas a ela.
