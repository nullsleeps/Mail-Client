import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  
server.ehlo()

server.login('email@email.com', 'password')

msg = MIMEMultipart()
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'recipient_email@gmail.com'
msg['Subject'] = 'message'

with open('message.text', 'r') as f:
    message = f.read()
msg.attach(MIMEText(message, 'plain'))

filename = 'water.jpg'
with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
msg.attach(part)

text = msg.as_string()
server.sendmail('email@email.com', 'email2@email2.com', text)

server.quit()
