Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.maxsize
2147483647
>>> 
>>> a=2147483647
>>> print a
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a)?
>>> type(a)
<class 'int'>
>>> id(a)
54060240
>>> a=2147483648
>>> a=2147483648
>>> type(a)
<class 'int'>
>>> print(a)
2147483648
>>> a=10.2
>>> type(a)
<class 'float'>
>>> a=10+3j
>>> type(a)
<class 'complex'>
>>> a=25
>>> b=7
>>> a+b
32
>>> a-b
18
>>> a*b
175
>>> a/b
3.5714285714285716
>>> a%b
4
>>> a//b
3
>>> a**b
6103515625
>>> a==b
False
>>> a!=b
True
>>> a>b
True
>>> a<b
False
>>> a=10
>>> b=5
>>> c=1
>>> a>b
True
>>> a>b and c<b
True
>>> a>b or c>b
True
>>> a<b or c>b
False
>>> a<b and c<b
False
>>> 20 and 10
10
>>> 20 or 10
20
>>> 10 and 20
20
>>> 10 or 20
10
>>> 10 and 20 or 30
20
>>> a = 10
>>> b=20
>>> a&b
0
>>> a|b
30
>>> a>>2
2
>>> a<<2
40
>>> ~10
-11
>>> ~-10
9
>>> tech = "python"
>>> type(tech)
<class 'str'>
>>> tech(1)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    tech(1)
TypeError: 'str' object is not callable
>>> tech[2]
't'
>>> tech[-4]
't'
>>> tech[8]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    tech[8]
IndexError: string index out of range
>>> tech[1:3]
'yt'
>>> tech[:4]
'pyth'
>>> tech[2:]
'thon'
>>> tech = "python and machine learning"
>>> tech[2:10]
'thon and'
>>> tech[2:15]
'thon and mach'
>>> tech[2:15:2]
'to n ah'
>>> tech[2:15:3]
'tnnmh'
>>> tech[:]
'python and machine learning'
>>> tech[::2]
'pto n ahn erig'
>>> tech[10:2]
''
>>> tech[10:2:-1]
' dna noh'
>>> tech[::-1]
'gninrael enihcam dna nohtyp'
>>> tech
'python and machine learning'
>>> time="08:45:44 AM"
>>> tech[:2]
'py'
>>> time[:2]
'08'
>>> time[::]
'08:45:44 AM'
>>> time[::]
'08:45:44 AM'
>>> print('time:',time[::])
time: 08:45:44 AM
>>> print('time:',time[0::-2])
time: 0
>>> print('time:',time[:0:-1])
time: MA 44:54:8
>>> print('time:',time[::-1])
time: MA 44:54:80
>>> print('time:',time[::1])
time: 08:45:44 AM
>>> print('time:',time[0::2])
time: 0:54 M
>>> print('time:',time[0::1])
time: 08:45:44 AM
>>> print('time:',time[0::-1])
time: 0
>>> print('time:',time[::])
time: 08:45:44 AM
>>> 
>>> 
>>> 
>>> 
>>> a=10
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
<class 'int'>
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
<class 'int'>
h
py
pyt
nohtyp
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
<class 'int'>
h
py
pyt
nohtyp
<class 'str'>
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
20
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
20
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 15, in <module>
    print(a)
NameError: name 'a' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
20
a
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
20
a
10203
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
20
a
10 20 3
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
hello
=================== RESTART: D:/python tutorial/sample1.py ===================
hello2
2
<class 'str'>
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
helloshyam
shyam
<class 'str'>
>>> 10
10
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
hello10.52
10.52
<class 'str'>
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter anythingsdfs
sdfs
<class 'str'>
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyamkumarreddy
shyam kumar reddy
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 30, in <module>
    print("fullname=",a+" "+b+" "+c)
NameError: name 'a' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
fullname= shyam kumar reddy
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam kumarreddy
fullname= shyam kumar reddy
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam kumar reddy
fullname= shyam kumar reddy
>>> a="12 34 56"
>>> a[0:]
'12 34 56'
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam kumar 10
fullname= shyam kumar 10
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam kumar 10
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 30, in <module>
    print("fullname=",first+" "+middle+" "+last)
