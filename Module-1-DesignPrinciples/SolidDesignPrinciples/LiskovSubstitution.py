# ❌ BAD - Penguin breaks Bird's contract
class Bird:
    def fly(self):
        print("Flying...")

class Penguin(Bird):
    def fly(self):
        raise Exception("Can't fly!")  # Violates LSP!

# ✅ GOOD - Both preserve behavior
class Bird:
    def move(self):
        pass

class Eagle(Bird):
    def move(self):
        print("Flying high!")

class Penguin(Bird):
    def move(self):
        print("Swimming!")

bird1 = Eagle()
bird2 = Penguin()
bird1.move()  # Works as expected
bird2.move()  # Works as expected