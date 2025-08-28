# ETL Template

A **professional and modular ETL project template**, designed following best practices in **data engineering**. Ideal for building robust, maintainable, and testable ETL pipelines for APIs, RPA, databases, and file-based workflows. This template is structured to be used as a **portfolio project** or as a starting point for production-grade ETL solutions.

## Project Structure

```bash
etl-template/
│
├── config/            # Configuration files (YAML, JSON) and environment variables
├── src/
│   ├── core/          # Base classes and pipeline framework for ETL processes
│   │   ├── base_etl.py
│   │   ├── pipeline.py
│   │   └── helpers.py
│   ├── api/           # ETL pipelines for API-based data sources
│   │   ├── extract/   # Functions to extract data from APIs
│   │   ├── transform/ # Data cleaning, normalization, aggregation
│   │   └── saver/     # Save data to database (SQL Server via pyodbc)
│   ├── bot/           # ETL pipelines for RPA / Selenium / Bot-based sources
│   │   ├── extract/
│   │   ├── transform/
│   │   └── saver/
│   ├── db/            # Database connector and SQL query templates
│   └── utils/         # Utility functions (logging, date handling, driver setup)
├── tests/             # Unit and integration tests with pytest, fixtures, mocks
├── notebooks/         # Example Jupyter notebooks for testing and demonstration
├── dags/              # Airflow DAGs for scheduling ETL jobs (optional)
├── .env               # Environment variables for credentials and configs
└── README.md
```

## Features

- Modular ETL architecture for **API and Bot data sources**
- **Database-agnostic design** using pyodbc for SQL Server (can be extended to other DBs)
- **Logging** and debugging with Loguru
- **Unit and integration tests** using pytest with mocks and fixtures
- **Professional folder structure** following Python best practices
- Optional integration with **Airflow** for orchestration
- Ready-to-use **notebooks** for analysis, validation, and demonstration

## Technologies & Dependencies

- Python 3.11+
- **Pandas** – data manipulation
- **PyODBC** – database connectivity (SQL Server)
- **Pytest** – testing framework
- **Loguru** – advanced logging
- **YAML/JSON** – configuration management
- Optional: Docker for environment reproducibility  
- Optional: Apache Airflow for ETL scheduling

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/seu-usuario/etl-template.git
cd etl-template
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
- Create a .env file in the project root:

```bash
SQL_SERVER=your_sql_server
SQL_DATABASE=your_database
SQL_USERNAME=your_username
SQL_PASSWORD=your_password
```

### 4. Run the ETL
```bash
python main.py
```

- Supports API ETL and Bot/RPA ETL flows
- Logs progress and errors in the console

### 5. Run Tests
```bash
pytest --cov=src --maxfail=1 --disable-warnings -q
```

- Tests include unit and integration tests
- Mocks are provided for API responses and Bot data
- Coverage reports can be generated for portfolio showcase

## Best Practices Implemented

- Separation of concerns: Extract / Transform / Load are in separate modules
- Clean code & type hints: All Python code includes type hints and professional docstrings
- Environment variables & configuration files: Credentials and endpoints are never hardcoded
- Test-driven design: Unit tests and integration tests cover all ETL flows
- Mocking & fixtures: Enables offline testing without production dependencies

## Contributing

1. Fork the repository  
2. Create a feature branch: `git checkout -b feature-name`  
3. Commit your changes: `git commit -m "Add feature"`  
4. Push to the branch: `git push origin feature-name`  
5. Open a Pull Request 