import smtplib
import configuration as config

class mail_notify:
    def __init__(self,toAddress,message):
        self.toAddress=toAddress
        self.message=message

    def send_mail(self):
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(config.fromAddress,config.password)
        server.sendmail(config.fromAddress,self.toAddress,self.message)
        print('Successfully sent to: ',self.toAddress)
        server.quit()

obj=mail_notify(config.toAddress,config.message)
obj.send_mail()
