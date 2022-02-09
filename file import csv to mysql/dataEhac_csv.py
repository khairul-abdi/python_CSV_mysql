import mysql.connector
import csv
import datetime
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_microsite"
)

def create_table(mydb):
  try:
    sql = """
    CREATE TABLE `user` 
    (    
      `idUser` INTEGER NOT NULL AUTO_INCREMENT ,
      `sid` VARCHAR( 255 ) ,
      `userId` VARCHAR( 255 ) ,
      `place` VARCHAR( 255 ) ,
      `swabDate` DATE ,
      `swabResult` VARCHAR( 255 ) ,
      `swabHospital` VARCHAR( 255 ) ,
      `swabValid` BOOLEAN,
      `antigenDate` DATE ,
      `antigenResult` VARCHAR( 255 ) ,
      `antigenHospital` VARCHAR( 255 ) ,
      `antigenValid` BOOLEAN ,
      `flightStatus` BOOLEAN ,
      `createdAt` DATE ,
      `updatedAt` DATE, 
      PRIMARY KEY `inst_ID`(`idUser`)
    ) ENGINE = INNODB DEFAULT CHARSET = utf8;
    """
    
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    print("Tabel user berhasil dibuat!")
  except mysql.connector.ProgrammingError as err:
    print("Tabel sudah di buat!") 

def import_data(mydb):
  with open("dataMicrosite.csv", newline='') as csv_file:
      csv_reader= csv.reader(csv_file, delimiter=",")
      status = 0
      for row in csv_reader:
        if status != 0:

          if row[6].lower() == "true":
            row[6] = 1
          elif row[6].lower() == "false":
            row[6] = 0

          if row[10].lower() == "true":
            row[10] = 1
          elif row[10].lower() == "false":
            row[10] = 0

          if row[11].lower() == "true":
            row[11] = 1
          elif row[11].lower() == "false":
            row[11] = 0

          sql = "INSERT INTO `db_microsite`.`user` (`sid`,`userId`,`place`,`swabDate`,`swabResult`,`swabHospital`,`swabValid`,`antigenDate`,`antigenResult`,`antigenHospital`,`antigenValid`,`flightStatus`,`createdAt`,`updatedAt`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          mycursor = mydb.cursor()
          mycursor.execute(sql,row)
          mydb.commit()
        status = 1
  print("Data berhasil di import!") 

def show_menu(mydb):
  print("=== APLIKASI DATABASE PYTHON DATA EHAC ===")
  print("1. Create Table")
  print("2. Import Data from CSV")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    create_table(mydb)
  elif menu == "2":
    import_data(mydb)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(mydb)