import pickle
"""Write a function to Update marks of a Student record (Rollno, name,
marks)in a binary file named Student.dat. Record will be updated based on
Rollno passed as parameter to the function."""

# def read():
#     f=open('Student.dat','rb')
#     try:
#         while True:
#             s=pickle.load(f)
#             print(*s)
#     except:
#         f.close()
# def add():
#     f=open('Student.dat','wb')
#     n=int(input("Enter the number of records you want to insert:"))
#     for i in range(n):
#         rollno=int(input("Enter the roll number:"))
#         name=input("Enter the name:")
#         marks=int(input("Enter the marks:"))
#         rec=[rollno,name,marks]
#         pickle.dump(rec,f)
def update(roll):
    f=open('Student.dat','rb')
    l=[]
    try:
        while True:
            s=pickle.load(f)
            if s[0]==roll:
                name=input("Enter the name:")
                marks=int(input("Enter the marks:"))
                rec=[name,marks]
                l.append(rec)
                continue
            l.append(s)
    except:
        fin=open('Student.dat','wb')
        pickle.dump(l,fin)

# add()
roll=int(input("Enter the roll number which needs to be updated:"))
update(roll)
# read()
