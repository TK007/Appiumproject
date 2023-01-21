import smtplib, ssl
import datetime as dt
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


msg = MIMEMultipart()
msg['From'] = "Tarunkaushik.prepladder@gmail.com"
msg['To'] = "Tarun.kaushik@prepladder.com"
msg['Subject'] = "Time email"

body = "Hi \nThis is my first email through python"

msg.attach(MIMEText(body, 'plain'))

context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#server.starttls(context=context)
server.login("Tarunkaushik.prepladder@gmail.com", "prepladder123")
send_time = dt.datetime(2021,12,1,11,34,45)
#print(send_time.timestamp())
#print(time.time())
x = time.sleep(send_time.timestamp() - time.time())
#print(x)
server.send_message(msg)

print('Email Sent')