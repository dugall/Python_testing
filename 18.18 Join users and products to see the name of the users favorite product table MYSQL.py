#Join users and products to see the name of the users favorite product

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="!@!!@####",
  database="python_db"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)