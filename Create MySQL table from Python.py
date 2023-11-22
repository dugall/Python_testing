#Create MySQL table from Python

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='********')

    mySql_Create_Table_Query = """CREATE TABLE Hospital ( 
                            Hospital_Id INT UNSIGNED NOT NULL, 
    						Hospital_Name TEXT NOT NULL, 
    						Bed_Count INT, 
    						PRIMARY KEY (Hospital_Id) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Hospital Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")