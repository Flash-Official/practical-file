"""Write a Python program to count the number of digits in the text file
DIGIT.txt."""

f=open("digit.txt",'r')
s=f.read()
c=0
for i in s:
    if i.isdigit()==True:
        c+=1
print(f"The number of digits in the file is : {c}")
