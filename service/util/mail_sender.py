import smtplib


class MailSender:

    def __init__(self, your_mail, mail, message):
        self.your_mail = your_mail
        self.mail = mail
        self.message = message

    def send_mail(self):
        try:
            smtp_obj = smtplib.SMTP('localhost')
            smtp_obj.sendmail(self.your_mail, self.mail, self.message)
            return 1
        except smtplib.SMTPException:
            return 0
