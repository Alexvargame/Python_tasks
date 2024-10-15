import peewee
from models import *

if __name__=='__main__':
    try:
        dbhandle.connect()
        Category.create_table()
    except peewee.InternalError as px:
        print(str(px))
    try:
        
        Product.create_table()
    except peewee.InternalError as px:
        print(str(px))                             


    
