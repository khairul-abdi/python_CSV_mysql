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
      CREATE TABLE  `user_ehac` 
      (
        `idUserEhac`INTEGER NOT NULL AUTO_INCREMENT ,
        `sid` VARCHAR(255),
        `createdBy_userId` VARCHAR(255),
        `createdAt` DATE,
        `createdBy_status` VARCHAR(255),
        `healthDeclaration_hospitalName` VARCHAR(255),
        `healthDeclaration_visitedCountry` VARCHAR(255),
        `healthDeclaration_symptoms` VARCHAR(255),
        `personalDetail_travelPurpose` VARCHAR(255),
        `personalDetail_passportCountry` VARCHAR(255),
        `personalDetail_citizen` VARCHAR(255),
        `personalDetail_gender` VARCHAR(255),
        `personalDetail_bornDate` VARCHAR(255),
        `scan_latitude` VARCHAR(255),
        `scan_longitude` VARCHAR(255),
        `travelDetail_transportation_vehicleType` VARCHAR(255),
        `travelDetail_destination_cityName` VARCHAR(255),
        `travelDetail_destination_provinceName` VARCHAR(255),
        `travelDetail_origin_cityName` VARCHAR(255),
        `travelDetail_origin_provinceName` VARCHAR(255),
        `typeEhac` VARCHAR(255),
        `updatedAt` DATE,
        PRIMARY KEY `inst_ID`(`idUserEhac`)
      ) ENGINE = INNODB DEFAULT CHARSET = utf8;
    """
    
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    print("Tabel user berhasil dibuat!")
  except mysql.connector.ProgrammingError as err:
    print("Tabel sudah di buat!") 

def import_data(mydb):
  with open("dataEHac.csv", newline='') as csv_file:
      csv_reader= csv.reader(csv_file, delimiter=",")
      i = 0
      for row in csv_reader:
        if i != 0:
         
          if row[2][2] == "/":
            dataSplit = row[3].split("/")
            row[2] = str(dataSplit[2])+"/"+str(dataSplit[1])+"/"+str(dataSplit[0])

          sql = "INSERT INTO `db_dataHealth`.`user_ehac` (`sid`, `createdBy_userId`, `createdAt`, `createdBy_status`, `healthDeclaration_hospitalName`, `healthDeclaration_visitedCountry`, `healthDeclaration_symptoms`, `personalDetail_travelPurpose`, `personalDetail_passportCountry`, `personalDetail_citizen`, `personalDetail_gender`, `personalDetail_bornDate`, `scan_latitude`, `scan_longitude`, `travelDetail_transportation_vehicleType`, `travelDetail_destination_cityName`, `travelDetail_destination_provinceName`, `travelDetail_origin_cityName`, `travelDetail_origin_provinceName`, `typeEhac`, `updatedAt`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          mycursor = mydb.cursor()
          mycursor.execute(sql,row)
          mydb.commit()
          print("Load ... ", i)
        i+= 1

  print("Data berhasil di import!") 

def show_menu(mydb):
  print("=== APLIKASI DATABASE PYTHON DATA Peduli Lindungi ===")
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