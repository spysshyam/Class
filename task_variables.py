L=["digital","Lync","hyderabad","gachibowli","kukatpally"]
a="Lync"
for i in range(len(L)):
    if L[i]==a:
        print("given string is there in sequence")
    

# output:given string is there in sequence


a=45
b=65
print(a&b)
print(a|b)
print(a>>b)
print(a<<b)
print(~a)
print(~b)

# OUTPUT: 1
# 109
# 0
# 1660206966633859645440
# -46
# -66

import math
z=65.33
z=int(z)
print(~z)
print(abs(z))
print(math.factorial(z))
print(math.sqrt(z))
print(math.exp(z))

#output:
##-66
##65
##8247650592082470666723170306785496252186258551345437492922123134388955774976000000000000000
##8.06225774829855
##1.6948892444103338e+28



z=1234
z=str(z)
y=int(z[0])
for i in range(1,len(z)):
    y=y+int(z[i])
print(y)
    
#output: 10



print(15==2)
print(15!=2)
print(15>2)
print(15<2)
print(15>=2)
print(15<=2)

##False
##True
##True
##False
##True
##False





