#Select only the name and address columns

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*******",
  database="python_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#If you are only interested in one row, you can use the fetchone() method.
#The fetchone() method will return the first row of the result:
#myresult = mycursor.fetchone()