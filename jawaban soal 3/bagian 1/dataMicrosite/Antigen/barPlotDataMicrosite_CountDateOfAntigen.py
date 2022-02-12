import matplotlib.pyplot as plt
from matplotlib import style
import mysql.connector

style.use('ggplot')
fig, ax = plt.subplots(constrained_layout=True)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_microsite"
)

if mydb.is_connected():
    print("Berhasil terhubung ke database")

mycursor = mydb.cursor()
sql = "SELECT antigenDate, COUNT(antigenDate) AS CountDateOfAntigen FROM user GROUP BY antigenDate ORDER BY antigenDate ASC"
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
        if  data[1] < 4000000:
            TempDate.append(lengthX)
            lengthX += 1
            Date.append(data[0].strftime("%Y/%m/%d"))
            Count.append(data[1])


ax.bar(TempDate, Count, align="center")
plt.xticks(rotation=90)

ax.set_title('Grafik Antigen')
ax.set_ylabel('Pengguna')
ax.set_xlabel('Date')

ax.set_xticks(TempDate)
ax.set_xticklabels(Date)

plt.show()