from bs4 import BeautifulSoup as bs
from selenium import webdriver

def c_process_url(url):
    price=""
    options = webdriver.ChromeOptions()
    

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.get(url)
   
    soup=bs(driver.page_source,'html.parser')
    ele=soup.find('span',class_="amount")
    if ele!=None:
        price=ele.text
        print(price)
    return price