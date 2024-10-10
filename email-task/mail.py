import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_mail(recv_addr: str, subject: str, body: str) -> None:
    print(f"[-] sending email to '{recv_addr}'")

    EMAIL = os.environ.get('EMAIL_ADDRESS')
    KEY = os.environ.get('EMAIL_KEY')

    if not EMAIL or not KEY:
        raise ValueError("EMAIL_ADDRESS and EMAIL_KEY environment variables are required")

    msg = MIMEMultipart()
    msg["To"] = recv_addr
    msg["From"] = EMAIL
    msg["Subject"] = subject
    body_text = body
    body_part = MIMEText(body_text, 'plain')
    msg.attach(body_part)

    smtp_obj = smtplib.SMTP(host="smtp.gmail.com", port=587)

    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.ehlo()
    smtp_obj.login(EMAIL, KEY)

    mail = smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())

    print(f"[-] email sent to '{recv_addr}'")

