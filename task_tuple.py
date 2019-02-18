#1) Write a program to create tuple with different data types?
n=int(input("enter length of tuple"))
l1=[]
for i in range(1,n+1):
    element=input("enter any element")
    if element.isnumeric():
        l1.append(int(element))
    else:
        l1.append(element)
l1=tuple(l1)
print(l1)


#2) Write a program that display index and value side by side?

a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
a=list(a)
for i in range(0,len(a)):
    print(str(i)+" : "+str(a[i]))

	
	
#3) Write a program to convert tuple to a string?

tup=("a","b","c")
print(type(tup))
tup=list(tup)
a=""
for i in range(len(tup)):
    a=a+tup[i]
tup=a
print(type(tup))






