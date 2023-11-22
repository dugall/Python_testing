#Table existance 

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="******",
  database="python_db"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print("THere are the next tables:", x)