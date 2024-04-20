import sqlite3
conn=sqlite3.connect("product_sample.db")
c=conn.cursor()
# c.execute("Drop table product3")
# c.execute("Delete  from flipkart")
# c.execute("Delete  from croma")
# c.execute("Delete  from amazon")


# c.execute("Drop table flipkart")
# c.execute("Drop table amazon")
# c.execute("Drop table croma")
# c.execute(""" create table amazon(website text, url text, title text,price text, company text, image text,short_title text)""") 
# c.execute(""" create table flipkart(website text, url text, title text,price text, company text, image text,short_title text)""") 
# c.execute(""" create table croma(website text, url text, title text,price text, company text, image text,short_title text)""")
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
c.execute("Create table wishlist(user_email text, product_id number) ")

# res=c.fetchall()

# for row in res:
#     print(row,end="\n\n")

conn.commit()

c.close()