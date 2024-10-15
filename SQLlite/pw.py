import sqlite3
import sys
import traceback
from peewee import *
from datetime import date

user='root'
password='root'
db_name='peewee_demo'

dbhandle=MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
    )
