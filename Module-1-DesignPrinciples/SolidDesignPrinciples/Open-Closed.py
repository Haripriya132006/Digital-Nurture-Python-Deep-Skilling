# ❌ BAD - Need to modify PaymentProcessor every time
class PaymentProcessor:
    def process(self, payment_type, amount):
        if payment_type == "credit":
            print(f"Process credit: ${amount}")
        elif payment_type == "paypal":
            print(f"Process paypal: ${amount}")

# ✅ GOOD - Extend without modifying
class Payment:
    def process(self, amount):
        pass

class CreditCard(Payment):
    def process(self, amount):
        print(f"Process credit: ${amount}")

class PayPal(Payment):
    def process(self, amount):
        print(f"Process paypal: ${amount}")

payment = CreditCard()
payment.process(100)