import requests
from bs4 import BeautifulSoup

def a_process_url(url):
    price=""
    try:
        response = requests.get(url)
        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'html.parser')
            price=soup.find('span',class_="a-price-whole").text
            print(price)
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)
    return price
def f_process_url(url):
    price=""
    try:
        response = requests.get(url)
        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'html.parser')
            ele=soup.find('div',class_="Nx9bqj CxhGGd")
            if ele!=None:
                price=ele.text
            print(price)
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)
    return price