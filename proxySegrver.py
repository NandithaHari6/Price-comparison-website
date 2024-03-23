import requests
import queue
import threading
q=queue.Queue()
valid=[]
file2=open("validproxy.txt","w")
with open('proxylist.txt') as f: 
   
    r=f.read().split("\n")
    for ele in r:
        q.put(ele)
def valid_check():
    
    global q,file2
    while not q.empty():
        proxy=q.get()
        try:
            
            r=requests.get("http://ipinfo.io/json",proxies={"http":proxy,"https":proxy})
        except:
            
            continue
        if r.status_code == 200:
            file2.write(f"{proxy}\n")
        
for _ in range(10):
    threading.Thread(target=valid_check).start()
if q.empty():
    file2.close()