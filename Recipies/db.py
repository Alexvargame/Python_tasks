import sqlite3

stocks = [
 ('GOOG', 100, 490.1),
 ('AAPL', 50, 545.75),
 ('FB', 150, 7.45),
 ('HPQ', 75, 33.2),
]

db=sqlite3.connect('database.db')
cur=db.cursor()
#cur.execute('create table portfolio (symbol text,shares integer, price real)')
#db.commit()
cur.executemany('insert into portfolio values(?,?,?)',stocks)
db.commit()
