def kgtolbs(kg):
    if(isinstance(kg,float)):
        return kg*2.20462
    else:
        print("give a float value as input")

kg=float(input("Enter kg: "))
print(f"{kgtolbs(kg):.2f}")