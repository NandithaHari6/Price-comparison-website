
from bs4 import BeautifulSoup
import os
from amazon import amazon_scrap_ac
from flipkart_no_proxy import flipkart_scrap_ac
from croma import croma_scrap_ac
import sys
from prod_db_op import create_grouping,deleteTable
# Access command line arguments
args=sys.argv[1:]

search=""
for i in args:
   search=search+i+"+"

def execute_python_file(file_path):
   try:
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")


execute_python_file("fetchProxy.py")
# print("Execution of fetch complete")
execute_python_file("proxyServer.py")
# print("Execution of ProxyServer complete")
deleteTable()
amazon_scrap_ac("/s?k="+search)
flipkart_scrap_ac("/search?q="+search)

croma_scrap_ac("searchB?q="+search+"%3Arelevance&text="+search)
# print("Completed successfully")
create_grouping()