# 1) Write a program for grading system of marks? 
s1=int(input("enter marks of subject 1 out of 100"))
s2=int(input("enter marks of subject 2 out of 100"))
s3=int(input("enter marks of subject 3 out of 100"))
avg=(s1+s2+s3)/3
if s1>=40 or s2>=40 or s3>=40:
    if avg>90:
        print("student secured A grade")
    elif avg<=90 and avg>70:
        print("student secured B grade")
    elif avg<=70 and avg>=40:
        print("student secured C grade")
else:
    print("student has failed")

#output:
##enter marks of subject 1 out of 10040
##enter marks of subject 2 out of 10050
##enter marks of subject 3 out of 10060
##student secured C grade
	


# 2) Write a program that check for leap year? 
year=int(input("enter year"))
if year%4==0:
    print("%d is leap year"%year)
else:
    print("%d is not a leap year"%year)
##enter year2016
##2016 is leap year


# 3) Write a program that checks the number is even or odd? 
num=int(input("enter any number"))
if num%2==0:
    print("%d is even number"%num)
else:
    print("%d is odd number"%num)
	
# 4) Write a program that takes country, state and print number of districts by users? 

# 5) Write  a program for finding largest of Three numbers? 
a=7
b=6
c=5
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")
