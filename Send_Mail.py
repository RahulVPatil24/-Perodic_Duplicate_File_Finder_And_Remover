import smtplib
from email.message import EmailMessage

def Send_Mail(attach):

    msg = EmailMessage()
    msg['Subject'] = 'Duplicate removed logs'
    msg['From'] = ''#Enter Your Mail
    msg['To'] = ''#Enter Receiver Mail
    msg.set_content('You will get an attachments soon')

    with open(attach,"rb") as fd:
        file_data = fd.read()
        file_name = fd.name
        msg.add_attachment(file_data,maintype="applicaation",subtype="txt",filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

        smtp.login('Enter Your Mail','Enter Your Password')#Enter Your Mail, Enter Your Password

        smtp.send_message(msg)
        print("mail sent")