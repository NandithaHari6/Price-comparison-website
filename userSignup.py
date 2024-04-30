import sqlite3
import bcrypt

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
# def loginAuth(email,password):
#     conn = sqlite3.connect('product_sample.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT password FROM users WHERE email=?', (email,))   
#     stored_hashed_password = cursor.fetchone()
#     if stored_hashed_password is None or not bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password[0].encode('utf-8')):
#         return 0
#     conn.close()
#     return 1 
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=401,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     return email

# def is_authenticated(email: str = Depends(get_current_user)):
#     return True