"""Write a function to add (append) Employee records (Empno, name and
address, salary) onto a Binary file"""
import pickle
def add():
    f=open('emp.dat','wb')
    n=int(input("Enter the number of records you want to insert:"))
    for i in range(n):
        empno=int(input("Enter the employee number:"))
        name=input("Enter the employee name:")
        address=input("Enter the employee address:")
        salary=int(input("Enter the employee salary:"))
        rec=[empno,name,address,salary,]
        pickle.dump(rec,f)
# def read():
#     f=open('emp.dat','rb')
#     try:
#         while True:
#             s=pickle.load(f)
#             print(*s)
#     except:
#         f.close()
add()
# read()
