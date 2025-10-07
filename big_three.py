print("Enter 3 numbers:")
n1=int(input("1st number:"))
n2=int(input("2nd number:"))
n3=int(input("3rd number:"))

if(n1>n2 and n1>n3):
    print(n1,"is the biggest")
elif(n2>n3):
    print(n2,"is the biggest")
else:
    print(n3,"is the biggest")
