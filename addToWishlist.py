import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

DATABASE_PATH = "product_sample.db"
class Wishlist(BaseModel):
    productId:int
    targetPrice:float
# Create a database connection
def create_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

# Function to create WishlistProduct table
def create_product_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WishlistProduct (
            productId INTEGER PRIMARY KEY,
            title TEXT,
        image TEXT,
        a_url TEXT,
        a_price TEXT,
        f_url TEXT,
        f_price TEXT,
        c_url TEXT,
        c_price TEXT
        )
    ''')
    conn.commit()

# Function to create WishlistEntry table
def create_wishlist_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WishlistEntry (
            email TEXT,
            productId INTEGER,
            targetPrice text,
            FOREIGN KEY (productId) REFERENCES WishlistProduct(productId)
        )
    ''')
    conn.commit()

# Function to add a product to the wishlist
# @app.post("/add_to_wishlist/")
# async def add_to_wishlist(wish:WishList):
#     conn = create_connection()
#     create_product_table(conn)
#     create_wishlist_table(conn)  
    
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM grouping WHERE productId=?',[wish.productId])
#     row = cursor.fetchone()
#     if not row:
#         raise HTTPException(status_code=404, detail="Product not found")
#     print(row)
#     title = row[0]  # Assuming title is the second column in grouping1 table
#     image = row[1]  # Assuming image is the third column in grouping1 table
    
#     cursor.execute("""insert into WishlistProduct(title ,
#         image ,
#         a_url ,
#         a_price ,
#         f_url ,
#         f_price,
#         c_url ,
#         c_price ) values(?,?,?,?,?,?,?,?)""",(title,image,row[2],row[3],row[4],row[5],row[6],row[7]))
#     product_id = cursor.lastrowid
#     conn.commit()
#     cursor.execute('''
#         INSERT INTO WishlistEntry (email, productId, targetPrice)
#         VALUES (?, ?, ?)
#     ''', (wish.email, product_id, wish.targetPrice))
#     conn.commit()
#     conn.close()

#     return {"message": "Added to WishList"}


