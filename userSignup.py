import sqlite3
import bcrypt
from fastapi import Depends, FastAPI, HTTPException
from datetime import datetime, timedelta

from pydantic import BaseModel
def is_email_present(email):
    conn = sqlite3.connect('product_sample.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email=?', (email,))
    rows = cursor.fetchall()
    conn.close()
    return len(rows) > 0
def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def insertUser(email,password,phoneNo,name):
    conn = sqlite3.connect('product_sample.db')
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    password = hashed_password   
    cursor.execute('Insert into Users(email,password,phoneNo,name) values(?,?,?,?)', (email,password,phoneNo,name))
    conn.commit()
    conn.close()
    return cursor.lastrowid

