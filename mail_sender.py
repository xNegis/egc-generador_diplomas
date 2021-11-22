import smtplib  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pathlib
import codecs

msg = MIMEMultipart()
path = str(pathlib.Path().resolve())
msg.attach(MIMEText(open(path+"\prueba2.pdf",errors='ignore').read()))

mailer = smtplib.SMTP()
mailer.connect()
mailer.sendmail("xnegis@gmail.com", "xnegis@gmail.com", msg.as_string())
mailer.close()

def send_email_pdf_figs(path_to_pdf, subject, message, destination, password_path=None):
    from socket import gethostname
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    import json

    my_mail = 'diplomaapiinnosoft@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    with open(password_path) as f:
        config = json.load(f)
        server.login(my_mail, "Innosoft")
        # Craft message (obj)
        msg = MIMEMultipart()

        message = f'{message}\nSend from Hostname: {gethostname()}'
        msg['Subject'] = subject
        msg['From'] = my_mail
        msg['To'] = destination
        # Insert the text to the msg going by e-mail
        msg.attach(MIMEText(message, "plain"))
        # Attach the pdf to the msg going by e-mail
        with open(path_to_pdf, "rb") as f:
            attach = MIMEApplication(f.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str(path_to_pdf))
        msg.attach(attach)
        # send msg
        server.send_message(msg)

send_email_pdf_figs(str(pathlib.Path().resolve())+"\prueba2.pdf","xfa","funciona","diplomaapiinnosoft@gmail.com")