import os
import shutil
path=str(input("enter a path"))
for paths,dirs,file in os.walk(path):
    for i in file:
        m,n=os.path.splitext(i)
        if os.path.isdir(path+"\\"+n):
            shutil.move(path+"\\"+i,path+"\\"+n)
        else:
            os.mkdir(path+"\\"+n)
            shutil.move(path+"\\"+i,path+"\\"+n)
            