TypeError: can only concatenate str (not "int") to str
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
<class 'int'>
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
<class 'int'>
10
<class 'str'>
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
<class 'int'>
10
<class 'str'>
10name
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
<class 'int'>
10
<class 'str'>
report 10 name
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyamsecured50marks
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam secured 50 marks
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam secured 50 marks
shyam secured 50 marks
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam secured 50 marks
shyam secured 50 marks
shyam secured 50 marks
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam secured 50 marks
shyam secured 50 marks
shyam secured 50 50 marks
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam secured 50 marks
shyam secured 50 marks
shyam secured 50 marks in hyd
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam secured 50 marks
shyam secured 50 marks
shyam secured 50 marks in 2.000000
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam secured 50 marks
shyam secured 50 marks
shyam secured 50 marks in 2.400000
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam secured 50 marks
shyam secured 50 marks
shyam secured 50.000000 marks in 2.400000
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
first 
 second 
 third
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
first
second
third
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
first
second
third
i	am	in	a	python	class
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
i am
on duty
>>> a='12 34 56'
>>> a='12:34:60pm'
>>> h=a[-10:-9]
>>> h=a[-10:-9:-1]
>>> h=a[-10:2]
>>> h=a[2:-10]
>>> a[-10:-9]
'1'
>>> h=a[-10:-8]
>>> a[-10:-8]
'12'
>>> a[-7,-5]
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a[-7,-5]
TypeError: string indices must be integers
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
12
32
56
m
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
12
32
56
pm
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
hours 12
minutes 32
seconds 56
format pm
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
hours 12
minutes 32
seconds 56
format pm
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
python and machine learning
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
python and machine learning
PYTHON AND MACHINE LEARNING
Python and machine learning
Python And Machine Learning
pYTHON AND mACHINE LEARNING
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 61, in <module>
    print("t" in tech)
NameError: name 'tech' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 61, in <module>
    print("t" in tech)
NameError: name 'tech' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
True
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
True
True
False
False
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
True
True
True
False
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
True
True
True
False
False
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
True
True
True
False
True
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
True
True
True
False
True
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
True
True
True
False
True
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
False
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
True
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
True
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
False
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
27
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
27
3
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
27
3
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 65, in <module>
    print(tech.index(a))
NameError: name 'a' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
27
3
7
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
27
3
7
17
7
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
27
3
7
17
7
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 68, in <module>
    print(tech.replace(a,b))
NameError: name 'a' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
27
3
7
17
7
Python bnd Mbchine lebrning
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
12
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
Pythov avd Machive learvivg
12
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
Python bnd Mbchine lebrning
12
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
3
12
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
['i', 'am', 'in', 'a', 'python', 'class']
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
['i', 'am', 'in', 'a', 'python', 'class']
['i ', 'm in ', ' python cl', 'ss']
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
['i', 'am', 'in', 'a', 'python', 'class']
['i am in a ', ' class']
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
['i', 'am', 'in', 'a', 'python', 'class']
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
['i', 'am', 'in', 'a', 'python', 'class']
i am in a python class
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
['i', 'am', 'in', 'a', 'python', 'class']
i/nam/nin/na/npython/nclass
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
['i', 'am', 'in', 'a', 'python', 'class']
i
am
in
a
python
class
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
we live in India
we live in India
       we live in India
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
       we live in India   
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
e live in India
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
e live in India   
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
       we live in India
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
       we live in India
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
       we live in India   
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
       we live in India   
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
       we live in India   
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
we live in India
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
live in India
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
India
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
dia
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
shyam
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
00000shyam
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
00000shyam
00100
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
a is greater than 5
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
a is less than 5
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
chotu
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
a is greater than 5
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
a is greater than 5
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
a is less than 5
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
a thop
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter number
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 95, in <module>
    num= int(input("enter number"))
ValueError: invalid literal for int() with base 10: ''
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter number
=================== RESTART: D:/python tutorial/sample1.py ===================
enter number30
divisible by 3
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter number3
divisible by 5
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter number3
divisible by 3
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter number5
divisible by 5
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter number
=================== RESTART: D:/python tutorial/sample1.py ===================
enter number15
divisible by 3 and 5
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter number22
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter number
3
divisible by 3
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter time in format HH:MM:SSFF

=================== RESTART: D:/python tutorial/sample1.py ===================
enter time in format HH:MM:SSFF
03:05:16Pm

Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 95, in <module>
    time= int(input("enter time in format HH:MM:SSFF\n"))
ValueError: invalid literal for int() with base 10: '03:05:16Pm'
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter time in format HH:MM:SSFF

=================== RESTART: D:/python tutorial/sample1.py ===================
enter time in format HH:MM:SSFF
02:05:50Pm
02:05:50
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter time in format HH:MM:SSFF
02:02:02Pm
02:02:02
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter time in format HH:MM:SSFF
02:02:02Pm
Pm
140202
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter a path of locationD:\python tutorial
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 112, in <module>
    if path is notnull:
NameError: name 'notnull' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter a path of locationD:\python tutorial
['D:\\python tutorial']
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter a path of locationD:\python tutorial
['D:', 'python tutorial']
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter time in format HH:MM:SSFF

=================== RESTART: D:/python tutorial/sample1.py ===================
enter time in format HH:MM:SSFF

