import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("SENDER_EMAIL") 
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD") 


EMAIL_SUBJECT = "Exciting Opportunity for {company}"
EMAIL_BODY = """
Dear {name},

I hope this email finds you well. I'm reaching out because I believe our product/service could greatly benefit {company}.

[Your personalized message here]

I'd love to schedule a brief call to discuss how we can help {company} achieve its goals. Would you be available for a 15-minute chat next week?

Best regards,
Your Name
Your Company
"""

def send_email(recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to {recipient}")
        return True
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {str(e)}")
        return False

def read_contacts(file_path):
    contacts = []
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts.append(row)
        print(f"Loaded {len(contacts)} contacts from {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading contacts: {str(e)}")
    return contacts

def main():
    contacts = read_contacts('contacts.csv')
    
    if not contacts:
        print("No contacts found or file error.")
        return

    for contact in contacts:
        name = contact.get('name', 'there')  
        company = contact.get('company', 'your company') 
        
        if not email:
            print(f"Missing email for contact: {contact}")
            continue

        subject = EMAIL_SUBJECT.format(company=company)
        body = EMAIL_BODY.format(name=name, company=company)
        
        if send_email(email, subject, body):
            time.sleep(60)  
if __name__ == "__main__":
    main()
