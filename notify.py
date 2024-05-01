import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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