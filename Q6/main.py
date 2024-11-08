"""Write a function to open the text file ABC.txt and count the number of
words that start with ‘the’, like the, their, they, them, these etc."""

def sbstrchk():
    f=open('abc.txt','r')
    s=f.read()
    s=s.split()
    c=0
    l=[]
    for i in s:
        if "the"==i[0:3].lower():
            c+=1
    print(f"The count of words starting with \"the\" is : {c}")

sbstrchk()
