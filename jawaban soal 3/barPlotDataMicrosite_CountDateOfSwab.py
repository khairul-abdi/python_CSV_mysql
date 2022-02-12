import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_microsite"
)

if mydb.is_connected():
    print("Bershasil terhubung ke database")

mycursor = mydb.cursor()
sql = "SELECT swabDate, COUNT(swabDate) AS CountDateOfSwab FROM user GROUP BY swabDate ORDER BY swabDate ASC"
mycursor.execute(sql)
results = mycursor.fetchall()

Date = []
Count = []
if mycursor.rowcount < 0:
    print("Tidak ada data")
else:
    for data in results:
        print(data[0])
        Date.append(data[0].strftime("%Y/%m/%d"))
        Count.append(data[1])

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(Date,Count)
plt.show()