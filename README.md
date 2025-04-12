# Projeto de Faculdade - Programação Orientada a Objetos

Este projeto foi desenvolvido como parte das atividades acadêmicas da faculdade, com foco em conceitos de **Programação Orientada a Objetos** utilizando o framework Django.

## Passo a Passo para Subir uma Instância de Desenvolvimento

Siga os passos abaixo para configurar e executar o projeto em um ambiente de desenvolvimento:

### 1. Baixar o Repositório

Clone o repositório do projeto para sua máquina local utilizando o comando:

```bash
git clone https://github.com/valdeirsapara/siscursor.git
```


### 2. Copiar o arquivo `.env.example` para `.env`

O arquivo `.env` é usado para configurar variáveis de ambiente essenciais para o funcionamento do projeto. Para criar o arquivo, execute:

```bash
cp .env.example .env
```

> **Nota:** Certifique-se de configurar corretamente as variáveis no arquivo `.env`, como `SECRET_KEY` e `ALLOWED_HOSTS`. Essas variáveis são importantes para a segurança e o funcionamento do projeto.

### 3. Criar o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto. Execute o comando abaixo:

```bash
python -m venv ENV
```

### 4. Ativar o Ambiente Virtual

- **No Windows**:
  ```bash
  ENV\Scripts\activate
  ```

- **No Linux/Mac**:
  ```bash
  source ENV/bin/activate
  ```

### 5. Instalar as Dependências do Projeto

Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 6. Configurar as Variáveis do `.env`

As variáveis no arquivo `.env` são fundamentais para o funcionamento do projeto. Por exemplo:

- `SECRET_KEY`: Chave secreta usada pelo Django para segurança.
- `DEBUG`: Define se o modo de depuração está ativado.
- `ALLOWED_HOSTS`: Lista de hosts permitidos para acessar o projeto.

Certifique-se de preencher essas variáveis corretamente antes de iniciar o servidor.

### 7. Executar o Servidor de Desenvolvimento

Após configurar tudo, inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

O projeto estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

**Nota:** Este projeto é apenas para fins acadêmicos e não deve ser usado em produção sem as devidas configurações de segurança.