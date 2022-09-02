import sqlite3
from sqlite3 import Error


def create_connection(path: str):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f'SQlite connection error {e}')
    return connection


def execute_query(connection, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f'SQlite connection {e}')


def select_query(connection, query: str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'Sqlite connection error {e}')
