"""Write a program to input two dictionary and then subtract the values of two
dictionary.
Output :
The original dictionary 1: {'gfg': 6, 'is': 4, 'best': 7}
The original dictionary 2: {'gfg': 10, 'is': 6, 'best': 10}
The difference dictionary is : {'gfg': 4, 'is': 2, 'best': 3}"""

d1=eval(input("Enter dictionary 1:"))
d2=eval(input("Enter dictionary 2:"))
d={}
for i in d1:
    if i in d2:
        d[i]=d2[i]-d1[i]

print(f"The difference dictionary is : {d}")
