"""Write a Program to connect with database and store record in employee
table (empno, empname, department, salary) and display entire records.
"""
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='jeet',database="employee")
# def create():
#     cursor.execute("""create table if not exists employee(
#                     empno INT PRIMARY KEY,
#                     name  varchar(25),
#                     dep varchar(25),
#                     salary INT
#                     )""")
#     conn.commit()
#     return "Table Created"
def show():
    cursor.execute('select * from employee')
    data=cursor.fetchall()
    for row in data:
        print(*row)

def store():
    n=int(input("Enter the number of entries:"))
    for i in range(n):
            eno=int(input("Enter the employee number:"))
            name=input("Enter the employee name:")
            dep=input("Enter the employee department:")
            sal=int(input("Enter the employee salary:"))
            query="insert into employee values({},'{}','{}','{}')".format(eno,name,dep,sal)
            cursor.execute(query)
            conn.commit()
if conn.is_connected():
    cursor=conn.cursor()
    # x=create()
    # print(x)
    # cursor.execute("create database employee")
    # conn.commit()
    store()
    show()
