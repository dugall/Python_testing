#Select record(s) where the address is "Park Lane 38": result

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*******",
  database="python_db"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)