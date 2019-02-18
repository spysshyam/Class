####a=10
####print(a)
####print(type(a))
####
####
####tech="python"
####print(tech[3])
####print(tech[0:2])
####print(tech[:3])
####print(tech[::-1])
####print(type(tech))
######
####print(10)
####print(20)
####print('a')
##
##print(10,end=" ")
##print(20,end=" ")
##print(3)

##a=input("enter anything")
##print(a)
##print(type(a))


##first="shyam"
##middle="kumar"
##last=10
##print(first,middle,last)
##print("fullname=",first+" "+middle+" "+last)
##
##b="name"
##a=10
##print(a)
##print(type(a))
##
##a=str(a)
##print(a)
##print(type(a))
##
##print("report",a+" "+b)

##book="first\nsecond\nthird"
##print(book)
##
##para="i\tam\tin\ta\tpython\tclass"
##print(para)

##time="12:32:56pm"
##print("hours",time[:-8])
##print("minutes",time[-7:-5])
##print("seconds",time[-4:-2])
##print("format",time[-2:])
##
#tech = "Python and Machine learning"
##print(tech.lower())
##print(tech.upper())
##print(tech.capitalize())
##print(tech.title())
##print(tech.swapcase())


##print(len(tech))
##print(tech.count("a"))
##print(tech.index("a"))
##print(tech.index("e"))
##print(tech.find("a"))
#print(tech.replace('a','b') and tech.count('a'))
#print(tech.index("a",(tech.index("a")+1)))
##dia = "i am in a python class"
####print(dia.split())
#print(dia.split("python"))
##words = dia.split()
##print(words)
##print("\n".join(words))



##dia="   in india   "
##
####print(dia.strip())
####print(dia.lstrip())
####print(dia.rstrip())
##
##print(dia.strip(" in"))
##
##name="shyam"
##print(name.zfill(10))
##
##num=100
##print(str(num).zfill(5))0



##time= input("enter time in format HH:MM:SSFF\n")
##if len(time)==10:
##    minutes=time[3:5]
##    seconds=time[6:8]
##    hours=(time[:2])
##    if int(hours)==12 and lower(time[8:10])=="pm":
##            print(str(hours)+":"+minutes+":"+seconds)
##        elif lower(time[8:10])=="pm":
##            hours=hours+12
##            print(str(hours)+":"+minutes+":"+seconds)
##    else:
##        print(time[:8])
##    


#path = input("enter a path of location")
#print(path.split("\\"))
##for i in range(10,20):
##    if i%4==0 and i%3==0:
##        print(i)


##n = input("enter a number")
##if n.isdigit():
##    n=int(n)
##    for i in range(1,n+1):
##        
##        print(str(i)*i)
##
##else:
##    print("enter only numbers")

##n = int(input("enter a number"))
##for j in range(1,n+1):
##    for i in range(1,j+1):
##        print(i,end="")
##    print()


##n=input("enter any number")
##n=int(n)
##for i in range(1,11):
##    p=i*n
##    print("%d x %d = %d"%(n,i,p))


##m = int(input("enter starting point"))
##n = int(input("enter ending point"))
##for i in range(m,n+1):
##    count = 0
##    for j in range(1,n+1):
##        if i%j==0:
##            count +=1
##    if count > 2:
##        print(str(i) +" is composite")
##    else:
##        print(str(i) + " is prime")
##

##n=int(input("ënter any number"))
##m=ord("a")
##for i in range(0,n):
##    print(chr(m+i)*(i+1))
    
##a=10
##while a>0:
##    print(a)

##for i in range(0,11):
##    print(i)
##    if i==5:
##        break

##
##tech="python"
##for i in tech:
##    if i=="h":
##        continue
##    

##nums = [1,2,3,4,5]
##print(nums)
##print(type(nums))
##
##chars=["python","java","c++","php"]
##print(chars)
##print(type(chars))
##
##mix=[1,"a",2,"b",3,"c"]
##mix[3]="k"
##print(mix)
##list=[0,1,2,3,[4,5,6],5,6]
##print(list)
##print(list[4])
##print(list[4][1])

##ll=[[[[[[[[10]]]]]]]]
##print(ll[0][0][0][0][0][0][0][0])

##mix=[1,"a",2,"b",3,"c"]
##mix.append(4)
##print(mix)
##mix.insert(3,"d")
##print(mix)

##l1=[2,3,4,5,6,7,7,8,6,2,5,4,3,2,12,1]
##l2=[]
##for i in l1:
##    if i not in l2:
##        l2.append(i)
##print(l2)