=================== RESTART: D:/python tutorial/sample1.py ===================
0
1
2
3
4
5
6
7
8
9
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 112, in <module>
    for i in range(10.20):
TypeError: 'float' object cannot be interpreted as an integer
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
11
12
13
14
15
16
17
18
19
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
12
14
16
18
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
12
16
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
12
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter a number6
*
**
***
****
*****
******
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter a number5
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 119, in <module>
    for i in range(1,n+1):
TypeError: can only concatenate str (not "int") to str
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter a number5
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 119, in <module>
    for i in range(1,n+1):
TypeError: can only concatenate str (not "int") to str
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter a number5
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 119, in <module>
    for i in range(1,n+1):
TypeError: can only concatenate str (not "int") to str
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter a number5
1
22
333
4444
55555
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter a number6

1
12
123
1234
12345
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter a number6
1
12
123
1234
12345
123456
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number5
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 136, in <module>
    p==i*n
NameError: name 'p' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number5
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 136, in <module>
    int(p)==i*n
NameError: name 'p' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number6
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 136, in <module>
    p==i*n
NameError: name 'p' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number6
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 137, in <module>
    print("5 x %d = %d"%(i,p))
TypeError: %d format: a number is required, not str
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number6
5 x 1 = 6
5 x 2 = 12
5 x 3 = 18
5 x 4 = 24
5 x 5 = 30
5 x 6 = 36
5 x 7 = 42
5 x 8 = 48
5 x 9 = 54
5 x 10 = 60
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number6
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 135, in <module>
    n=int(n+1)
TypeError: can only concatenate str (not "int") to str
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter starting point10
enter ending point20
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 143, in <module>
    for i in range(m,n+1):
TypeError: can only concatenate str (not "int") to str
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter starting point10
enter ending point20
10 is even number
11 is odd number
12 is even number
13 is odd number
14 is even number
15 is odd number
16 is even number
17 is odd number
18 is even number
19 is odd number
20 is even number
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter starting point
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number10
10 is composite with 4 factors
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number7
7is prime number
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter starting point10
enter ending point20
20is prime number
20is prime number
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter starting point10
enter ending point20
10is prime number
20is prime number
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter starting point10
enter ending point20
10 is prime
10 is prime
10 is composite
10 is composite
11 is composite
11 is composite
12 is composite
12 is composite
12 is composite
12 is composite
12 is composite
12 is composite
13 is composite
13 is composite
14 is composite
14 is composite
14 is composite
14 is composite
15 is composite
15 is composite
15 is composite
15 is composite
16 is composite
16 is composite
16 is composite
16 is composite
16 is composite
17 is composite
17 is composite
18 is composite
18 is composite
18 is composite
18 is composite
18 is composite
18 is composite
19 is composite
19 is composite
20 is composite
20 is composite
20 is composite
20 is composite
20 is composite
20 is composite
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter starting point10
enter ending point20
20 is composite
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter starting point10
enter ending point20
10 is composite
11 is prime
12 is composite
13 is prime
14 is composite
15 is composite
16 is composite
17 is prime
18 is composite
19 is prime
20 is composite
>>> chr(65)
'A'
>>> ord(S)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    ord(S)
NameError: name 'S' is not defined
>>> ord("S")
83
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter somethingpython
o
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter somethingi am in a class
i
a
i
a
a
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter somethingi am 33
3
3
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter somethingi am 64
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 158, in <module>
    print(i+end(""))
NameError: name 'end' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter somethingi am 1st ranker
1
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 157, in <module>
    m=ord(a)
NameError: name 'a' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 157, in <module>
    m=ord(a)
NameError: name 'a' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 157, in <module>
    m=ord(a)
NameError: name 'a' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4










>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4










>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4
aaaaaa
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4
aaaaaaaaaa
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4

a
aaa
aaaaaa
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4
a
aaa
aaaaaa
aaaaaaaaaa
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
enter any number4
aaaaaaaaaa
>>> ord(a)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
>>> ord("a")
97
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
ënter any number4
a
bb
ccc
dddd
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
ënter any number4
a
ab
abc
abcd
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
1
2
3
4
5
6
7
8
9
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
9
8
7
6
5
4
3
2
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
10
9
8
7
6
5
4
3
2
1
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
0
1
2
3
4
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
5
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
0
1
2
3
4
5
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
p
Traceback (most recent call last):
  File "D:/python tutorial/sample1.py", line 172, in <module>
    if i==h:
NameError: name 'h' is not defined
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
p
y
t
h
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
pyth
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
python
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
pyton
>>> 
=================== RESTART: D:/python tutorial/sample1.py ===================
>>> 
