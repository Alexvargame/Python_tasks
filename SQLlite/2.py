import sqlite3


try:
    sqlite_connection=sqlite3.connect('sqlite_python.db')
    sqlite_create_table_query='''CREATE TABLE sqlitedb_developers(
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email text NOT NULL UNIQUE,
                        joining_date datetime,
                        salary REAL NOT NULL);'''
    cursor=sqlite_connection.cursor()
    print("База подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")
    cursor.close()
except sqlite3.Error as error:
    print("Ошибка при подключении", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение SQLite с закрыто")
