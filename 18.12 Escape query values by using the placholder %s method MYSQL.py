#Escape query values by using the placholder %s method

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*******",
  database="python_db"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)