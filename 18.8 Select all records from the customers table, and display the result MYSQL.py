#Select all records from the "customers" table, and display the result

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="********",
  database="python_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)