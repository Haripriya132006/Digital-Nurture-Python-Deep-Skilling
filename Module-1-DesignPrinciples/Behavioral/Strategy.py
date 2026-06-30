# Strategy 1 - Payment via Credit Card
class CreditCardPayment:
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card"

# Strategy 2 - Payment via PayPal
class PayPalPayment:
    def pay(self, amount):
        return f"Paid ${amount} using PayPal"

# Strategy 3 - Payment via Bitcoin
class BitcoinPayment:
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin"

# Context - uses the chosen strategy
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def process_payment(self, amount):
        return self.strategy.pay(amount)

# Usage
processor = PaymentProcessor(CreditCardPayment())
print(processor.process_payment(100))  # Paid $100 using Credit Card

processor = PaymentProcessor(PayPalPayment())
print(processor.process_payment(100))  # Paid $100 using PayPal

processor = PaymentProcessor(BitcoinPayment())
print(processor.process_payment(100))  # Paid $100 using Bitcoin