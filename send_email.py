import smtplib
from email.mime.multipart import MIMEMultipart
from  email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")

reciever_email = os.getenv("RECEIVER_EMAIL")
ngrok_link = "https://service-starter-useable.ngrok-free.dev"

msg = MIMEMultipart()
msg['Subject'] = "Urgent: Unusual Activity Detected on Your Account"
msg['From'] = "CyberSecurity Bank Security Team <" + sender_email + ">"
msg['To'] = reciever_email


html_part = MIMEText(open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "email_template.html"), encoding="utf-8").read(), "html")

msg.attach(html_part)

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.ehlo()
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, reciever_email, msg.as_string())
    print("Email sent successfully!")