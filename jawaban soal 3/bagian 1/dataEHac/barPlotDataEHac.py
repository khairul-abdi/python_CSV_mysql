from re import L
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib import style
import mysql.connector

style.use('ggplot')
fig, ax = plt.subplots(constrained_layout=True)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_dataHealth"
)

if mydb.is_connected():
    print("Berhasil terhubung ke database")

mycursor = mydb.cursor()

sql = "SELECT updatedAt , COUNT(updatedAt) AS CountDateOfDataEHAC FROM user_ehac GROUP BY updatedAt ORDER BY updatedAt"
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
        if data[1] > 400: 
            TempDate.append(lengthX)
            lengthX += 1
            Date.append(data[0])
            Count.append(data[1])

X_axis = np.arange(len(TempDate))
ax.bar(TempDate, Count, align='center')
plt.xticks(rotation=90)

ax.set_title('Grafik Data EHac')
ax.set_ylabel('Pengguna')
ax.set_xlabel('Date')

ax.set_xticks(X_axis, TempDate)
ax.set_xticklabels(Date)

plt.show()