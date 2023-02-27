"""SMTP mail sender."""
import getpass
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = getpass.getpass("Enter your mail : ")
password = getpass.getpass("Enter your password : ")
toemail = input("Enter your mail : ")
context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.login(email, password)

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = toemail
    msg["Subject"] = "Keylogger"
    BODY = "şğüçö"
    msg.attach(MIMEText(BODY, "plain", "utf-8"))

    part = MIMEBase("application", "octet-stream")
    FILENAME = "face.jpg"
    attachment = open(FILENAME, "rb")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename=" + FILENAME)
    msg.attach(part)

    # msg = "Subject: " + subject + "\n" + body
    smtp.sendmail(email, email, msg=msg.as_string())
