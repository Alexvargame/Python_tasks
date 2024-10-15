import sqlite3
import sys
import traceback
from peewee import *
from datetime import date
db=SqliteDatabase('people.db')
class Person(Model):
    name=CharField()
    birthday=DateField()
    is_relative=BooleanField()

    class Meta:
        database=db

class Pet(Model):
    owner=ForeignKeyField(Person, related_name='pets')
    name=CharField()
    animal_type=CharField()

    class Meta:
        database=db        
"""   
Person.create_table()
Pet.create_table()

uncle_bob=Person(name='Bob', birthday=date(1960,1,15), is_relative=True)

uncle_bob.save()
grandma=Person.create(name='Grandma', birthday=date(1935,3,1), is_relative=True)

herb=Person.create(name='Herb', birthday=date(1950,5,5), is_relative=False)

grandma.name='Grandma L'
grandma.save()

bob_kitty=Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido=Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens=Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr=Pet.create(owner=herb, name='Mittens J', animal_type='cat')
#herb_mittens.delete_instance()
"""
conn = sqlite3.connect('people.db')
cur=conn.cursor()
cur.execute("SELECT * FROM Person;")
print(cur.fetchall())

#sql_delete_query = """DELETE from Pet where id>4"""
#cur.execute(sql_delete_query)
#cur.execute("SELECT * FROM Person;")
#print(cur.fetchall())
cur.close





#herb_fido.owner=uncle_bob
#herb_fido.save()
#bob_fido=herb_fido
cur.execute("SELECT * FROM Pet;")
print(cur.fetchall())
cur.close
conn.commit()
for person in Person.select():
    print(person.name, person.pets.count(), 'pets')
    for pet in person.pets:
        print(' ', pet.name, pet.animal_type)
for pet in Pet.select().join(Person).where(Person.name=='Bob'):
    print(pet.name)

for person in Person.select().where(fn.Lower(fn.Substr(Person.name,1,1))=='h'):
    print(person.name)

