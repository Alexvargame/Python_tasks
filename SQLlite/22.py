import sqlite3
import sys
import traceback

try:
    sqlite_connection=sqlite3.connect('sqlite_python.db')
    cursor=sqlite_connection.cursor()
    print("База подключена к SQLite")
    sqlite_insert_query="""INSERT INTO sqlitedb_developers
                (id, name, email, joining_date. salary)
                VALUES (4, 'Alex', 'sale@qmail.com','2020-11-20', 8600);"""
    
    cursor.execute(sqlite_insert_query)
    sql_update_query="""Update sqlitedb_developers set salary=10000 where id=4"""
    cursor.execute(sql_update_query)
    sql_delete_query = """DELETE from sqlitedb_developers where id = 4"""
    cursor.execute(sql_delete_query)
    
    sqlite_connection.commit()
    cursor.close()
except sqlite3.Error as error:
    print("Ошибка работы с SQLite:  ", error)
    exc_type, exc_value, exc_tb=sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sqlite_connection):
        print("Всего строкб измененных: ", sqlite_connection.total_changes)
        sqlite_connection.close()
        print("Соединение SQLite с закрыто")
