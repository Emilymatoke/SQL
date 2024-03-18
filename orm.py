''' ORM
-A technique that allows interaction of relational database using OOP.
- Allows us to work with DB entities as objects.
-simplifies DB operations and make code more readable.
'''
import sqlite3
'''I want a producys table
-name
-price



tables === classes
columns === attributes
table rows === instances
'''


class Product :
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor

    def __init__(self, id, name, price) :
        self.id = id
        self.name = name
        self.price = price

# create several methods that relate to class
    def save(self) :
         Product.cursor.execute('INSERT INTO products(id, name, price) VALUES(?,?,?)'(self.id,self.name,self.price))
         Product.conn.commit()
         Product.conn.close()


#creating the products table
    def create_table() :
        conn = sqlite3.connect('produts.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, name TEXT, price INTEGER)
''')
        conn.commit()
        conn.close()


    create_table()
    #create the objects
    new_product= (1, 'Laptop',999)

    #call methods from my class
    new_product.save()



        
        