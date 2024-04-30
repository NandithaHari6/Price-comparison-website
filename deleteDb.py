import sqlite3
conn=sqlite3.connect("product_sample.db")
c=conn.cursor()
# # c.execute("Drop table product3")
# c.execute("Delete from flipkart")
# c.execute("Delete from Croma")
# c.execute("Delete from Amazon")
# c.execute("Drop table users")
# # c.execute("Drop table if exists ")
# c.execute("Drop table if exists WishlistEntry")
# c.execute("Drop table if exists WishlistProduct")
# c.execute("Create table users(id int auto_increment primary key, email text,password text,phoneNo int,name text)")
# c.execute("""Create table grouping(productId int,a_url,a_price,a_image,a_title,a_short,f_url,f_price,f_image,f_title,f_short,c_url,c_price,c_image,c_title,c_short)""")
# c.execute("Select * from grouping1")
# res=c.fetchall()
# for r in res:
#     print(r[0])
#     c.execute("""insert into grouping(a_url) values(?)""",r[0])
#     c.execute("""insert into grouping(a_url,a_price,a_image,a_title,a_short,f_url,f_price,f_image,f_title,f_short,c_url,c_price,c_image,c_title,c_short) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?  )""",r)
# # c.execute("Drop view amazon_set")
# c.execute("Drop view flipkart_set")
# c.execute("Drop view croma_set")
# c.execute("Drop table flipkart")
# c.execute("Drop table amazon")
# c.execute("Drop table croma")
c.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT,
    phoneNo INTEGER,
    name TEXT
)""")
c.execute(""" create table if not exists amazon(website text, url text, title text,price text, company text, image text,short_title text)""") 
c.execute(""" create table if not exists flipkart(website text, url text, title text,price text, company text, image text,short_title text)""") 
c.execute(""" create table if not exists croma(website text, url text, title text,price text, company text, image text,short_title text)""")
# c.execute("create view amazon_set as select title,short_title from amazon group by short_title ")
# c.execute("create view croma_set as select title,short_title from croma group by short_title ")
# c.execute("create view flipkart_set as select title,short_title from flipkart group by short_title ")
# c.execute(""" select  amazon_set.title,flipkart_set.title from amazon_set inner join flipkart_set on flipkart_set.short_title=amazon_set.short_title""")
# c.execute(""" select  amazon.title,flipkart.title from amazon inner join flipkart on flipkart.short_title=amazon.short_title""")
# c.execute(""" select title,short_title from amazon_set except
#           select  amazon_set.title,amazon_set.short_title from amazon_set inner join flipkart_set on flipkart_set.short_title=amazon_set.short_title""")
# c.execute("""select title,short_title from flipkart_set except
#       select  flipkart_set.title,flipkart_set.short_title from amazon_set inner join flipkart_set on flipkart_set.short_title=amazon_set.short_title""")
# c.execute("""select  flipkart_set.title,amazon_set.title,croma_set.title,flipkart_set.short_title from amazon_set inner join flipkart_set on flipkart_set.short_title=amazon_set.short_title inner join croma_set on croma.short_title=flipkart.title""")

# full join to get all matching products together

# c.execute(""" select  flipkart_set.title,amazon_set.title,croma_set.title,flipkart_set.short_title from amazon_set left join flipkart_set on flipkart_set.short_title=amazon_set.short_title left join croma_set on croma_set.short_title=flipkart_set.short_title UNION  select  flipkart_set.title,amazon_set.title,croma_set.title,flipkart_set.short_title from amazon_set right join flipkart_set on flipkart_set.short_title=amazon_set.short_title right join croma_set on croma_set.short_title=flipkart_set.short_title """)
# c.execute("Create table wishlist(user_email text, product_id number) ")

# res=c.fetchall()

# for row in res:
#     print(row,end="\n\n")

conn.commit()

c.close()