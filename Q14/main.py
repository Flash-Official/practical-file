"""Write a program to display the record of those patients whose cholesterol is
more than 250 and Resting BP is less than 125 from a file the “patient.csv”."""
import csv
f=open('patient.csv','r',newline="")
rdr=csv.reader(f)
for i in rdr:
    if int(i[4])>250 and int(i[3])<125:
        print(*i)
f.close()
