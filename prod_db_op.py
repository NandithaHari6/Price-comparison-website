import sqlite3
import os
absolute_path = os.path.abspath('product_sample.db')

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
    # c.execute("""( product_id INT AUTO_INCREMENT PRIMARY KEY, a_url,a_price,a_image,a_title,a_short,f_url,f_price,f_image,f_title,f_short,c_url,c_price,c_image,c_title,c_short)""")
    c.execute("""create table grouping1 as select * from amazon_set left join flipkart_set on flipkart_set.short_title=amazon_set.short_title left join croma_set on croma_set.short_title=flipkart_set.short_title UNION  select  * from amazon_set right join flipkart_set on flipkart_set.short_title=amazon_set.short_title right join croma_set on croma_set.short_title=flipkart_set.short_title  UNION  select  * from amazon_set right join flipkart_set on flipkart_set.short_title=amazon_set.short_title left join croma_set on croma_set.short_title=flipkart_set.short_title""")
    c.execute("""
    CREATE TABLE grouping (
        productId INTEGER PRIMARY KEY AUTOINCREMENT,
        a_url TEXT,
        a_price TEXT,
        a_image TEXT,
        a_title TEXT,
        a_short TEXT,
        f_url TEXT,
        f_price TEXT,
        f_image TEXT,
        f_title TEXT,
        f_short TEXT,
        c_url TEXT,
        c_price TEXT,
        c_image TEXT,
        c_title TEXT,
        c_short TEXT
    )
""")

# Insert data into the 'grouping' table by selecting from 'grouping1'
    c.execute("""
    INSERT INTO grouping (a_url, a_price, a_image, a_title, a_short,
                          f_url, f_price, f_image, f_title, f_short,
                          c_url, c_price, c_image, c_title, c_short)
    SELECT * FROM grouping1
""")
    # c.execute("""Create table grouping(productId int,a_url,a_price,a_image,a_title,a_short,f_url,f_price,f_image,f_title,f_short,c_url,c_price,c_image,c_title,c_short)""")
    # c.execute("""insert into grouping(a_url,a_price,a_image,a_title,a_short,f_url,f_price,f_image,f_title,f_short,c_url,c_price,c_image,c_title,c_short) select * from grouping1;""")
# FROM amazon_set AS a
# LEFT OUTER JOIN flipkart_set AS f ON a.short_title = f.short_title
# LEFT OUTER JOIN croma_set AS c ON a.short_title = c.short_title
# UNION 
# SELECT *
# FROM flipkart_set AS f
# LEFT OUTER JOIN amazon_set AS a ON a.short_title = f.short_title
# LEFT OUTER JOIN croma_set AS c ON f.short_title = c.short_title
# WHERE a.short_title IS NULL
# UNION 
# SELECT *
# FROM croma_set AS c
# LEFT OUTER JOIN amazon_set AS a ON a.short_title = c.short_title
# LEFT OUTER JOIN flipkart_set AS f ON f.short_title = c.short_title
# WHERE a.short_title IS NULL AND f.short_title IS NULL;""")
    res=c.fetchall()

    conn.close()

    return res
create_grouping()