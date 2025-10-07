clist1 = set()
clist2 = set()
n1 = int(input("eenter thhe number of colors in list 1:"))
print("enter the colors to list1 :")
for x in range(n1):
    color = input()
    clist1.add(color)
n2 = int(input("eenter thhe number of colors in list 2:"))
print("enter the colors to list2 :")
for x in range(n2):
    color = input()
    clist2.add(color)
diff=clist1.difference(clist2)
if len(diff)==0:
    print("same colors in list1 and list2:")
else:
    print("colors in list1 is not in list2",diff)
