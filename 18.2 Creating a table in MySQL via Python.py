#Creating a table in MySQL via Python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="******",
  database="python_db"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

