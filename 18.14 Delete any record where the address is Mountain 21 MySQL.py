#Delete any record where the address is "Mountain 21"

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*******",
  database="python_db"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

#Escape values by using the placeholder %s method:
#sql = "DELETE FROM customers WHERE address = %s"
#adr = ("Yellow Garden 2", )

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")