"""Write a program to display the content of rows in reverse order from the file
“patient.csv”.
"""
import csv
f=open('patient.csv','r',newline='')
rdr=csv.reader(f)
for i in rdr:
    print(*i[::-1])
f.close()
