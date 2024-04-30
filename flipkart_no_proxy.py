
import requests
from bs4 import BeautifulSoup
from  prod_db_op import insert_into_db
from process_title import process_title
def flipkart_scrap_ac(link):
    global count
    base_url="https://www.flipkart.com"
    url = base_url + link
    try:
            #proxies={"http":proxiesSet[count],"https":proxiesSet[count]},timeout=3
            r=requests.get(url)
            print(r.status_code)
    except:
            pass
       
    if r.status_code==200:
        soup=BeautifulSoup(r.text,'lxml')
        products=soup.find_all('div',class_="cPHDOP col-12-12")
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
                    processed_title=process_title(title)
                #     print(f"Flipkart {title}  {price} {processed_title}")
                    prod_company = title.split(" ", 1)[0]
                    new_url=base_url+link

                    #code to find model number of products
                    # try:
                    #     r2=requests.get(new_url)
                    #     soup2=BeautifulSoup(r2.text,'lxml')
                    #     rows=soup2.find('table',class_="_14cfVK").find_all('tr')
                    
                    #     model=rows[1].find('li',class_="_21lJbe")
                    #     print(f"Model No :  {model}")
                    # except:
                    #     print("Cannot find model")
                    #     pass    
            
        
        
        
                    insert_into_db("flipkart",base_url+link,title,price,prod_company, image,processed_title)
                        
                    
          
