"""Write a program using a function to input a list of elements and display a
list with only duplicate elements after removing the unique ones.
Output:
The original list: [10, 20, 30, 10, 40, 20, 50]
The Duplicate list: [10, 20]"""

def lstdp(l):
    k=[]
    dup=[]
    for i in l:
        if i not in k:
            k.append(i)
    for i in k:
        c=l.count(i)
        if c>1:
            dup.append(i)
    print(f"The duplicate elements are : {dup}")

v=eval(input("Enter the list:"))
lstdp(v)