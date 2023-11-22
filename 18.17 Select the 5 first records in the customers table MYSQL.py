#Select the 5 first records in the "customers" table

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="########",
  database="python_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)