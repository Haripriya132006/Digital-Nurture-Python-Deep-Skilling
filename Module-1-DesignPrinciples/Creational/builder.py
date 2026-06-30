# Product
class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []
    
    def __str__(self):
        return f"Pizza({self.size}, {self.crust}, {self.toppings})"

# Builder
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def set_crust(self, crust):
        self.pizza.crust = crust
        return self
    
    def add_toppings(self, *toppings):
        self.pizza.toppings.extend(toppings)
        return self
    
    def build(self):
        return self.pizza

# Usage
pizza1 = (PizzaBuilder()
          .set_size("Large")
          .set_crust("Thick")
          .add_toppings("Pepperoni", "Mushroom","Basil")
          .build()) # method chaining

# cant use where the return type is nul
print(pizza1)  # Pizza(Large, Thick, ['Pepperoni', 'Mushroom'])
