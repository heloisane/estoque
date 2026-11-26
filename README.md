
# API Almoxarifado

Sistema de gerenciamento de estoque desenvolvido em Python utilizando FastAPI.

## Funcionalidades

- Listagem de produtos.
- Controle de entrada e saída de estoque.
- Cadastro e gerenciamento de solicitações.
- Aprovação e cancelamento de pedidos.
- Controle de acesso por usuário e permissões.

## Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie a API:

```bash
uvicorn main:app --reload
```

## Documentação

Acesse no navegador:

http://127.0.0.1:8000/docs

## Testes

Execute:

```bash
python -m testes.teste_api
```
