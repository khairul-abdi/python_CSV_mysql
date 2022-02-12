from re import L
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib import style
import mysql.connector

style.use('ggplot')
fig, ax = plt.subplots(constrained_layout=True)
plt.xticks(rotation=90)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_dataHealth"
)

if mydb.is_connected():
    print("Berhasil terhubung ke database")

mycursor = mydb.cursor()

sql = "SELECT updatedAt , COUNT(updatedAt) AS CountDateOfDataScanPeduliLindungi FROM user_scanPeduliLindungi GROUP BY updatedAt ORDER BY updatedAt"
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
        if data[1] > 1000: 
            TempDate.append(lengthX)
            lengthX += 1
            Date.append(data[0])
            Count.append(data[1])

X_axis = np.arange(len(TempDate))
ax.bar(TempDate, Count, align='center')

ax.set_title('Grafik Scan Peduli Lindungi')
ax.set_ylabel('Pengguna')
ax.set_xlabel('Date')

ax.set_xticks(X_axis, TempDate)
ax.set_xticklabels(Date)

plt.show()