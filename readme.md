# Python Task Application

This project modifies the source code of the PostgreSQL driver, `psycopg2`, to return query results in JSON string format. The Python programming language is used for the modification.

## Development Tools, Environment, and Setup

### Tools

- Programming Language: Python 3.10.4
- Open Source PostgreSQL Driver: `psycopg2` version 2.9.6
- Database: PostgreSQL

### Environment and Setup

1. **Download the project**

Clone the project repository from GitHub:

```
git clone https://github.com/ibuchi/modified_psycopg2.git
```

2. **Install and activate a virtual environment**

Install the virtual environment package using the following command:

```
pip install virtualenv
```

Create a new virtual environment named `venv` using the following command:

```
virtualenv\venv
```

Activate the virtual environment using the following command:

```
virtualenv\scripts\activate
```

Note: The commands given above are for a Windows operating system. If you're using a different operating system, please refer to the virtual environment documentation for the appropriate commands.

3. **Install the project dependencies**

Install the project dependencies using the following command:

```
pip install -r requirements.txt
```

Note: Replace the `psycopg2` folder located in the activated virtual environment's directory (`venv\Lib\site-packages`) with the modified `psycopg2` folder in the root directory of this project. Please refer to the modified driver file (`__init__.py`) located in the `\psycopg2` directory.

4. **Start the PostgreSQL server**

Start the PostgreSQL server using the following command:

```
pg_ctl -D <path-to-data-directory> start
```

5. **Run the application**

Run the application using the following command:

```
python task.py
```

This will run the application and return query results in JSON string format to the terminal.