# ETL Template

Este repositório serve como **template profissional para projetos ETL**, organizado de forma modular, seguindo boas práticas de engenharia de dados.

## Estrutura do projeto

- `config/` → Configurações de ambiente, conexões, credenciais.
- `src/extract/` → Extração de dados (APIs, bancos de dados, arquivos).
- `src/transform/` → Transformações de dados (limpeza, normalização, agregações).
- `src/load/` → Carregamento em Data Warehouse ou banco de dados.
- `src/utils/` → Funções auxiliares (logging, conexão, validações).
- `tests/` → Testes unitários e de integração.
- `notebooks/` → Notebooks para análise e demonstração.
- `dags/` → DAGs de Airflow (se aplicável).

## Tecnologias

- Python 3.11+
- Pandas, SQLAlchemy
- Pytest
- Docker (opcional)
- Airflow (opcional)

## Como usar

1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/etl-template.git
cd etl-template
