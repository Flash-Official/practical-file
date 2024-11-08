"""Write a function to transfer all lines starting with a vowel from ORIGIN.txt
to NEW.txt."""
def vow():
    f=open('origin.txt','r')
    fin=open('new.txt','w')
    s=f.readlines()
    for i in s:
        if i[0].lower() in "aeiou":
            fin.write(i)
vow()
