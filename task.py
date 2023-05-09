import psycopg2

from psycopg2 import JSONCursor

# --------------------------------------------------------------------------------------#
# Database Connection
# --------------------------------------------------------------------------------------#
connection = psycopg2.connect('user=postgres dbname=task')

# --------------------------------------------------------------------------------------#
# Cursor Connection
# --------------------------------------------------------------------------------------#
cursor = connection.cursor(cursor_factory=JSONCursor)

# --------------------------------------------------------------------------------------#
# Create User Table
# --------------------------------------------------------------------------------------#
cursor.execute('DROP TABLE IF EXISTS user_table;')

cursor.execute("""
    CREATE TABLE user_table (
        user_id numeric(10, 0) NOT NULL,
        name CHARACTER VARYING(50)COLLATE pg_catalog."default" NOT NULL,
        age NUMERIC(3,0) NOT NULL,
        phone CHARACTER VARYING(20) COLLATE pg_catalog."default",
        CONSTRAINT user_table_pkey PRIMARY KEY (user_id)
    );
""")

# --------------------------------------------------------------------------------------#
# Insert Records into the User Table
# --------------------------------------------------------------------------------------#
cursor.execute("""
    INSERT INTO user_table (user_id, name, age, phone) VALUES (3, 'Jenny', 34, NULL);
    INSERT INTO user_table (user_id, name, age, phone) VALUES (2, 'Tom', 29, '1-800-123-1234');
    INSERT INTO user_table (user_id, name, age, phone) VALUES (1, 'John', 28, NULL);
""")

# --------------------------------------------------------------------------------------#
# Fetch Records from User Table in JSON format
# --------------------------------------------------------------------------------------#
cursor.execute("SELECT * FROM user_table")

json_message = cursor.fetchall_json()

print(json_message)

connection.commit()

connection.close()

cursor.close()