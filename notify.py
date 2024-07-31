import os
import sqlite3
from track import a_process_url,f_process_url
from trackCroma import c_process_url
def join_wishlist():
    conn=sqlite3.connect('./product_sample.db')
    c=conn.cursor()
    c.execute("Select * from users inner join WishlistEntry on users.email=wishlistEntry.email inner Join wishListProduct on wishListProduct.productId=wishListEntry.productId")
    
    rows=c.fetchall()
    mainlist=[]
    print(len(rows))
    
    for row in rows:
        
        (id,email,m1,phoneNo,name,m8,m2,target,m4,title,m5,a_link,m6,f_link,m7,c_link,c_price)=row
        target=int(target[:-2])
        # target=37000
        print(target)
        minprice=0
        maxdiff=0
        minlink=""
        if a_link:
            print(a_link)
            a_price=a_process_url(a_link)
            print("Amazon price is " ,a_price)
            if a_price<target and target-a_price>maxdiff:
                maxdiff=target-a_price
                minprice=a_price
                minlink=a_link
        if f_link:
            print(f_link)
            f_price=f_process_url(f_link)
            print("Flipkart Price" ,f_price)
            if f_price<target and target-f_price>maxdiff:
                maxdiff=target-f_price
                minprice=f_price
                minlink=f_link
        if c_link:
        
            c_price=c_process_url(c_link)
            print("Croma price",c_price)
            if c_price<target and target-c_price>maxdiff:
                maxdiff=target-c_price
                minprice=c_price
                minlink=c_link
        if minprice!=0:
            mainlist.append({"name":name,"email":email,"phoneNo":phoneNo,"target":target,"title":title,"minprice":minprice,"minlink":minlink})
    print(mainlist)

    conn.commit()
    conn.close()
    return mainlist


if __name__ == "__main__":
    join_wishlist()
# (1, 'nandithahari6@gmail.com', '$2b$12$bbZkiVCCGez2F.q8sy4YGe6NFLpk19/KtG.ceoGfbcAuzU49CoefO', 998765432, 'Nanditha', 'nandithahari6@gmail.com', 7, '12000.0', 7, 'SAMSUNG 223 L Direct Cool Single Door 3 Star Refrigerator with 
# Base Drawer  with Digital Inverter', 'https://rukminim2.flixcart.com/image/312/312/xif0q/refrigerator-new/i/r/k/-original-imagy3pyt5tfwbqu.jpeg?q=70', 'https://www.amazon.in/Samsung-Direct-Cool-Refrigerator-RR24C2723S8-NL/dp/B0BXDJX8NB', '17,790', 'https://www.flipkart.com/samsung-223-l-direct-cool-single-door-3-star-refrigerator-base-drawer-digital-inverter/p/itme034f49f773dd?pid=RFRGHJPXNGEUM66R&lid=LSTRFRGHJPXNGEUM66RO8D9SB&marketplace=FLIPKART&q=fridge&store=j9e%2Fabm%2Fhzg&srno=s_1_1&otracker=search&fm=organic&iid=en_2dUO0G1Vw2NxSvxeShu5IKYGhg0aoyoDqSt1nHF1FMYN1j3sHY1EMrz-C7XrmMEbeWwVpUiGb92stRZYEHxlyPUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=None&ppn=None&ssid=jx1tecm5z40000001714530565357&qH=2be977f3ff92dd10', '₹19,190', 'https://www.croma.com//samsung-223-litres-3-star-direct-cool-single-door-refrigerator-with-base-drawer-rr24c2z23cr-nl-camellia-purple-/p/269794', ' ₹19,190 ')