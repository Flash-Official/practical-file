"""Write a Python program to count all lines in the file ABC.txt having ‘a’ as
the last character."""
f=open("abc.txt",'r')
c=0
s=f.readlines()
for i in s:
    k=i.split()
    if k[-1][-1].lower()=="a":
        c+=1
print(f"The number of lines ending with \"a\" is : {c}")