##n=int(input("enter any number"))
##l1=[]
##for i in range(n+1):
##    l1.append(i)
##print(l1)

##statement=str(input("enter any statement"))
##l1=statement.split()
##l2=[]
##for i in l1:
##    if len(i)>5:
##        i.strip()
##        l2.append(i)
##print(l2)

##import sys
##nums=[]
##if len(sys.argv)==2:
##    n=int(sys.argv[1])
##    for i in range(0,n+1):
##        nums.append(i)
##else:
##    print('do not enter multiple values')
##print(nums)

##ip=[10,300,"python",4,67,56,"java","c++",3]
##op=[]
##for i in ip:
##    if type(i)==int:
##        op.append(i*i)
##    else:
##        op.append(len(i))
##print(ip)
##print(op)

##city=["hyd","bom","cal","bng","chn","pun","del"]
##ind=[2,6,1]
##op=[]
##if max(ind)>=len(city):
##    print("list index is out of bounds")
##else:
##    for i in ind:
##        op.append(city[i])
##print(op)

##l1=["cal","ban",["java","c++",3,"chn"],"python",[4,67],56]
##op=[]
##for i in l1:
##    if type(i) != list:
##        op.append(i)
##    else:
##        for j in i:
##            op.append(j)
##print(l1)
##print(op)
##import sys
##op=[]
##for i in range(int(sys.argv[1])):
##    ele=input("enter a element")
##    op.append(ele)
##print(op)
##print(type(op))
##op=tuple(op)
##print(op)
##print(type(op))
##l1=[1,2,3]
##l2=[10,20,30]
##dict={}
##for i in range(len(l1)):
##    dict[l1[i]]=l2[i]
##print(dict)
##n=int(input("enter any number "))
##dict={}
##for i in range(1,n+1):
##    dict[i]=i**2
##print(dict)

##n=input("enter something")
##dict={}
##for i in n.split(" "):
##    dict[i]=len(i)
##print(dict)

##numset=set(())
##print(type(numset))

##set={1,2,3,"python"}
##set.add(10)
##print(set)
##set.remove(2)
##print(set)
##set.discard(3)
##print(set)

##
##s1={10,20,30,40}
##s2={30,40,50,60}
##s3={20}
##s4={100}
##print(s1.union(s2))             s1|s2
##print(s1.intersection(s2))      s1&s2
##print(s1.difference(s2))        s1-s2
##print(s2.difference(s1))        s2-s1
##print(s1.issuperset(s3))        s1>s2
##print(s1.issubset(s2))          s1<s2
##print(s1.isdisjoint(s2))        NA


##def add(a,b):
##    sum=a+b
##    print(sum)
##    return sum
##print(add(10,20))

##fo=open("testfile.txt","w")
##fo.write("hello \n")
##fo.write("bye \n")
##words=["first\n","seconds\n","third\n"]
##fo.writelines(words)
##
##fo.close()

##fo=open("testfile.txt","r")
##data=fo.read(10)
##print(data)
##print(fo.tell())
##fo.seek(15)
##print(fo.tell())
##fo.close()

##import os
##print(os.name)
##print(os.getcwd())
##os.chdir(r"C:\Users\hp\Desktop")
##print(os.getcwd())
##print(os.listdir(r"C:\Users\hp\Desktop"))
##
##
##import os
##os.mkdir("demo")
##os.makedirs

##import os
##path,end=os.path.split(r"C:\Users\hp\Desktop\text.txt")
##print(path)
##print(end)

##import os
##path,end=os.path.splitext(r"C:\Users\hp\Desktop\text.txt")
##print(path)
##print(end)

##import os
##for paths,dirs,files in os.walk(r"C:\Users\hp\Desktop"):
##    print(paths)
##    print(dirs)
##    print(files)


##import random
##print(random.random())
##print(random.randint(2,20))
##print(random.randrange(2,20))

import random
#num=int(input("enter any number"))
def numgen(num):
   ans=""
   for i in range(num):
       ans=ans+str(random.randint(0,9))
   return ans
#print(numgen(5))


##import random
#num=int(input("enter any number"))
def chrgen(num):
   ans=""
   chars=[]
   for i in range(num//2):
       chars.append(chr(random.randint(ord("a"),ord("z"))))
       chars.append(chr(random.randint(ord("A"),ord("Z"))))
   random.shuffle(chars)
   for i in chars:
       ans=ans+str(i)
   return ans
#print(chrgen(5))

import random

def combine():
    password=numgen(4)+chrgen(4)+numgen(4)+chrgen(4)
    return password
print(combine())



































































