
from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
from typing import Optional
from amazon import amazon_scrap_ac
from flipkart_no_proxy import flipkart_scrap_ac
from croma import croma_scrap_ac
from prod_db_op import create_grouping,deleteTable
import sqlite3
import jwt
from datetime import datetime, timedelta
from userSignup import is_email_present,insertUser
from login import create_access_token,login_auth,is_authenticated
from addToWishlist import create_connection,create_product_table,create_wishlist_table
from fastapi.middleware.cors import CORSMiddleware
import json
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class LoginUser(BaseModel):
    email: str
    password: str
class User(BaseModel):
    name:str
    phoneNo:int
    email: str
    password: str
class Search(BaseModel):
    searchWord:str
class Wishlist(BaseModel):
    productId:int
    targetPrice:float
   
users_db = {}
@app.post("/signup/")
async def signup(user: User):
    if is_email_present(user.email) :
        raise HTTPException(status_code=400, detail="Username already registered")
    else:
       user_id= insertUser(user.email,user.password,user.phoneNo,user.name)
    
    return {"message": "User created successfully with id   ","user_id":user_id}

@app.post("/search/")
def scrap_websites(req:Search):
    search=req.searchWord
    # deleteTable()
    # amazon_scrap_ac("/s?k="+search)
    # flipkart_scrap_ac("/search?q="+search)
    # croma_scrap_ac("searchB?q="+search+"%3Arelevance&text="+search)
    # create_grouping()
    conn=sqlite3.connect('product_sample.db')
    c=conn.cursor()
    c.execute("Select * from grouping")
    rows=c.fetchall()
    formatted_data = []
    for row in rows:
        dict={'productId':row[0],
              'title':row[1],
              'image':row[2],
              'a_link':row[3],
              'a_price':row[4],
              'f_link':row[5],
              'f_price':row[6],
              'c_link':row[7],
              'c_price':row[8]
              }
        
        formatted_data.append(dict)
    conn.commit()
    conn.close()
    
    return formatted_data

@app.post("/login/")
async def login(user:LoginUser):
    if not login_auth(user.email, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token({"email": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/add_to_wishlist/")
async def add_to_wishlist(wish:Wishlist,email: str = Depends(is_authenticated)):
    conn = create_connection()
    create_product_table(conn)
    create_wishlist_table(conn)  
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grouping WHERE productId=?',[wish.productId])
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Product not found")
    print(row)

    
    cursor.execute("""insert into WishlistProduct(title ,
        image ,
        a_url ,
        a_price ,
        f_url ,
        f_price,
        c_url ,
        c_price ) values(?,?,?,?,?,?,?,?)""",(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    product_id = cursor.lastrowid
    conn.commit()
    cursor.execute('''
        INSERT INTO WishlistEntry (email, productId, targetPrice)
        VALUES (?, ?, ?)
    ''', (email, product_id, wish.targetPrice))
    conn.commit()
    conn.close()
    return {"message": "Added to WishList"}

    
@app.get('/show_wishlist')
async def show_wishlist(email: str = Depends(is_authenticated)):
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM WishlistProduct where productId in (Select productId from WishlistEntry where email=?)",[email])
    rows=c.fetchall()
    formatted_data = []
    for row in rows:
        dict={'productId':row[0],
              'title':row[1],
              'image':row[2],
              'a_link':row[3],
              'a_price':row[4],
              'f_link':row[5],
              'f_price':row[6],
              'c_link':row[7],
              'c_price':row[8]
              }
        c.execute("Select targetPrice from WishlistEntry where email=? and productId=?",[email,row[0]])
        res=c.fetchone()
        dict.update({'targetPrice':float(res[0])})
        formatted_data.append(dict)
    
        
    conn.commit()
    conn.close()
    return formatted_data
