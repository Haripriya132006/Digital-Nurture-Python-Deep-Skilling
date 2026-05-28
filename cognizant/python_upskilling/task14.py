def getresult(marks):
    if(marks>=80):
        return "A"
    elif(marks>=70):
        return "B"
    elif(marks>=50):
        return "C"
    else:
        return "F"
marks=88
print("Your grade is",getresult(marks))