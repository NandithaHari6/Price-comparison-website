import sqlite3
import requests
from bs4 import BeautifulSoup

def flipkart_scrap_ac(link, page):
    global count
    base_url="https://www.flipkart.com"
    url = base_url + link
    conn=sqlite3.connect("product_sample.db")
    c=conn.cursor()
    #c.execute(""" create table flipkart(website text, url text, title text,price text, company text, image text) """)
    with open('validproxy.txt', "r") as f:
        proxiesSet=f.read().split("\n") 
    count=0
    while len(proxiesSet) > 0:
       
        try:
            r=requests.get(url,proxies={"http":proxiesSet[count],"https":proxiesSet[count]},timeout=3)
            print(r.status_code)
            
        except:
            continue
        finally:
            count=(count+1)%len(proxiesSet)
        if r.status_code==200:
            soup=BeautifulSoup(r.text,'lxml')
            products=soup.find_all('div',class_="cPHDOP col-12-12")
            next = soup.find('a', class_="cn++Ap")
            for product in products:
                prod_title=product.find('div',class_="KzDlHZ")
                prod_link=product.find('a',class_="CGtC98")
                prod_price=product.find('div',class_="Nx9bqj _4b5DiR")
                
                prod_image = product.find('img',class_="DByuf4")
                
                title= prod_title.text if prod_title is not None else "none"
                
                link= prod_link.get('href') if prod_link is not None else "none"
                
                price=(prod_price.text) if prod_price is not None else "error"
                image=(prod_image.get('src')) if prod_image is not None else "error"
                if "none" not in title:
                    prod_company = title.split(" ", 1)[0]
                    c.execute("insert into flipkart values(?,?,?,?,?,?)", ("Flipkart",link,title,price,prod_company, image))
                    
                    conn.commit()
                    
            break
    conn.close()
    if page < 1:
        flipkart_scrap_ac(next['href'], page+1)
    