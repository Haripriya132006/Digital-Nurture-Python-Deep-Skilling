# ❌ BAD - Depends on concrete class
class EmailService:
    def send(self, message):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self):
        self.email = EmailService()  # Hardcoded dependency!
    
    def notify(self):
        self.email.send("Hello")

# ✅ GOOD - Depends on abstraction
class NotificationService:
    def send(self, message):
        pass

class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

class Notification:
    def __init__(self, service):
        self.service = service  # Accept any NotificationService
    
    def notify(self):
        self.service.send("Hello")

email = EmailService()
notif = Notification(email)
notif.notify()