class Dress():
    def __init__(self):
        pass
    def wear(self):
        print("Wear the dress")

class Cotton(Dress):
    def wear(self):
        print("Wear a pretty dress made of cotton")
class Nylon(Dress):
    def wear(self):
        print("Wear a pretty dress made of nylon")

class Factory():
    @staticmethod
    def factory(cloth_type):
        if(cloth_type=="cotton"):
            return Cotton()
        elif(cloth_type=="nylon"):
            return Nylon()
        else:
            raise TypeError("Dress of cloth type not found")
        
def main():
    cloth_type=input("Enter cloth type: ")
    dress=Factory.factory(cloth_type)
    dress.wear()

main()