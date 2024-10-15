import sqlite3
conn = sqlite3.connect('peewee.db')
cur=conn.cursor()
cur.execute("""SELECT *, lastPrice, symbol FROM Coins where symbol='LUNAUSDT';""")
print(cur.fetchall())

