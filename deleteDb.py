import sqlite3
conn=sqlite3.connect("product_sample.db")
c=conn.cursor()
c.execute("Drop table product3")
conn.commit()
c.close()