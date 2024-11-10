"""Write a Program to connect with database and search a record from
employee table (empno, empname, department, salary) based on empno and
display records.
"""

import mysql.connector as sql

conn=sql.connect(host="localhost",user="root",password="",database="employee")
# def create():
#     cursor.execute("""create table if not exists employee(
#                     empno INT PRIMARY KEY,
#                     name  varchar(25),
#                     dep varchar(25),
#                     salary INT
#                     )""")
#     conn.commit()
#     return "Table Created"
def search(epmno):
    cursor.execute(f'select * from employee where empno={epmno}')
    data=cursor.fetchall()
    for row in data:
        print(*row)

if conn.is_connected():
    cursor=conn.cursor()
    create()
    x=int(input("Enter the number employee number:"))
    search(x)
