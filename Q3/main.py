"""Write a program to take input of two lists from the user and perform union
and intersection of these two lists.
Example:
Enter first list: [2,3,5,6,7,8]
Enter second list: [4,5,6,9]
Union: [2,3,4,5,6,7,8,9]
Intersection: [5,6]
"""

def union(l1,l2):
    l1c=l1[:]
    for i in l2:
        if i not in l1:
            l1c.append(i)
        
    print(f"Union of the two lists is : {sorted(l1c)}")

def intersection(l1,l2):
    k=[]
    for i in l1:
        if i in l2:
            k.append(i)
    print(f"The intersection of the two lists is : {k}")


l1=[2,3,5,6,7,8]
l2=[4,5,6,9]

union(l1,l2)
intersection(l1,l2)
