# ❌ BAD - User class does too much
class User:
    def save_to_db(self):
        pass
    def send_email(self):
        pass

# ✅ GOOD - Each class has one job
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to database")

class EmailService:
    def send(self, user):
        print(f"Sending email to {user.name}")