"""Write a Program to connect with database and update a record from
employee table (empno, empname, department, salary) based on empno and
display records"""

import mysql.connector as sql

conn=sql.connect(host="localhost",user="root",password="jeet",database="employee")
cursor=conn.cursor()
def create():
    try:
        q="""create table if not exists employee(
        empno int primary key,
        name varchar(25),
        department varchar(25),
        salary int
    )"""
        cursor.execute(q)
        conn.commit()
        return "Table created"
    except:
        return "Error in table creation"

def update(empno):
    cursor.execute(f"select * from employee where empno={empno}")
    data=cursor.fetchall()
    if data:
        name=input("Enter the name to be updated:")
        department=input("Enter the department to be updated:")
        salary=int(input("Enter the salary to be updated:"))
        q=f"""update employee
        set name='{name}',dep='{department}',salary={salary}
        where empno={empno}"""
        cursor.execute(q)
        conn.commit()
    else:
        print("No employee record found with that employee number")

def show():
    cursor.execute('select * from employee')
    data=cursor.fetchall()
    for row in data:
        print(*row)

if conn.is_connected():
    print(create())
    x=int(input("Enter the employee number for updating:"))
    update(x)
    show()
