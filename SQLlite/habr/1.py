import sqlite3
conn=sqlite3.connect('Chinook_Sqlite.sqlite')
cursor=conn.cursor()
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
results=cursor.fetchall()
results2=cursor.fetchall()
print(results)
print(results2)
#cursor.execute("insert into Artist values(Null, 'A Aagrh')")
#conn.commit()
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
results=cursor.fetchall()
print(results)
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT ?", ('2'))
results=cursor.fetchall()
print(results)
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT :limit", {"limit":3})
results=cursor.fetchall()
print(results)
new_artists=[
    ('A Aagrh!',),
     ('A Aagrh!-2',),
     ('A Aagrh!-3',),
    ]
#cursor.executemany("insert into Artist values(Null,?)", new_artists)

for row in cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT :limit", {"limit":3}):
    print(row)
    
    

conn.close()
