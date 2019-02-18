# 1) Write a program for printing ͞yhnetobgnes͟ from ͞pythonbestforbeginners͟. 
a="pythonbestforbeginners"
print(a[1::2])

# 2) Write a program to print reverse of a user given string. 
print(a[-1::-1])


# 3) Write a program to change all occurrences of 3rd character with ͞@͟? 
a="pythonbestforbeginners"
a=a.replace(a[4],"@")
print(a)
#output:pyth@nbestf@rbeginners

# 4) Write a program to replace a string with new string only specified number of times? 
a="pythonbestforbeginners"
a=a.replace(a[4],"@",1)
print(a)
#output:pyth@nbestforbeginners

# 5) Write a program to print character that are at multiples of 3 position in a user input string? 
a=str(input("Enter something"))
for i in range(int(len(a)/3)):
    print(a[i*3],end=" ")
#output:
##Enter somethingiam in a python class
##i     p h   a 

# 6) Write a program that exchange value of two numbers without using temporary variable. 
a=12
b=34
a=a+b
b=a-b
a=a-b
print(a,b)