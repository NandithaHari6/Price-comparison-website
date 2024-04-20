import sqlite3


def insert_into_db(table,link,title,price,prod_company,image,processed_title):
    conn=sqlite3.connect("product_sample.db")
    c=conn.cursor()
#     
    print("Inserting table")
    c.execute(f"insert into {table} values(?,?,?,?,?,?,?)", (table,link,title,price,prod_company, image,processed_title))
    conn.commit()
    conn.close()
def select_titles(table):
    conn=sqlite3.connect("product_sample.db")
    c=conn.cursor()
    c.execute(f"select title from {table}")
   
    res=c.fetchall()
    
    conn.close()
    return res
def create_grouping():
    conn=sqlite3.connect("product_sample.db")
    c=conn.cursor()
    c.execute("Drop view flipkart_set")
    c.execute("Drop view amazon_set")
    c.execute("Drop view croma_set")
    c.execute("create view amazon_set as select title,short_title from amazon group by short_title ")
    c.execute("create view croma_set as select title,short_title from croma group by short_title ")
    c.execute("create view flipkart_set as select title,short_title from flipkart group by short_title ")
    c.execute(""" select  flipkart_set.title,amazon_set.title,croma_set.title,flipkart_set.short_title from amazon_set left join flipkart_set on flipkart_set.short_title=amazon_set.short_title left join croma_set on croma_set.short_title=flipkart_set.short_title UNION  select  flipkart_set.title,amazon_set.title,croma_set.title,flipkart_set.short_title from amazon_set right join flipkart_set on flipkart_set.short_title=amazon_set.short_title right join croma_set on croma_set.short_title=flipkart_set.short_title """)
    res=c.fetchall()
    print(res)
    conn.close()
    return res
create_grouping()