from fastapi import Depends, FastAPI, HTTPException
from datetime import datetime, timedelta
import jwt
from pydantic import BaseModel
import sqlite3
import bcrypt
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    access_token_expires = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token_payload = {"sub": data["email"], "exp": access_token_expires}
    access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    return access_token

def login_auth(email, password):
    conn = sqlite3.connect('product_sample.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE email=?', (email,))
    stored_hashed_password = cursor.fetchone()
    if stored_hashed_password is None or not bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password[0].encode('utf-8')):
        return False
    conn.close()
    return True

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except :
        raise credentials_exception
    return email

def is_authenticated(email: str = Depends(get_current_user)):
    return email
