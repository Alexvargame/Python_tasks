import sqlite3
import sys
import traceback
from peewee import *
from datetime import date
import pymysql

user='root'
password='root'
db_name='peewee_demo'

ddbhandle=MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
)
#dbhandle.connect()
dbhandle = SqliteDatabase('peewee_demo.db')

