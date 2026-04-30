# Atividade didática: LGPD (Fatec Rio Claro)

Este projeto aplica conceitos da **Lei Geral de Proteção de Dados** em um banco de dados PostgreSQL utilizando Python.

## O que o script faz:
* **Anonimização:** Mascara Nome, CPF, E-mail e Telefone para proteger a privacidade.
* **Relatórios por Ano:** Gera um arquivo `.csv` para cada ano de nascimento com dados protegidos.
* **Dados Brutos:** Cria o arquivo `todos.csv` com nomes e CPFs originais para uso administrativo.
* **Logs de Performance:** Registra o tempo de execução no arquivo `log_execucao.txt`.

## Como usar:
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute o script: `python LGPD.py`

---
> **Observação:** Trabalho prático desenvolvido para fins estritamente didáticos.
