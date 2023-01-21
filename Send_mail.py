import smtplib , ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import


msg = MIMEMultipart()
msg['From'] = "Tarunkaushik.prepladder@gmail.com"
msg['To'] = "Tarun.kaushik@prepladder.com"
msg['Subject'] = "Python is love"

body = "Body of the mail"

msg.attach(MIMEText(body, 'plain'))
filepath = r"C://Users//user//Desktop//Images//alphabets.png"
filename = "alphabets.png"
attachment = open(filepath, "rb")

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', 'attachment', filename = filename)
msg.attach(p)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("Tarunkaushik.prepladder@gmail.com", "prepladder123")
server.send_message(msg)
server.quit()

