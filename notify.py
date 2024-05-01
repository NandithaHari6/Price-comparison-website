import os
import sqlite3
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from track import a_process_url,f_process_url
from trackCroma import c_process_url
def join_wishlist():
    conn=sqlite3.connect('./product_sample.db')
    c=conn.cursor()
    c.execute("Select * from users inner join WishlistEntry on users.email=wishlistEntry.email inner Join wishListProduct on wishListProduct.productId=wishListEntry.productId")
    
    rows=c.fetchall()
    for row in rows:
        a_new=f_new=c_new=999999999
        targetPrice=row[7]
        title=row[9]
        a_link=row[11]
        a_price=row[12]
        if  a_link!= None :
            a_new=a_process_url(a_link)
            if a_new<a_price :
                print("Price dropped ")
        f_link=row[13]
        f_price=row[14]
        if f_process_url!=None :
            f_new=f_process_url(f_link)
            if float(f_new[1:])<float(f_price[1:]) :
                print("Price dropped ")
        c_price=row[16]
        c_link=row[15]
        if c_link!=None :
            c_new=c_process_url(c_link)
            if float(c_new[1:])<float(c_price[1:]) :
                print("Price dropped ")
            
        
        

        
    conn.commit()
    conn.close()
def send_email(to_email, subject, body):
    # Replace 'YOUR_SENDGRID_API_KEY' with your actual API key
    api_key = 'ade0066c924816b2ad6b946a96f53fbd'
    sg = SendGridAPIClient(api_key)
    
    from_email = "nandithahari6@gmail.com"  # Change this to your email address
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        plain_text_content=body
    )
    try:
        response = sg.send(message)
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

# Example usage:
to_email = "hahahari@yahoo.com"
subject = "Test Email"
body = "Hello, this is a test email sent using Twilio SendGrid!"
send_email(to_email, subject, body)
join_wishlist()
# (1, 'nandithahari6@gmail.com', '$2b$12$bbZkiVCCGez2F.q8sy4YGe6NFLpk19/KtG.ceoGfbcAuzU49CoefO', 998765432, 'Nanditha', 'nandithahari6@gmail.com', 7, '12000.0', 7, 'SAMSUNG 223 L Direct Cool Single Door 3 Star Refrigerator with 
# Base Drawer  with Digital Inverter', 'https://rukminim2.flixcart.com/image/312/312/xif0q/refrigerator-new/i/r/k/-original-imagy3pyt5tfwbqu.jpeg?q=70', 'https://www.amazon.in/Samsung-Direct-Cool-Refrigerator-RR24C2723S8-NL/dp/B0BXDJX8NB', '17,790', 'https://www.flipkart.com/samsung-223-l-direct-cool-single-door-3-star-refrigerator-base-drawer-digital-inverter/p/itme034f49f773dd?pid=RFRGHJPXNGEUM66R&lid=LSTRFRGHJPXNGEUM66RO8D9SB&marketplace=FLIPKART&q=fridge&store=j9e%2Fabm%2Fhzg&srno=s_1_1&otracker=search&fm=organic&iid=en_2dUO0G1Vw2NxSvxeShu5IKYGhg0aoyoDqSt1nHF1FMYN1j3sHY1EMrz-C7XrmMEbeWwVpUiGb92stRZYEHxlyPUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=None&ppn=None&ssid=jx1tecm5z40000001714530565357&qH=2be977f3ff92dd10', '₹19,190', 'https://www.croma.com//samsung-223-litres-3-star-direct-cool-single-door-refrigerator-with-base-drawer-rr24c2z23cr-nl-camellia-purple-/p/269794', ' ₹19,190 ')