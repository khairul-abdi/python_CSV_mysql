import mysql.connector
import csv
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_dataHealth"
)

def create_table(mydb):
  try:
    sql = """
      CREATE TABLE `user_scanPeduliLindungi`
      (
        `idUserScanPedung` INTEGER NOT NULL AUTO_INCREMENT,
        `sid` VARCHAR(255),
        `userId` VARCHAR(255),
        `user_status` VARCHAR(255),
        `checkInTime` VARCHAR(255),
        `checkOutTime` VARCHAR(255),
        `place_name` VARCHAR(255),
        `place_categoryName` VARCHAR(255),
        `locationAddress` VARCHAR(255),
        `location_latitude` VARCHAR(255),
        `location_longitude` VARCHAR(255),
        `crowd` VARCHAR(255),
        `status` VARCHAR(255),
        `userStatus` VARCHAR(255),
        `updatedAt` DATE,
        `createdAt` DATE,
        PRIMARY KEY `inst_ID`(`idUserScanPedung`)
      ) ENGINE = INNODB DEFAULT CHARSET = utf8;
    """
    
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    print("Tabel user_scanPeduliLindungi berhasil dibuat!")
  except mysql.connector.ProgrammingError as err:
    print("Tabel sudah di buat!") 

def import_data(mydb):
  with open("dataScanPeduliLindungi.csv", newline='') as csv_file:
      csv_reader= csv.reader(csv_file, delimiter=",")
      status = 0
      i = 0
      for row in csv_reader:
        if status != 0:
         
          sql = "INSERT INTO `db_dataHealth`.`user_scanPeduliLindungi` (`sid`,`userId`,`user_status`,`checkInTime`,`checkOutTime`,`place_name`,`place_categoryName`,`locationAddress`,`location_latitude`,`location_longitude`,`crowd`,`status`,`userStatus`,`updatedAt`,`createdAt`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          mycursor = mydb.cursor()
          mycursor.execute(sql,row)
          mydb.commit()
          print("load...", i)
          i+= 1
        status = 1

  print("Data berhasil di import!") 

def show_menu(mydb):
  print("=== APLIKASI DATABASE PYTHON DATA SCAN PEDULI LINDUNGI ===")
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