from twilio.rest import Client
from notify import join_wishlist
import os
client=Client(os.getenv("secret_key"))
dropList=join_wishlist()
for priceDrop in dropList:
    to=f"whatsapp:+91{priceDrop['phoneNo']}"
    from_=f"whatsapp:+91{os.getenv("phone_number")}"
    body=f"Dear {priceDrop['name']},\n Price of {priceDrop['title']} is mow {priceDrop['minprice']}. Check out the product at {priceDrop['minlink']}. Your target price was {priceDrop['target']}.Thanks for shopping with Shofy."
    message=client.messages.create(to=to,from_=from_,body=body)
