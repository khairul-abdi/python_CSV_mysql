from re import L
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib import style
import mysql.connector
import copy

def DataFromDB(alias, table):
    sql = "SELECT updatedAt , COUNT(updatedAt) AS "+ alias +" FROM "+ table +" GROUP BY updatedAt ORDER BY updatedAt"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    Date = []
    TempDate = []
    lengthX = 0
    Count = []

    if mycursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            if data[1] < 200: 
                TempDate.append(lengthX)
                lengthX += 1
                Date.append(data[0])
                Count.append(data[1])

    return Date, TempDate, Count

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_dataHealth"
)

if mydb.is_connected():
    print("Berhasil terhubung ke database")

mycursor = mydb.cursor()

resultDataEHac = DataFromDB("CountDateOfDataEHAC", "user_ehac")
resultDataPeduliLindungi = DataFromDB("CountDateOfDataScanPeduliLindungi", "user_scanPeduliLindungi")

dateAll      = []

dateEHac     = resultDataEHac[0]
tempDateEHac = resultDataEHac[1]
CountEHac    = resultDataEHac[2]

datePeduliLindungi      = resultDataPeduliLindungi[0]
tempDatePeduliLindungi  = resultDataPeduliLindungi[1]
CountPeduliLindungi     = resultDataPeduliLindungi[2]

dateAll = copy.deepcopy(dateEHac)
for data in datePeduliLindungi:
    dateAll.append(data)

dateAll = sorted(dateAll)

idxSameDate = []
for idx in range(len(dateAll)-1):
    if dateAll[idx] == dateAll[idx+1]:
        idxSameDate.append(idx)

for idx in idxSameDate:
    dateAll.pop(idx)

dateEHacNew = []
for idx in dateAll:
    isFound = True
    for idy in range(len(dateEHac)):
        if dateEHac[idy] == idx:
            isFound = False
            dateEHacNew.append(CountEHac[idy])

    if isFound:
        dateEHacNew.append(0)

datePeduliLindungiNew = []
for idx in dateAll :
    isFound = True
    for idy in range(len(datePeduliLindungi)):
        if datePeduliLindungi[idy] == idx:
            isFound = False
            datePeduliLindungiNew.append(CountPeduliLindungi[idy])

    if isFound:
        datePeduliLindungiNew.append(0)

# CONTOH AJA
# datePeduliLindungiNew[12] = 2019
# datePeduliLindungiNew[13] = 4963
# datePeduliLindungiNew[14] = 4640
# datePeduliLindungiNew[15] = 2701

# print("datePeduliLindungiNew => ",len(datePeduliLindungiNew), datePeduliLindungiNew)
# print("dateEHacNew => ",len(dateEHacNew), dateEHacNew)

X_axis = np.arange(len(dateAll))

plt.subplots(constrained_layout=True)

plt.bar(X_axis - 0.2, dateEHacNew, 0.4, label = 'Data EHac')
plt.bar(X_axis + 0.2, datePeduliLindungiNew, 0.4, label = 'Data Scan Peduli Lindungi')

plt.title('Grafik EHac & Scan Peduli Lindungi')
plt.ylabel('Pengguna')
plt.xlabel('Date')

plt.xticks(X_axis, dateAll)
plt.xticks(rotation=90)
plt.legend()
plt.show()

