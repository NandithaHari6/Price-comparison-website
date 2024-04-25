import sqlite3
conn=sqlite3.connect("product_sample.db")
c=conn.cursor()
comm = "DELETE FROM Amazon WHERE website = 'Amazon' "
c.execute(comm)
comm = "DELETE FROM Flipkart WHERE website = 'Flipkart' "
c.execute(comm)
comm = "DELETE FROM Croma WHERE website = 'Croma' "
c.execute(comm)
conn.commit()
c.close()