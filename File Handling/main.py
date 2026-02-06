#open(filename,mode)-->mode-->r=read,w=write,a=append,x=create
#read will read entire file
#readline will read one line
#readlines will read lines and return in a list


file=open("test.txt","r")
print(file.readline(4))
file.close()

#faster and more memory efficient method
file=open("test.txt","r")
for line in file:
    print(file.readlines())
file.close()

#writing method
#open(filename,w)-->opened in write mode, and it will overwrite everything that is already present in the file
#open(filename,a)-->opened in append mode, and it will add text at the end of the file

file2=open("gayism.txt","w")
file2.write("Yar Awaim sb  acts as gay!!!\n")
file2.write("Lodhi sb is not safe from Awaim nowadays")
file2.close()

file2=open("gayism.txt","a")
file2.write("\nI dont have proof")
file2.close()

# creating a file
#open(filename,x)-->will create a file and returns and error if the file already exists
#file3=open("gayism2.txt","x")
#file3.close()

#deleting a file

import os
os.remove("gayism2.txt")

print(os.path.exists("main.py"))


