#) Write a program to find second largest number in a list?
l1=[1,2,3,4,5]
l1.sort()
print(l1[len(l1)-2])


#2) Write a program for calculating Mode of list numbers?

l1=[1,2,2,2,3,4,4,5]
lmode=[]
for i in l1:
    if l1.count(i)>l1.count(i+1):
        lmode.append(i)
        if i+1 in lmode:
            lmode.remove(i+1)
    else:
        lmode.append(i+1)
        if i in lmode:
            lmode.remove(i)
print(lmode[0])
    
	

#3) Write a program to remove the duplicate items from the list?
l1=[1,2,2,2,3,4,4,5]
for i in l1:
    if l1.count(i)>=2:
        l1.remove(i)
print(l1)



#4) Lets say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Write one line of Python that takes this list a and
#makes a new list that has only the even elements of this list in it.
a_1=[]
for i in a:
    if i%2==0:
        a_1.append(i)
print(a_1)



#5) Write a program to add two matrices?
X= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

result = [[X[i][j] + Y[i][j]  for j in range
(len(X[0]))] for i in range(len(X))] 
  
for r in result: 
    print(r)

	
	
	
#6) Write a program to display multiplication table?
table=[]
n=int(input("enter any number"))
for i in range(1, 11):
    value=str(n)+'x'+str(i)+'='+str(n*i)
    table.append(value)
print(table)

