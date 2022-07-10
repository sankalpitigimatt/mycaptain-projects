list1=[]
list2=[]
l2=[]
l3=[]
n=int(input("enter the total number of elements you want to enter in list1::"))
for i in range(0,n):
    m=int(input("enter elements ::"))

    list1.append(m)
print("LIST1::")
print(list1)

for i in list1:
    if i>0:
        l2.append(i)
print("The positive elements are::")
print(l2)

x=int(input("enter the total number of elements you want to enter in list2::"))
for i in range(0,x):
    y=int(input("enter elements::"))

    list2.append(y)
print("LIST2::")
print(list2)
for j in list2:
    if j>0:
        l3.append(j)

print("The positive elements are::")
print(l3)


