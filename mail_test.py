from email.mime.base import MIMEBase
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import COMMASPACE, formatdate
from email import encoders
import os
import pathlib
USERNAME = "diplomaapiinnosoft@gmail.com"
PASSWORD = "Innosoft"

def sendMail(to, subject, text, files=[]):
    assert type(to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME, to, msg.as_string())
    server.quit()

path = str(pathlib.Path().resolve())
sendMail( [USERNAME],
        "Alarm notification",
        "Someone has entered the room, picture attached",
        [path+"\prueba2.pdf"]
         )