import logging

from peewee import *

conn=SqliteDatabase('Chinook_Sqlite.sqlite')
class BaseModel(Model):
    class Meta:
        database=conn
class Artist(BaseModel):
    artist_id=AutoField(column_name='ArtistId')
    name=TextField(column_name='Name', null=True)

    class Meta:
        table_name='Artist'
def print_last_five_artists():
    cur_query=Artist.select().limit(5).order_by(Artist.artist_id.desc())
    for item in cur_query.dicts().execute():
        print('artist:', item)
    print("*"*10)
def logg():
    logger=logging.getLogger('peewee')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
print_last_five_artists()
Artist.create(name='1-Qwerty')
artist=Artist(name='2-asdfg')
artist.save()
artist_data=[{'name':'3-qaswed'}, {'name':'4-yghrf'}]
Artist.insert_many(artist_data).execute()

print_last_five_artists()
artist=Artist(name='2-asdfg***')
artist.artist_id=300
artist.save()
query=Artist.update(name=Artist.name*2).where(Artist.artist_id>290)
logg()
query.execute()
artist=Artist.get(Artist.artist_id==277)
artist.delete_instance()
query=Artist.delete().where(Artist.artist_id>276)
query.execute()
print_last_five_artists()
cursor=conn.cursor()
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
print(cursor.fetchall())
conn.close()
