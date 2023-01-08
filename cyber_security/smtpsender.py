"""SMTP mail sender."""
import getpass
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = getpass.getpass("Enter your mail : ")
password = getpass.getpass("Enter your password : ")
context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.login(email, password)

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = email
    msg["Subject"] = "Keylogger"
    body = "şğüçö"
    msg.attach(MIMEText(body, "plain", "utf-8"))

    # msg = "Subject: " + subject + "\n" + body
    smtp.sendmail(email, email, msg=msg.as_string())
