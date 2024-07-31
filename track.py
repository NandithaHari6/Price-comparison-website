import requests
from bs4 import BeautifulSoup

def a_process_url(url):
    formatted_price=0
    headers = {
    'User-Agent': 'Mozilla/5.0 ',
        }  
    try:
        response = requests.get(url,headers=headers)
        
        while response.status_code != 200:
            response = requests.get(url,headers=headers)

        soup = BeautifulSoup(response.content, 'lxml')
       
        price=soup.find('span',class_="a-price-whole")
        formatted_price=price.text.replace(",","").strip(".")
        
        
       
    except Exception as e:
        print("An error occurred:", e)
    return int(formatted_price)
def f_process_url(url):
    price=0
    try:
        response = requests.get(url)
        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'lxml')
            ele=soup.find('div',class_="Nx9bqj CxhGGd")
            if ele!=None:
                price=ele.text.replace(",","")[1:].strip()
            
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)
    return int(price)