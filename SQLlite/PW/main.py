import peewee
from models import *

               
def add_category(name):
    row=Category(
        name=name.lower().strip(),
        )
    row.save()

   
def add_product(name, price, category_name):
    cat_exist = True
    
    try:
        category = Category.select().where(Category.name == category_name.lower().strip()).get()
    except DoesNotExist as de:
        cat_exist = False
 
    if cat_exist:
        row = Product(
            name=name.lower().strip(),
            price=price,
            category=category
        )
        row.save()
def find_product(name):
    return Product.get(Product.name == name.lower().strip())

def update_category(id, new_name):
    category = Category.get(Category.id == id)
    category.name = new_name
    category.save()

def delete_category(name):
    category = Category.get(Category.name == name.lower().strip())
    category.delete_instance()
if __name__ == '__main__':
    # Создаем разделы.
    add_category('Books')
    add_category('Electronic Appliances')
    
     #Добавляем продукты в разделы.
    add_product('C++ Premier', 24.5, 'books')
    add_product('Juicer', 224.25, 'Electronic Appliances')
