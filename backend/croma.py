from bs4 import BeautifulSoup as bs
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import sqlite3
import requests
from name import getName 

def croma_scrap_ac(link):
    base_url='https://www.croma.com'
    url = base_url + link
    conn=sqlite3.connect("product_sample.db")
    c=conn.cursor()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.get(url)
    button = driver.find_element(By.CLASS_NAME,'btn btn-secondary btn-viewmore')
    button.click()
    time.sleep(2)
    soup=bs(driver.page_source,'html.parser')
    products=soup.find_all('li',class_="product-item")
    for product in products:
        # print(product.find('h3',class_="product-title plp-prod-title 999").a.text,end="\n\n")
        prod_title=product.find('h3',class_="product-title plp-prod-title 999").a
        prod_price=product.find('span',class_="amount plp-srp-new-amount")
                    
        prod_image = product.find('div',class_="product-img plp-card-thumbnail plpnewsearch").img
                    
        title= prod_title.text if prod_title is not None else "none"
                    
        link= prod_title.get('href') if prod_title is not None else "none"
                
        price=(prod_price.text) if prod_price is not None else "error"
        image=(prod_image.get('src')) if prod_image is not None else "error"
        if "none" not in title:
            processed_title = getName(title)
            prod_company = title.split(" ", 1)[0]
            c.execute(f"insert into croma values(?,?,?,?,?,?)", ("Croma",link,processed_title,price,prod_company, image))
            conn.commit()
    conn.close()
        
        