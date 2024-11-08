import pickle
"""Write a function to Delete a Student record (Rollno, name, class, section,
mobileno, marks) in a binary file named Student.dat. Record will be deleted
based on Rollno passed as parameter to the function.
"""
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
#         clas=input("Enter the class:")
#         section=input("Enter the section:")
#         rec=[rollno,name,clas,section]
#         pickle.dump(rec,f)
def delete(roll):
    f=open('Student.dat','rb')
    l=[]
    try:
        while True:
            s=pickle.load(f)
            if s[0]==roll:
                continue
            l.append(s)
    except:
        fin=open('Student.dat','wb')
        pickle.dump(l,fin)
# add()
roll=int(input("Enter the roll number to be deleted:"))
delete(roll)
# read()
