"""Write a Function to read data from a text file DATA.TXT, and display those
words, which are less than 4 characters"""
def readwords():
    f=open('data.txt','r')
    s=f.read()
    s=s.split()
    for i in s:
        if len(i)<4:
            print(i,end=" ")

readwords()
