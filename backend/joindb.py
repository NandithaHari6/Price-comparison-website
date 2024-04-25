
import sqlite3

conn=sqlite3.connect("product_sample.db")
c=conn.cursor()
comm = """
CREATE TABLE IF NOT EXISTS merged_table AS
SELECT *
FROM amazon
LEFT JOIN flipkart ON amazon.title = flipkart.title
LEFT JOIN croma ON amazon.title = croma.title

UNION

SELECT *
FROM amazon
RIGHT JOIN flipkart ON amazon.title = flipkart.title
RIGHT JOIN croma ON amazon.title = croma.title
WHERE amazon.title IS NULL

UNION

SELECT *
FROM amazon
RIGHT JOIN flipkart ON amazon.title = flipkart.title
RIGHT JOIN croma ON flipkart.title = croma.title
WHERE amazon.title IS NULL AND flipkart.title IS NULL
"""
c.execute(comm)
results = c.fetchall()

# Print or process the results
for row in results:
    print(row)
conn.commit()
c.close()