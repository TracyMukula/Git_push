
import sqlite3
from sqlite3 import Error
def create_connection(OCCUPATIONS):
    conn = None
    try:
        conn = sqlite3.connect('OCCUPATIONS.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
if __name__ == '__main__':
    create_connection(r"C:\sqlite\db\OCCUPATIONS.db")

    connection = create_connection.connect()
