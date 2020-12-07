import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

server.login('email@email.com', 'password') #change to your email and password

msg = MIMEMultipart()
msg['From'] = 'Null'
msg['To'] = 'email2@email2.com'
msg['Subject'] = 'message'

with open ('message.text', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'water.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attatchment; filename-{filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('email@email.com', 'email2@email2.com', text)