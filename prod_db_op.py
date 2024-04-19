import sqlite3


def insert_into_db(table,link,title,price,prod_company,image,processed_title):
    conn=sqlite3.connect("product_sample.db")
    c=conn.cursor()
#     listOfTables = c.execute(
# f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'""").fetchall()
#     print(listOfTables)
    # if len(listOfTables) == 0:
    #     c.execute(f""" create table {table}(website text, url text, title text,price text, company text, image text) """)
    print("Inserting table")
    c.execute(f"insert into {table} values(?,?,?,?,?,?,?)", (table,link,title,price,prod_company, image,processed_title))
    conn.commit()
    conn.close()
def select_titles(table):
    conn=sqlite3.connect("product_sample.db")
    c=conn.cursor()
    c.execute(f"select title from {table}")
   
    res=c.fetchall()
    print(res)
    conn.close()
    return res
    
select_titles("amazon")