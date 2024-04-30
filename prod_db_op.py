import sqlite3
import os
absolute_path = os.path.abspath('product_sample.db')
print(absolute_path)
def insert_into_db(table,link,title,price,prod_company,image,processed_title):
    conn=sqlite3.connect(absolute_path)
    c=conn.cursor()
    
    print("Inserting table")
    c.execute(f"insert into {table} values(?,?,?,?,?,?,?)", (table,link,title,price,prod_company, image,processed_title))
    conn.commit()
    conn.close()
def deleteTable():
    conn=sqlite3.connect('product_sample.db')
    c=conn.cursor()
    c.execute("Delete from flipkart")
    c.execute("Delete from croma")
    c.execute("Delete from amazon")
    conn.commit()
    conn.close()
    return 1
def create_grouping():
    conn=sqlite3.connect('product_sample.db')
    c=conn.cursor()
    c.execute("Drop  table if exists flipkart_set")
    c.execute("Drop table if exists amazon_set")
    c.execute("Drop table  if exists croma_set")
    c.execute("Drop table if exists grouping")
    c.execute("Drop table if exists grouping1")
    c.execute("create table amazon_set as select url as a_url,price as a_price,image as a_image,title as a_title,short_title from amazon group by short_title ")
    c.execute("create table croma_set as select url as c_url,price as c_price,image as c_image,title as c_title,short_title from croma group by short_title ")
    c.execute("create table flipkart_set as select url as f_url,price as f_price,image as f_image,title as f_title,short_title from flipkart group by short_title ")

    c.execute("""create table grouping1 as select * from amazon_set left join flipkart_set on flipkart_set.short_title=amazon_set.short_title left join croma_set on croma_set.short_title=flipkart_set.short_title UNION  select  * from amazon_set right join flipkart_set on flipkart_set.short_title=amazon_set.short_title right join croma_set on croma_set.short_title=flipkart_set.short_title  UNION  select  * from amazon_set right join flipkart_set on flipkart_set.short_title=amazon_set.short_title left join croma_set on croma_set.short_title=flipkart_set.short_title""")
    c.execute("""
    CREATE TABLE grouping (
        productId INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        image TEXT,
        a_url TEXT,
        a_price TEXT,
        f_url TEXT,
        f_price TEXT,
        c_url TEXT,
        c_price TEXT
    )
""")
    c.execute("Select * from grouping1")
    rows=c.fetchall()
    for row in rows:
        if row[8]:
            title=row[8]
            image=row[7]
        elif row[13]:
            title=row[13]
            image=row[12]
        else:
            title=row[3]
            image=row[2]
        c.execute("""insert into grouping(title ,
        image ,
        a_url ,
        a_price ,
        f_url ,
        f_price,
        c_url ,
        c_price ) values(?,?,?,?,?,?,?,?)""",(title,image,row[0],row[1],row[5],row[6],row[10],row[11]))
        conn.commit()



    res=c.fetchall()
    conn.commit()
    conn.close()

    return res
create_grouping()