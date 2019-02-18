class org:  #defining a class
    name='lync'
    address='hyd'
    emp_count=15
o1=org()    #defining an object
o2=org()    #defining an object
#object reference
print(o1.name)
print(o1.emp_count)

#class reference
print(org.name)
print(org.emp_count)

#changing class variable
o1.name="DL"
print(o1.name)
print(org.name)
print(o2.name)

#changing class varable
org.name="digital lync"
print(org.name)
print(o1.name)
print(o2.name)

print(org)
print(o1)
print(o2)



class func():   #function inside a class
    def addnums(something,a,b):     #anything can be in place of something
        sum=a+b
        print(sum)
o1=func()
o2=func()
o3=func()
o1.addnums(10,20)
o2.addnums(10,20)
o3.addnums(10,30)
#func.addnums(10,20) throws an error



class company():
    cname="lync"
    caddr="hyd"
    ccount=100
    def hire(self,name,role):
        print(name+" hired for "+role)
        company.ccount=company.ccount+1
    def printedetails(self):
        print(name)
        print(role)
        print(company.cname)
    def printcdetails(self):
        print(company.ccount)
        print(company.caddr)
        print(company.cname)        
        
e1=company()
e2=company()
e3=company()

e1.hire("shyam","se")
e1.printcdetails()

e2.hire("iqbal","se")
e2.printcdetails()



#above code using constructor __init__

class company():
    cname="lync"
    caddr="hyd"
    ccount=100
    
    def __init__(self,name,role):
        self.name=name
        self.role=role
#    def hire(self,name,role):
        print(self.name+" hired for "+self.role)
        company.ccount=company.ccount+1
    def printedetails(self):
        print(self.name)
        print(self.role)
        print(company.cname)
    def printcdetails(self):
        print(company.ccount)
        print(company.caddr)
        print(company.cname)    
        
    @classmethod   #decorator for class method
    def changeCname(cls,newname):
        company.cname=newname
        print("company name has changed to "+company.cname)
        
    @staticmethod   #decorator for static method
    def calc(a,b):
        print(a*b)
        
e1=company("shyam","se")
e2=company("iqbal","se")
e3=company("aditya","associate")

e1.changeCname("DL")
e2.calc(2,3)
#e1.printedetails()
#e1.printcdetails()


#print(company.ccount)

#e1.hire("shyam","se")
#e2.hire("iqbal","se")
e2.printcdetails()