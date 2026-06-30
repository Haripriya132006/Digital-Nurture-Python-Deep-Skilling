from abc import ABC, abstractmethod

class Pizza:
     
    def __init__(self):
        self.size = None          # Required
        self.crust = None         # Required
        self.sauce = None         # Optional
        self.cheese = None        # Optional
        self.toppings = []        # Optional
        self.is_vegetarian = False
        self.is_spicy = False
    
    def __str__(self):
        """Display the pizza configuration"""
        toppings_str = ", ".join(self.toppings) if self.toppings else "None"
        return f"""
            ╔════════════════════════════════════════╗
            ║            🍕 YOUR PIZZA 🍕            ║
            ╚════════════════════════════════════════╝
            Size:           {self.size}
            Crust:          {self.crust}
            Sauce:          {self.sauce}
            Cheese:         {self.cheese}
            Toppings:       {toppings_str}
            Vegetarian:     {self.is_vegetarian}
            Spicy Level:    {'🌶️  ' * self.is_spicy if self.is_spicy else 'Not spicy'}
            ╚════════════════════════════════════════╝
        """


class PizzaBuilder:
 
    def __init__(self):
        self.pizza = Pizza()
        print("Pizza Builder created!")
    
    def set_size(self, size):
        if size not in ["Small", "Medium", "Large", "Extra Large"]:
            raise ValueError(f"Invalid size: {size}")
        
        self.pizza.size = size
        print(f"Size: {size}")
        return self  # ← Return self for chaining!
    
    def set_crust(self, crust):
        
        if crust not in ["Thin", "Regular", "Thick", "Stuffed"]:
            raise ValueError(f"Invalid crust: {crust}")
        
        self.pizza.crust = crust
        print(f"Crust: {crust}")
        return self
    
    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        print(f"Sauce: {sauce}")
        return self
    
    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        print(f"✅ Cheese: {cheese}")
        return self
    
    def add_toppings(self, *toppings):
        """
        Example: .add_toppings("pepperoni", "mushrooms", "onions")
        """
        for topping in toppings:
            self.pizza.toppings.append(topping)
        print(f"Added toppings: {', '.join(toppings)}")
        return self
    
    def make_vegetarian(self):
        """
        Make the pizza vegetarian.
        
        This is a convenience method that removes meat and sets a flag.
        """
        self.pizza.is_vegetarian = True
        # Remove meat toppings
        self.pizza.toppings = [t for t in self.pizza.toppings 
                              if t not in ["Pepperoni", "Sausage", "Bacon", "Ham"]]
        print("Made vegetarian (removed all meats)")
        return self
    
    def make_spicy(self, level=1):

        self.pizza.is_spicy = level
        if level > 0:
            self.add_toppings("Jalapeños")
        if level > 1:
            self.add_toppings("Habaneros")
        if level > 2:
            self.add_toppings("Ghost Peppers")
        print(f"Made spicy (level {level})")
        return self
    
    def build(self):
        # Validation - make sure required parts are set
        if not self.pizza.size:
            raise ValueError("Size is required!")
        if not self.pizza.crust:
            raise ValueError("Crust is required!")
        
        print("\n✨ Pizza is ready!\n")
        return self.pizza


# ============================================================================
# DIRECTOR CLASS - For common pizza types
# ============================================================================

class PizzaDirector:
    """
    The PizzaDirector.
    
    This creates common pizza types without needing to specify everything.
    Think of this as "preset" pizzas on a menu.
    """
    
    def __init__(self, builder):
        self.builder = builder
    
    def create_margherita(self):
        print("\n📊 Director: Creating MARGHERITA pizza...\n")
        return (self.builder
                .set_size("Large")
                .set_crust("Thin")
                .set_sauce("Tomato")
                .set_cheese("Mozzarella")
                .add_toppings("Basil", "Tomato Slices")
                .make_vegetarian()
                .build())
    
    def create_pepperoni(self):
        print("\n📊 Director: Creating PEPPERONI pizza...\n")
        return (self.builder
                .set_size("Large")
                .set_crust("Regular")
                .set_sauce("Tomato")
                .set_cheese("Mozzarella")
                .add_toppings("Pepperoni")
                .build())
    

def main():
    print("\n\n[EXAMPLE 1] Building a CUSTOM pizza step-by-step")
    print("-" * 60)
    
    builder = PizzaBuilder()
    my_pizza = (builder
                .set_size("Large")
                .set_crust("Thick")
                .set_sauce("Tomato")
                .set_cheese("Mozzarella")
                .add_toppings("Pepperoni","Basil")
                .build())
    
    print(my_pizza)
    
    builder2 = PizzaBuilder()
    minimal_pizza = (builder2
                     .set_size("Small")
                     .set_crust("Regular")
                     .build())
    
    print(minimal_pizza)
    
    
    # ╔══════════════════════════════════════════════════════════════════╗
    # EXAMPLE 3: Using Director for Pre-defined Pizzas
    # ╚══════════════════════════════════════════════════════════════════╝
    
    print("\n\n[EXAMPLE 3] Using DIRECTOR for preset pizzas")
    print("-" * 60)
    
    builder3 = PizzaBuilder()
    director = PizzaDirector(builder3)
    
    # Get a Margherita pizza
    margherita = director.create_margherita()
    print(margherita)

    print("\n\n[EXAMPLE 3] Using DIRECTOR for preset pizzas")
    print("-" * 60)
    builder6 = PizzaBuilder()
    try:
        incomplete_pizza = (builder6
                            .set_size("Large")
                            #no crust!
                            .set_sauce("Tomato")
                            .build())
    except ValueError as e:
        print(f"Error caught: {e}")

main()