list1=[]
list2=[]
m=int(input("enter the limit of list 1:"))
print("Enter the elements:")
for i in range(0,m):
    value=int(input())
    list1.append(value)
n=int(input("Enter the limit of list 2:"))
print("Enter the elements:")
for i in range(0,n):
    value=int(input())
    list2.append(value)
print(list1,list2)

if len(list1)==len(list2):
    print("Both List1 and List2 are of the same length")
else:
    print("Both List1 and List2 are off not the same length")

if sum(list1)==sum(list2):
    print("The sum of both List 1 and List 2 are same")
else:
    print("The sum of both List 1 and List 2 are not the same")

list3=[each for each in list1 if each in list2]
print("Same members are:",list3)
    
