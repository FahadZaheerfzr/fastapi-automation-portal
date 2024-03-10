import pyodbc
import pandas as pd


def create_connection():
    username = "USERNAME"
    password = "PASSWORD"
    server = "HOST"
    database = "DB"

    connection_string = f"DRIVER={{SQL server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    sql_con = pyodbc.connect(connection_string)
    return sql_con


def query_user(query):
    try:
        conn = create_connection()
    except Exception as e:
        raise Exception(f'Error creating connection: {e}')

    try:
        result = pd.read_sql(query, conn)
        conn.close()
        return result
    except Exception as e:
        raise Exception(f'Error in fetching the data from the database {e}')


def insert_user(query):
    try:
        conn = create_connection()
        cursor = conn.cursor()
    except Exception as e:
        raise Exception(f'Error creating connection: {e}')

    try:
        cursor.execute(query)
        conn.commit()
        conn.close()
        return {'message': 'Record inserted successfully'}
    except Exception as e:
        raise Exception(f'Error in fetching the data from the database {e}')
