import requests
from bs4 import BeautifulSoup
from  prod_db_op import insert_into_db
from process_title import process_title
def amazon_scrap_ac(link,page):
    global count
    base_url="https://www.amazon.in"
    url = base_url + link
    headers = {
    'User-Agent': 'Mozilla/5.0 ',
        }  
    
    with open('validproxy.txt', "r") as f:
        proxiesSet=f.read().split("\n")[:50] 
    count=0
    while len(proxiesSet) > 0:
        try:
            # ,proxies={"http":proxiesSet[count],"https":proxiesSet[count]},timeout=3
            r=requests.get(url,headers=headers)
 
        except:
            continue
        finally:
            count=(count+1)%len(proxiesSet)
        if r.status_code==200:
            soup=BeautifulSoup(r.text,'lxml')
            products=soup.find_all('span',class_="a-declarative")
            next = soup.find('a', class_="s-pagination-item s-pagination-button")
            for product in products:
                prod_title=product.find('span',class_="a-size-medium a-color-base a-text-normal")
                prod_link=product.find('a',class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
                prod_price=product.find('span',class_="a-price-whole")
                prod_image = product.find('img',class_="s-image")

                title= prod_title.text if prod_title is not None else "none"
                link= prod_link.get('href') if prod_link is not None else "none"
                price=(prod_price.text) if prod_price is not None else "error"
                image=(prod_image.get('src')) if prod_image is not None else "error"
                if "none" not in title:
                    processed_title=process_title(title)
                    prod_company = title.split(" ", 1)[0]
                    insert_into_db("Amazon",base_url+link,title,price,prod_company, image,processed_title)
            break
    if page < 1:
        amazon_scrap_ac(next['href'], page+1)  