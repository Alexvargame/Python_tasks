from peewee import *
from pw import *
from datetime import *
import pymysql


class BaseModel(Model):
    class Meta:
         database = dbhandle
class Category(BaseModel):
    id = PrimaryKeyField(null=False)
    name=CharField(max_length=100)
    created_at=DateTimeField(default=datetime.now())
    updated_at=DateTimeField(default=datetime.now())

    class Meta:
        db_table="categories"
        order_by=('created_at')
class Product(BaseModel):
    id = PrimaryKeyField(null=False)
    name=CharField(max_length=100)
    price = FloatField(default=None)
    category=ForeignKeyField(Category, related_name='fk_cat_prod', to_field='id',on_delete='cascade', on_update='cascade')
    created_at=DateTimeField(default=datetime.now())
    updated_at=DateTimeField(default=datetime.now())

    class Meta:
        db_table="products"
        order_by=('created_at',)
