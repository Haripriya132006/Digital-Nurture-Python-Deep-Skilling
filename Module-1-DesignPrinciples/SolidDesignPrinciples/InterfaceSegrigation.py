# ❌ BAD - Worker forced to implement everything
class Worker: # this is weak way of making abstract class 
          # can also make an abstract class using @abstractmethod 
          # by importing from abc import ABC,abstractmethod.. 
          # with ABC as parameter for the class
    def work(self):
        pass
    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        print("Working...")
    def eat(self):
        pass  # Robot doesn't eat!

# ✅ GOOD - Segregate interfaces
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Working...")
    def eat(self):
        print("Eating...")

class Robot(Workable):
    def work(self):
        print("Working...")