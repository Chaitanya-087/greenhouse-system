import smtplib
from email.message import EmailMessage

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

sender_mail = "greenhousemail87@gmail.com"
pwd = "wcjgcfiuwmdhjuuo"


def send_mail(receiver_mail, subject, body):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_mail
        msg['To'] = receiver_mail
        msg.set_content(body)
        with smtplib.SMTP(EMAIL_SERVER, PORT) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(sender_mail, pwd)
            smtp.send_message(msg)
    except RuntimeError:
        pass

    finally:
        print("mail sent to user...")

