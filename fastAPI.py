
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from amazon import amazon_scrap_ac
from flipkart_no_proxy import flipkart_scrap_ac
from croma import croma_scrap_ac
from prod_db_op import create_grouping,deleteTable
import sqlite3
import jwt
from datetime import datetime, timedelta
from userSignup import is_email_present,insertUser,loginAuth
app = FastAPI()

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
    deleteTable()
    amazon_scrap_ac("/s?k="+search)
    flipkart_scrap_ac("/search?q="+search)
    croma_scrap_ac("searchB?q="+search+"%3Arelevance&text="+search)

    create_grouping()
    conn=sqlite3.connect('product_sample.db')
    c=conn.cursor()
    
    
    c.execute("Select * from grouping1")
    row=c.fetchall()
    conn.commit()
    conn.close()
    return row


# Secret key for JWT token encoding (keep it secret in production)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time

@app.post("/login/")
async def login(user:LoginUser):
    
    
    if loginAuth(user.email,user.password)==0:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    # Generate JWT token
    access_token_expires = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token_payload = {"sub": user.email, "exp": access_token_expires}
    access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": access_token, "token_type": "bearer"}

    
