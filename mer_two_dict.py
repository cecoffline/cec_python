mydict1={}
print("enter elements of the first dictinoary:")
while True:
    key=input("Enter a key(or 'q' to quit):")
    if key=='q':
        break;
    value=int(input("Enter a value:"))
    mydict1[key]=value
    
mydict2={}
print("enter elements of the second dictinoary:")
while True:
    key=input("Enter a key(or 'q' to quit):")
    if key=='q':
        break;
    value=int(input("Enter a value:"))
    mydict2[key]=value
print("Mergerd dictionaries are:")    
print(mydict1|mydict2)
