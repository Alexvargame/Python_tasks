import peewee
from models import *
 
 
def find_all_categories():
    return Category.select()
 
def find_all_products():
    return Product.select()
products = find_all_products()
product_data = []
for product in products:
    product_data.append({
        'title': product.name,
        'price': product.price,
        'category': product.category.name
    })
 
print(product_data)
