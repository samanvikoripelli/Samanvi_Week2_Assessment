class notification:
    def send(self):
        print("sending a notification")
class emailnotification(notification):
    def send(self):
        print("send email notification")
class smsnotification(notification):
    def send(self):
        print("sending sms notification")
notifications = [emailnotification(),smsnotification()]
for notification in notifications:
    notification.send()