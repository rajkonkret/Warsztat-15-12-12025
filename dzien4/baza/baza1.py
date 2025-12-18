# baza danych - silnik bazy danych
# sql
# mysql, postgres, mssql, oracle

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_db.db')
    cursor = sql_connection.cursor()
    print("Baza została podłączona")
except sqlite3.Error as e:
    print("Bład podłaczennia bazy danych")
finally:
    if sql_connection:
        sql_connection.close()
# Baza została podłączona
#
# Process finished with exit code 0
