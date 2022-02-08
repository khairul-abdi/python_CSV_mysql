from ast import In
import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_microsite"
)

mycursor = mydb.cursor()
with open("contacts.csv", newline='') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    i = 0
    for row in csv_reader:
        if i != 0:
            sql = "INSERT INTO `db_scv_python`.`user` (`sid`, `nama`,`telepon`) VALUES (%s,%s,%s)"
            mycursor.execute(sql,row)
        i = 1

mydb.commit()
mydb.close()