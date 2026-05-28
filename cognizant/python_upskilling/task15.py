def validate(user,pswd):
    if(user=="admin" and pswd=="pass123"):
        return True
    else:
        return False

f=lambda ans:print("Allowed") if(ans==True) else print("Not Allowed")

user=input("Enter Username: ")
pswd=input("Enter Password: ");
f(validate(user,pswd))