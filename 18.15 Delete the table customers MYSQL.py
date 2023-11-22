#Delete the table "customers"

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*******",
  database="python_db"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)