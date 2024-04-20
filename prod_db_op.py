import sqlite3


def insert_into_db(table,link,title,price,prod_company,image,processed_title):
    conn=sqlite3.connect("product_sample.db")
    c=conn.cursor()
    
    print("Inserting table")
    c.execute(f"insert into {table} values(?,?,?,?,?,?,?)", (table,link,title,price,prod_company, image,processed_title))
    conn.commit()
    conn.close()
def deleteTable():
    conn=sqlite3.connect("product_sample.db")
    c=conn.cursor()
    c.execute("Delete  from flipkart")
    c.execute("Delete  from croma")
    c.execute("Delete  from amazon")
    conn.close()
def create_grouping():
    conn=sqlite3.connect("product_sample.db")
    c=conn.cursor()
    c.execute("Drop  view if exists flipkart_set")
    c.execute("Drop view if exists amazon_set")
    c.execute("Drop view  if exists croma_set")
    c.execute("Drop table if exists grouping")
    c.execute("create view amazon_set as select url,price,image,title,short_title from amazon group by short_title ")
    c.execute("create view croma_set as select url,price,image,title,short_title from croma group by short_title ")
    c.execute("create view flipkart_set as select url,price,image,title,short_title from flipkart group by short_title ")
    c.execute(""" create table grouping as select  * from amazon_set left join flipkart_set on flipkart_set.short_title=amazon_set.short_title left join croma_set on croma_set.short_title=flipkart_set.short_title UNION  select  * from amazon_set right join flipkart_set on flipkart_set.short_title=amazon_set.short_title right join croma_set on croma_set.short_title=flipkart_set.short_title """)
#     c.execute("""create table grouping as SELECT *
# FROM amazon_set AS a
# LEFT OUTER JOIN flipkart_set AS f ON a.short_title = f.short_title
# LEFT OUTER JOIN croma_set AS c ON a.short_title = c.short_title
# UNION ALL
# SELECT *
# FROM flipkart_set AS f
# LEFT OUTER JOIN amazon_set AS a ON a.short_title = f.short_title
# LEFT OUTER JOIN croma_set AS c ON f.short_title = c.short_title
# WHERE a.short_title IS NULL
# UNION ALL
# SELECT *
# FROM croma_set AS c
# LEFT OUTER JOIN amazon_set AS a ON a.short_title = c.short_title
# LEFT OUTER JOIN flipkart_set AS f ON f.short_title = c.short_title
# WHERE a.short_title IS NULL AND f.short_title IS NULL;""")
    res=c.fetchall()
    conn.close()

    return res
create_grouping()