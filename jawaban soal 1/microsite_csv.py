import mysql.connector
import csv
import datetime
import os
import uuid

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
      i = 0

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
          print("load...", i)
          i+= 1
        status = 1
  print("Data berhasil di import!") 

def insert_data(mydb):
  TrimUUID        = uuid.uuid4().hex[:20]
  
  sid             = TrimUUID
  userId          = uuid.uuid4()
  place           = input("Masukkan place: ")
  swabDate        = input("Masukkan swabDate (YYYY/MM/DD): ")
  swabResult      = input("Masukkan swabResult: ")
  swabHospital    = input("Masukkan swabHospital: ")
  swabValid       = num_input(input("Masukkan swabValid (True/False): "), "swabValid")
  antigenDate     = input("Masukkan antigenDate (YYYY/MM/DD): ")
  antigenResult   = input("Masukkan antigenResult: ")
  antigenHospital = input("Masukkan antigenHospital: ")
  antigenValid    = num_input(input("Masukkan antigenValid (True/False): "), "antigenValid")
  flightStatus    = num_input(input("Masukkan flightStatus (True/False): "), "flightStatus")
  createdAt       = formatDate("")
  updatedAt       = formatDate("")

  val = (sid, userId, place, swabDate, swabResult, swabHospital, swabValid, antigenDate, antigenResult, antigenHospital, antigenValid, flightStatus, createdAt, updatedAt)
  sql = "INSERT INTO user (sid, userId, place, swabDate, swabResult, swabHospital, swabValid, antigenDate, antigenResult, antigenHospital, antigenValid, flightStatus, createdAt, updatedAt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  mycursor = mydb.cursor()
  mycursor.execute(sql,val)
  mydb.commit()
  print("{} data berhasil disimpan".format(mycursor.rowcount))

def num_input(strWord, field): 
  try:
    n = int(validateBool(strWord))
    if n == 0 or n == 1:
      return n
    else:
      print("Masukkan input yang benar, besar kecil berpengaruh")
      if field == "swabValid":
        num_input(input("Masukkan swabValid (True/False): "), "swabValid")
      elif field == "antigenValid":
        num_input(input("Masukkan antigenValid (True/False): "), "antigenValid")
      elif field == "flightStatus":
        num_input(input("Masukkan flightStatus (True/False): "), "flightStatus")
  except:
    print("Masukkan input yang benar, besar kecil berpengaruh")
    if field == "swabValid":
      num_input(input("Masukkan swabValid (True/False): "), "swabValid")
    elif field == "antigenValid":
      num_input(input("Masukkan antigenValid (True/False): "), "antigenValid")
    elif field == "flightStatus":
      num_input(input("Masukkan flightStatus (True/False): "), "flightStatus")

def validateBool(strWord):
  if strWord == "True":
    return 1
  elif strWord == "False":
    return 0
  else:
    return "Salah input perhatikan besar kecil"

def formatDate(inputDate):
  # untuk convert format TAHUN-BULAN-TGL
  x = datetime.datetime.now()
  inputStr = str(x.year)+"/"+str(x.month)+"/"+str(x.day)
  format = '%Y/%m/%d'

  if inputDate != "":
    return datetime.datetime.strptime(inputDate, format).date()
  else:
    return datetime.datetime.strptime(inputStr, format).date()

def show_data(mydb):
  mycursor = mydb.cursor()
  sql = "SELECT * FROM user"
  mycursor.execute(sql)
  results = mycursor.fetchall()
  
  if mycursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def update_data(mydb):
  mycursor = mydb.cursor()
  show_data(mydb)
  userId          = input("pilih id user> ")

  sid             = input("sid baru: ")
  place           = input("place baru: ")
  swabDate        = formatDate(input("swabDate baru (YYYY/MM/DD): "))
  swabResult      = input("swabResult baru: ")
  swabHospital    = input("swabHospital baru: ")
  swabValid       = input("swabValid baru: ")
  antigenDate     = formatDate(input("antigenDate baru (YYYY/MM/DD): "))
  antigenResult   = input("antigenResult baru: ")
  antigenHospital = input("antigenHospital baru: ")
  antigenValid    = input("antigenValid baru: ")
  flightStatus    = input("flightStatus baru: ")
  updatedAt       = formatDate("")

  sql = "UPDATE user SET sid=%s, place=%s, swabDate=%s, swabResult=%s, swabHospital=%s, swabValid=%s, antigenDate=%s, antigenResult=%s, antigenHospital=%s, antigenValid=%s, flightStatus=%s, updatedAt=%s, WHERE userId=%s"
  val = (sid, place, swabDate, swabResult, swabHospital, swabValid, antigenDate, antigenResult, antigenHospital, antigenValid, flightStatus, updatedAt, userId)
  mycursor.execute(sql, val)
  mydb.commit()
  print("{} data berhasil diubah".format(mycursor.rowcount))

def delete_data(mydb):
  mycursor = mydb.cursor()
  show_data(mydb)
  user_id = input("pilih id user> ")
  sql = "DELETE FROM user WHERE userId=%s"
  val = (user_id,)
  mycursor.execute(sql, val)
  mydb.commit()
  print("{} data berhasil dihapus".format(mycursor.rowcount))

def search_data(mydb):
  mycursor = mydb.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM user WHERE sid LIKE %s OR userId LIKE %s OR place LIKE %s OR swabDate LIKE %s OR swabResult LIKE %s OR swabHospital LIKE %s OR swabValid LIKE %s OR antigenDate LIKE %s OR antigenResult LIKE %s OR antigenHospital LIKE %s OR antigenValid LIKE %s OR flightStatus LIKE %s OR createdAt LIKE %s OR updatedAt LIKE %s" 
  val = ("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword))
  mycursor.execute(sql, val)
  results = mycursor.fetchall()
  
  if mycursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(mydb):
  print("=== APLIKASI DATABASE PYTHON MICROSITE===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("6. Create Table")
  print("7. Import Data from CSV")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(mydb)
  elif menu == "2":
    show_data(mydb)
  elif menu == "3":
    update_data(mydb)
  elif menu == "4":
    delete_data(mydb)
  elif menu == "5":
    search_data(mydb)
  elif menu == "6":
    create_table(mydb)
  elif menu == "7":
    import_data(mydb)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(mydb)