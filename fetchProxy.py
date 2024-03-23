from bs4 import BeautifulSoup as bs
import requests as r

res=r.get("https://free-proxy-list.net/")
soup=bs(res.text,'lxml')
f=open("proxylist.txt","w")
rows=soup.find('table',class_='table table-striped table-bordered').find_all('tr')
for row in rows[2:]:
    tds=row.find_all('td')
    ip=tds[0].text.strip()
    port=tds[1].text.strip()
    f.write(f"{str(ip)}:{str(port)}\n")
f.close()    