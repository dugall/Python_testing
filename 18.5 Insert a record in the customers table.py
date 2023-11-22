#Insert a value into the table:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*****",
  database="python_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit() #to actually commit changes

print(mycursor.rowcount, "record inserted.")

