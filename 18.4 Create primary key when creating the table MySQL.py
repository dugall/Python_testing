#Create primary key when and after creating a table:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*******",
  database="python_db"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

