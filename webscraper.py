import sqlite3
import requests
from bs4 import BeautifulSoup
import os
from amazon import amazon_scrap_ac
from flipkart import flipkart_scrap_ac


def execute_python_file(file_path):
   try:
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")


execute_python_file("fetchProxy.py")
print("Execution of fetch complete")
execute_python_file("proxyServer.py")
print("Execution of ProxyServer complete")
search=input("Enter the product to search for  :  ")
# amazon_scrap_ac("/s?k="+search)
flipkart_scrap_ac("/search?q="+search)
print("Completed successfully")