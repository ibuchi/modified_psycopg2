PostgreSQL Driver(Psycopg2) Modification
-----

## Introduction

This application modifies a PostgreSQL driver source(psycopg2) to return outputs in JSON string format. Python programming language was used to achieve this.

## Development Tools, Environment and Setup
# Tools
Programming Language- Python 3.10.4
Open Source PostgreSQL Driver- psycopg 2.9.6
Database- PostgreSQL

# Environment and Setup
1. **Download the project locally**
```
git clone 
```

2. **Activate the virtualenv using:**
```
virtualenv\scripts\activate
```
3. **Run the app using:**
```
python task.py
```
Note: Ensure to use the project's virtual environment as the modifications were made in the __init__.py file located in the venv folder.

Modified file directory: bitnine\venv\Lib\site-packages\psycopg2\__init__.py
