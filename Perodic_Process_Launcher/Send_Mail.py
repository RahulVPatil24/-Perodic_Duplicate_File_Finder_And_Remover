import smtplib
from email.message import EmailMessage

def Send_Mail(attach):

    msg = EmailMessage()
    msg['Subject'] = 'Process Logs'
    msg['From'] = ''#Enter Your Mail
    msg['To'] = ''#Enter Receiver Mail
    msg.set_content('Your given processes are sucessfully running logs are in below attachments')

    with open(attach,"rb") as fd:
        file_data = fd.read()
        file_name = fd.name
        msg.add_attachment(file_data,maintype="application",subtype="txt",filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

        smtp.login('','')#Enter Your Mail, Enter Your Password

        smtp.send_message(msg)
        print("mail sent")