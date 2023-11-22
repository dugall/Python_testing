#Overwrite the address column from "Valley 345" to "Canyon 123"

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="********",
  database="python_db"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

#sql = "UPDATE customers SET address = %s WHERE address = %s"
#val = ("Valley 345", "Canyon 123")
#mycursor.execute(sql, val)

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")