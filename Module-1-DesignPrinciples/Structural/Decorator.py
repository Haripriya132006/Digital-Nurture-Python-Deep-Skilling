# Base class - the component we want to enhance
class Coffee:
    def cost(self):
        return 5
    
    def description(self):
        return "Coffee"

# Decorator - adds functionality without changing Coffee class
class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 2  # Add milk cost
    
    def description(self):
        return self.coffee.description() + ", Milk"

# Another decorator
class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 1  # Add sugar cost
    
    def description(self):
        return self.coffee.description() + ", Sugar"

# Usage
coffee = Coffee()
print(f"{coffee.description()}: ${coffee.cost()}")  # Coffee: $5

# Add milk
coffee_with_milk = MilkDecorator(coffee)
print(f"{coffee_with_milk.description()}: ${coffee_with_milk.cost()}")  # Coffee, Milk: $7

# Add milk AND sugar (wrapping decorators)
coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
print(f"{coffee_with_milk_sugar.description()}: ${coffee_with_milk_sugar.cost()}")  # Coffee, Milk, Sugar: $8