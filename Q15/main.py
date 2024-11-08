"""Write a program to display the Blood sugar of those patients whose name
either starting with ‘O’ or ending with ‘r’ and Age is more than 70 from file
the“patient.csv”"""
import csv
f=open('patient.csv','r',newline='')
rdr=csv.reader(f)
for i in rdr:
    if (i[0][0].lower()=="o" or i[0][-1].lower()=='r') and int(i[1])>=70:
        print(f"Name:{i[0]}\nAge:{i[1]}\nBlood Sugar:{i[5]}")
f.close()
