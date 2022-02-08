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

sql = """
CREATE TABLE `user` 
(    
  `idUser` INTEGER NOT NULL AUTO_INCREMENT ,
  `sid` VARCHAR( 255 ) ,
  `userId` VARCHAR( 255 ) ,
  `place` VARCHAR( 255 ) ,
  `swabDate` VARCHAR( 255 ) ,
  `swabResult` VARCHAR( 255 ) ,
  `swabHospital` VARCHAR( 255 ) ,
  `swabValid` BOOLEAN,
  `antigenDate` VARCHAR( 255 ) ,
  `antigenResult` VARCHAR( 255 ) ,
  `antigenHospital` VARCHAR( 255 ) ,
  `antigenValid` BOOLEAN ,
  `flightStatus` BOOLEAN ,
  `createdAt` VARCHAR( 255 ) ,
  `updatedAt` VARCHAR( 255 ), 
  PRIMARY KEY `inst_ID`(`idUser`)
) ENGINE = INNODB DEFAULT CHARSET = utf8;
"""

mycursor.execute(sql)

print("Tabel customers berhasil dibuat!")

with open("dataMicrosite.csv", newline='') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    status = 0
    for row in csv_reader:
      if status != 0: 
        swabValid = row[6]
        antigenValid = row[10]
        flightStatus = row[11]

        if swabValid == 'true' or antigenValid == 'true' or  flightStatus == 'true'  :
          row[6] = 1
          row[10] = 1
          row[11] = 1

        if swabValid == 'true' or antigenValid == 'true' or  flightStatus == 'true'  :
          row[6] = 0
          row[10] = 0
          row[11] = 0
        sql = "INSERT INTO `db_microsite`.`user` (`sid`,`userId`,`place`,`swabDate`,`swabResult`,`swabHospital`,`swabValid`,`antigenDate`,`antigenResult`,`antigenHospital`,`antigenValid`,`flightStatus`,`createdAt`,`updatedAt`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,row)
      status = 1

mydb.commit()
mydb.close()