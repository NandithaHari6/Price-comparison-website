import sqlite3
import requests
from bs4 import BeautifulSoup

conn=sqlite3.connect("product_sample.db")
c=conn.cursor()
# c.execute(""" create table product3(website text, url text, title text,price text) """)

with open('validproxy.txt', "r") as f:
    proxiesSet=f.read().split("\n")
 
count=0
def amazon_scrap_ac(url):
    global count
    
    while len(proxiesSet) > 0:
       
        try:
            r=requests.get(url,proxies={"http":proxiesSet[count],"https":proxiesSet[count]})
            print(r.status_code)
            
        except:
            continue
        finally:
            count=(count+1)%len(proxiesSet)
        if r.status_code==200:
            soup=BeautifulSoup(r.text,'lxml')
            products=soup.find_all('span',class_="a-declarative")
            for product in products:
                prod_title=product.find('span',class_="a-size-medium a-color-base a-text-normal")
                prod_link=product.find('a',class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
                prod_price=product.find('span',class_="a-price-whole")
               
                title= prod_title.text if prod_title is not None else "none"
                link= prod_link.get('href') if prod_link is not None else "none"
                
                price=(prod_price.text) if prod_price is not None else "0"
                
                if "none" not in title:
                    print(f"{title} {link} {price}")
                    c.execute("insert into product3 values(?,?,?,?)", ("Amazon",link,title,price))
                    
                    conn.commit()
            break

search=input("Enter the product to search for")
base_url="https://www.amazon.in"
amazon_scrap_ac(base_url+"/s?k="+search)
conn.close()
print("Completed successfully")