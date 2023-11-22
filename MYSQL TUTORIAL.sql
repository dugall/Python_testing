1) The following SQL statement selects all the records in the "Customers" table:

SELECT * FROM Customers;

2) Some of The Most Important SQL Commands

SELECT - extracts data from a database
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index

3) Getting data
SELECT * FROM table_name;
SELECT CustomerName, City, Country FROM Customers;
SELECT Country FROM Customers;

4) SELECT DISTINCT Examples

SELECT DISTINCT Country FROM Customers;
SELECT COUNT(DISTINCT Country) FROM Customers;
#count unique countries

5) WHERE
SELECT * FROM Customers
WHERE Country = 'Mexico';

SELECT * FROM Customers
WHERE CustomerID = 1;

6) AND, OR and NOT Operators

SELECT * FROM Customers
WHERE Country = 'Germany' AND City = 'Berlin';

SELECT * FROM Customers
WHERE City = 'Berlin' OR City = 'Stuttgart';

SELECT * FROM Customers
WHERE Country = 'Germany' OR Country = 'Spain';

SELECT * FROM Customers
WHERE NOT Country = 'Germany';

SELECT * FROM Customers
WHERE Country = 'Germany' AND (City = 'Berlin' OR City = 'Stuttgart');

SELECT * FROM Customers
WHERE NOT Country = 'Germany' AND NOT Country = 'USA';

7) MySQL ORDER BY Keyword

SELECT * FROM Customers
ORDER BY Country;

SELECT * FROM Customers
ORDER BY Country DESC;

SELECT * FROM Customers
ORDER BY Country, CustomerName;
#if some rows have the same Country, it orders them by CustomerName

SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;

8) MySQL INSERT INTO Statement

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');

9) MySQL NULL Values

SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NULL;
#The IS NULL operator is used to test for empty values (NULL values).

SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NOT NULL;

10) UPDATE

UPDATE Customers
SET ContactName = 'Alfred Schmidt', City = 'Frankfurt'
WHERE CustomerID = 1;

UPDATE Customers
SET PostalCode = 00000
WHERE Country = 'Mexico';
#UPDATE Multiple Records

#Without where, all records will be updated

11) MySQL DELETE Statement

DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';

DELETE FROM Customers;
#deleting content in the table

12) MySQL LIMIT Clause

SELECT column_name(s) FROM table_name WHERE condition LIMIT number;
#syntax

SELECT * FROM Customers
LIMIT 3;

SELECT * FROM Customers
LIMIT 3 OFFSET 3;

#What if we want to select records 4 - 6 (inclusive)?
#MySQL provides a way to handle this: by using OFFSET.
#The SQL query below says "return only 3 records,
#start on record 4 (OFFSET 3)"

SELECT * FROM Customers
WHERE Country='Germany'
LIMIT 3;

13) MySQL MIN() and MAX() Functions

SELECT MIN(Price) AS SmallestPrice
FROM Products;

SELECT MAX(Price) AS LargestPrice
FROM Products;

14) MySQL COUNT(), AVG() and SUM() Functions

SELECT COUNT(ProductID)
FROM Products;

SELECT AVG(Price)
FROM Products;
#Note: NULL values are ignored.

SELECT SUM(Quantity)
FROM OrderDetails;

15) MySQL LIKE Operator

#There are two wildcards often used in conjunction with the LIKE operator:
#The percent sign (%) represents zero, one, or multiple characters
#The underscore sign (_) represents one, single character

#WHERE CustomerName LIKE 'a%'
#Finds any values that start with "a"
#WHERE CustomerName LIKE '%a'
#Finds any values that end with "a"
#WHERE CustomerName LIKE '%or%'
#Finds any values that have "or" in any position
#WHERE CustomerName LIKE '_r%'
#Finds any values that have "r" in the second position
#WHERE CustomerName LIKE 'a_%'
#Finds any values that start with "a" and are at least 2 characters in length
#WHERE CustomerName LIKE 'a__%'
#Finds any values that start with "a" and are at least 3 characters in length
#WHERE ContactName LIKE 'a%o'
#Finds any values that start with "a" and ends with "o"

SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';

SELECT * FROM Customers
WHERE CustomerName LIKE '%a';

SELECT * FROM Customers
WHERE CustomerName LIKE '%or%';

SELECT * FROM Customers
WHERE CustomerName LIKE '_r%';

SELECT * FROM Customers
WHERE CustomerName LIKE 'a__%';

SELECT * FROM Customers
WHERE ContactName LIKE 'a%o';

SELECT * FROM Customers
WHERE CustomerName NOT LIKE 'a%';

16) MySQL Wildcard Characters

#%	Represents zero or more characters	bl% finds bl, black, blue, and blob
#_	Represents a single character	h_t finds hot, hat, and hit

SELECT * FROM Customers
WHERE City LIKE 'ber%';

SELECT * FROM Customers
WHERE City LIKE '%es%';

SELECT * FROM Customers
WHERE City LIKE '_ondon';

SELECT * FROM Customers
WHERE City LIKE 'L_n_on';

17) MySQL IN Operator

SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');
#selects all customers that are located in "Germany", "France" or "UK"

SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');

SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);
#selects all customers that are from the same countries as the suppliers

18) MySQL BETWEEN Operator

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;

SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID NOT IN (1,2,3);

SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;

SELECT * FROM Products
WHERE ProductName BETWEEN "Carnarvon Tigers" AND "Chef Anton's Cajun Seasoning"
ORDER BY ProductName;

SELECT * FROM Products
WHERE ProductName NOT BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;

SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';

19) MySQL Aliases
#An alias (nickname) is created with the AS keyword.

SELECT column_name AS alias_name
FROM table_name;
#syntax

SELECT column_name(s)
FROM table_name AS alias_name;
#syntax

SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;

SELECT CustomerName AS Customer, ContactName AS "Contact Person"
FROM Customers;

SELECT CustomerName, CONCAT_WS(', ', Address, PostalCode, City, Country) AS Address
FROM Customers;
#creates an alias named "Address" that combine four columns (Address, PostalCode, City and Country)

SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName='Around the Horn' AND c.CustomerID=o.CustomerID;
#selects all the orders from the customer with CustomerID=4 (Around the Horn).
#We use the "Customers" and "Orders" tables,
#and give them the table aliases of "c" and "o" respectively
#(Here we use aliases to make the SQL shorter)

SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerName
FROM Customers, Orders
WHERE Customers.CustomerName='Around the Horn' AND Customers.CustomerID=Orders.CustomerID;
#The following SQL statement is the same as above, but without aliases:

20) MySQL Joining Tables

SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

#INNER JOIN: Returns records that have matching values in both tables
#LEFT JOIN: Returns all records from the left table, and the matched records from the right table
#RIGHT JOIN: Returns all records from the right table, and the matched records from the left table
#CROSS JOIN: Returns all records from both tables

SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
#syntax

SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
#The following SQL statement selects all orders with customer information

SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);
#The following SQL statement selects all orders with customer and shipper information

SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
#syntax

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;
#The following SQL statement will select all customers,
#and any orders they might have

SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
#syntax

SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;
#return all employees, and any orders they might have placed

SELECT column_name(s)
FROM table1
CROSS JOIN table2;
#cross join syntax

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
CROSS JOIN Orders;
#selects all customers, and all orders

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
CROSS JOIN Orders
WHERE Customers.CustomerID=Orders.CustomerID;
#If you add a WHERE clause (if table1 and table2 has a relationship),
#the CROSS JOIN will produce the same result as the INNER JOIN clause

SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
#T1 and T2 are different table aliases for the same table.
#selfjoin syntax

SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City
ORDER BY A.City;
#The following SQL statement matches customers that are from the same city

21) MySQL UNION Operator
#The UNION operator is used to combine the result-set of two or more SELECT statements

SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
#syntax

SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
#syntax

SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;
#If some customers or suppliers have the same city, each city will only be listed once,
#because UNION selects only distinct values.
#Use UNION ALL to also select duplicate values!

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;

SELECT 'Customer' AS Type, ContactName, City, Country
FROM Customers
UNION
SELECT 'Supplier', ContactName, City, Country
FROM Suppliers;
#SQL statement lists all customers and suppliers

22) MySQL GROUP BY Statement

#The GROUP BY statement groups rows that have the same values into summary rows,
#like "find the number of customers in each country"

#The GROUP BY statement is often used with aggregate functions
#(COUNT(), MAX(), MIN(), SUM(), AVG()) to group the result-set by one or more columns.

SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
#syntax

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;
#lists the number of customers in each country, sorted high to low

SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders
LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName;
#The following SQL statement lists the number of orders sent by each shipper

23) MySQL HAVING Clause

SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
#syntax

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;
#The following SQL statement lists the number of customers in each country.
#Only include countries with more than 5 customers

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5
ORDER BY COUNT(CustomerID) DESC;
#The following SQL statement lists the number of customers in each country,
#sorted high to low (Only include countries with more than 5 customers)

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM (Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 10;
#The following SQL statement lists the employees that have
#registered more than 10 orders:

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
WHERE LastName = 'Davolio' OR LastName = 'Fuller'
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 25;
#The following SQL statement lists if the employees "Davolio" or "Fuller"
#have registered more than 25 orders:

24) MySQL EXISTS Operator
#The EXISTS operator is used to test for the existence of any record in a subquery.
#The EXISTS operator returns TRUE if the subquery returns one or more records.

SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
#syntax

SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20);
#The following SQL statement returns TRUE and lists
#the suppliers with a product price less than 20:

SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price = 22);
#The following SQL statement returns TRUE and
#lists the suppliers with a product price equal to 22

25) MySQL ANY and ALL Operators
#The ANY and ALL operators allow you to perform a comparison
#between a single column value and a range of other values.

#The ANY operator:
#returns a boolean value as a result
#returns TRUE if ANY of the subquery values meet the condition

SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY
  (SELECT column_name
  FROM table_name
  WHERE condition);
#syntax
#The operator must be a standard comparison operator (=, <>, !=, >, >=, <, or <=).

SELECT ALL column_name(s)
FROM table_name
WHERE condition;

SELECT column_name(s)
FROM table_name
WHERE column_name operator ALL
  (SELECT column_name
  FROM table_name
  WHERE condition);
#syntax

SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);
#The following SQL statement lists the ProductName if it finds ANY records in
#the OrderDetails table has Quantity equal to 10
#(this will return TRUE because the Quantity column has some values of 10)

SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity > 99);
#The following SQL statement lists the ProductName
#if it finds ANY records in the OrderDetails table has Quantity larger
#than 99(this will return TRUE because the Quantity column
#has some values larger than 99):

SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity > 1000);
#The following SQL statement lists the ProductName if it finds ANY records
#in the OrderDetails table has Quantity larger than 1000
#(this will return FALSE because the Quantity column has no values larger than 1000)

SELECT ALL ProductName
FROM Products
WHERE TRUE;
#syntax

SELECT ProductName
FROM Products
WHERE ProductID = ALL
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);
#The following SQL statement lists the ProductName if ALL the records in the OrderDetails
#table has Quantity equal to 10. This will of course
#return FALSE because the Quantity column has many different values
#(not only the value of 10)

26) MySQL INSERT INTO SELECT Statement
#The INSERT INTO SELECT statement copies
#data from one table and inserts it into another table.
#The INSERT INTO SELECT statement requires that
#the data types in source and target tables matches.

INSERT INTO table2
SELECT * FROM table1
WHERE condition;
#syntax

INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;
#syntax

INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM Suppliers;
#The following SQL statement copies "Suppliers" into "Customers"
#(the columns that are not filled with data, will contain NULL)

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
SELECT SupplierName, ContactName, Address, City, PostalCode, Country FROM Suppliers;
#The following SQL statement copies "Suppliers" into "Customers" (fill all columns)

INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM Suppliers
WHERE Country='Germany';
#The following SQL statement copies only the German suppliers into "Customers"

27) MySQL CASE Statement
#The CASE statement goes through conditions and returns a value
#when the first condition is met (like an if-then-else statement).
#So, once a condition is true, it will stop reading and return the result.
#If no conditions are true, it returns the value in the ELSE clause.
#If there is no ELSE part and no conditions are true, it returns NULL.

CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
#syntax

SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;
#The following SQL goes through conditions and
#returns a value when the first condition is met:

SELECT CustomerName, City, Country
FROM Customers
ORDER BY
(CASE
    WHEN City IS NULL THEN Country
    ELSE City
END);
#The following SQL will order the customers by City.
#However, if City is NULL, then order by Country:

28) MySQL IFNULL() and COALESCE() Functions

SELECT ProductName, UnitPrice * (UnitsInStock + UnitsOnOrder)
FROM Products;
#In the example above, if any of the "UnitsOnOrder"
#values are NULL, the result will be NULL

SELECT ProductName, UnitPrice * (UnitsInStock + IFNULL(UnitsOnOrder, 0))
FROM Products;
#The MySQL IFNULL() function lets you return an alternative value if an expression is NULL.
#The example below returns 0 if the value is NULL

SELECT ProductName, UnitPrice * (UnitsInStock + COALESCE(UnitsOnOrder, 0))
FROM Products;

29) MySQL Operators
#https://www.w3schools.com/mysql/mysql_operators.asp

##############3

30) MySQL CREATE DATABASE Statement

CREATE DATABASE databasename;

31) MySQL DROP DATABASE Statement

DROP DATABASE databasename;
#deleting DB

32) MySQL CREATE TABLE Statement

CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
#syntax

CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

33) Create Table Using Another Table

CREATE TABLE new_table_name AS
    SELECT column1, column2,...
    FROM existing_table_name
    WHERE ....;
#syntax

CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers;
#The following SQL creates a new table called "TestTables" (which is a copy of the "Customers" table)

34) MySQL DROP TABLE Statement

#The DROP TABLE statement is used to drop an existing table in a database.

DROP TABLE table_name;
#syntax

35) MySQL TRUNCATE TABLE

#The TRUNCATE TABLE statement is used to delete the data inside a table, but not the table itself.

TRUNCATE TABLE table_name;
#syntax

36) MySQL ALTER TABLE Statement

#The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.

ALTER TABLE table_name
ADD column_name datatype;
#syntax

ALTER TABLE Customers
ADD Email varchar(255);


ALTER TABLE table_name
DROP COLUMN column_name;
#syntax
#ALTER TABLE - DROP COLUMN

ALTER TABLE Customers
DROP COLUMN Email;

ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
#syntax
#ALTER TABLE - MODIFY COLUMN

ALTER TABLE Persons
ADD DateOfBirth date;
#applying data type

ALTER TABLE Persons
DROP COLUMN DateOfBirth;
#delete the column

37) MySQL Constraints

#Constraints can be specified when the table is created with the CREATE TABLE statement,
#or after the table is created with the ALTER TABLE statement.

CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
    ....
);
#syntax

#The following constraints are commonly used in SQL:

#NOT NULL - Ensures that a column cannot have a NULL value
#UNIQUE - Ensures that all values in a column are different
#PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
#FOREIGN KEY - Prevents actions that would destroy links between tables
#CHECK - Ensures that the values in a column satisfies a specific condition
#DEFAULT - Sets a default value for a column if no value is specified
#CREATE INDEX - Used to create and retrieve data from the database very quickly

38) MySQL NOT NULL Constraint

#By default, a column can hold NULL values.
#The NOT NULL constraint enforces a column to NOT accept NULL values.

#The following SQL ensures that the "ID", "LastName",
#and "FirstName" columns will NOT accept NULL values
#when the "Persons" table is created:

CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Age int
);

#NOT NULL on ALTER TABLE

ALTER TABLE Persons
MODIFY Age int NOT NULL;

39) MySQL UNIQUE Constraint

#The UNIQUE constraint ensures that all values in a column are different.
#Both the UNIQUE and PRIMARY KEY constraints provide
#a guarantee for uniqueness for a column or set of columns.
#A PRIMARY KEY constraint automatically has a UNIQUE constraint.
#However, you can have many UNIQUE constraints per table,
#but only one PRIMARY KEY constraint per table.

#UNIQUE Constraint on CREATE TABLE
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    UNIQUE (ID)
);

#To name a UNIQUE constraint, and to define a UNIQUE constraint on
#multiple columns, use the following SQL syntax:

CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT UC_Person UNIQUE (ID,LastName)
);

#UNIQUE Constraint on ALTER TABLE
ALTER TABLE Persons
ADD UNIQUE (ID);

ALTER TABLE Persons
ADD CONSTRAINT UC_Person UNIQUE (ID,LastName);
#To name a UNIQUE constraint, and to define a UNIQUE constraint
#on multiple columns, use the following SQL syntax

#DROP a UNIQUE Constraint
ALTER TABLE Persons
DROP INDEX UC_Person;

40) MySQL PRIMARY KEY Constraint

#The PRIMARY KEY constraint uniquely
#identifies each record in a table.
#Primary keys must contain UNIQUE values,
#and cannot contain NULL values.
#A table can have only ONE primary key;
#and in the table, this primary key can consist
#of single or multiple columns (fields).

#PRIMARY KEY on CREATE TABLE
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);
#The following SQL creates a PRIMARY KEY on
#the "ID" column when the "Persons" table is created

CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT PK_Person PRIMARY KEY (ID,LastName)
);
#To allow naming of a PRIMARY KEY constraint, and
#for defining a PRIMARY KEY
#constraint on multiple columns, use the following SQL syntax

#In the example above there is only ONE PRIMARY KEY (PK_Person).
#However, the VALUE of the primary key is made up of TWO COLUMNS
#(ID + LastName).

#PRIMARY KEY on ALTER TABLE

ALTER TABLE Persons
ADD PRIMARY KEY (ID);

#To create a PRIMARY KEY constraint on 
#"ID" column when the table is already created

ALTER TABLE Persons
ADD CONSTRAINT PK_Person PRIMARY KEY (ID,LastName);
#To allow naming of a PRIMARY KEY constraint,
#and for defining a PRIMARY KEY constraint on multiple columns

#If you use ALTER TABLE to add a primary key, the primary key column(s)
#must have been declared to not contain NULL
#values (when the table was first created).

#DROP a PRIMARY KEY Constraint
ALTER TABLE Persons
DROP PRIMARY KEY;

41) MySQL FOREIGN KEY Constraint

#The FOREIGN KEY constraint is used to prevent actions
#that would destroy links between tables.

#A FOREIGN KEY is a field (or collection of fields) in one table,
#that refers to the PRIMARY KEY in another table.

#FOREIGN KEY on CREATE TABLE

CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
#creates a FOREIGN KEY on the "PersonID" column
#when the "Orders" table is created

CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    CONSTRAINT FK_PersonOrder FOREIGN KEY (PersonID)
    REFERENCES Persons(PersonID)
);

#To allow naming of a FOREIGN KEY constraint, and for defining a
#FOREIGN KEY constraint on multiple columns, use the following SQL syntax

#FOREIGN KEY on ALTER TABLE

ALTER TABLE Orders
ADD FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);
#To create a FOREIGN KEY constraint on the "PersonID"
#column when the "Orders" table is already created, use the following SQL

ALTER TABLE Orders
ADD CONSTRAINT FK_PersonOrder
FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);
#To allow naming of a FOREIGN KEY constraint, and for defining
#a FOREIGN KEY constraint on multiple columns

#DROP a FOREIGN KEY Constraint
ALTER TABLE Orders
DROP FOREIGN KEY FK_PersonOrder;

42) MySQL CHECK Constraint

#The CHECK constraint is used to limit the value range
#that can be placed in a column.

#If you define a CHECK constraint on a column
#it will allow only certain values for this column.

#If you define a CHECK constraint on a table
#it can limit the values in certain columns based on
#values in other columns in the row.

#CHECK on CREATE TABLE
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);
#The CHECK constraint ensures that the age of a person must be 18, or older

CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255),
    CONSTRAINT CHK_Person CHECK (Age>=18 AND City='Sandnes')
);

#To allow naming of a CHECK constraint, and for defining
#a CHECK constraint on multiple columns, use the following SQL syntax

#CHECK on ALTER TABLE
ALTER TABLE Persons
ADD CHECK (Age>=18);
#To create a CHECK constraint on
#the "Age" column when the table is already created

ALTER TABLE Persons
ADD CHECK (Age>=18);

ALTER TABLE Persons
ADD CONSTRAINT CHK_PersonAge CHECK (Age>=18 AND City='Sandnes');

#DROP a CHECK Constraint
ALTER TABLE Persons
DROP CHECK CHK_PersonAge;

43) MySQL DEFAULT Constraint

#The DEFAULT constraint is used to set a default value for a column.

#DEFAULT on CREATE TABLE
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255) DEFAULT 'Sandnes'
);

CREATE TABLE Orders (
    ID int NOT NULL,
    OrderNumber int NOT NULL,
    OrderDate date DEFAULT CURRENT_DATE()
);
#The DEFAULT constraint can also be used to
#insert system values, by using functions like CURRENT_DATE():

#DEFAULT on ALTER TABLE
ALTER TABLE Persons
ALTER City SET DEFAULT 'Sandnes';
#To create a DEFAULT constraint
#on the "City" column when the table is already created

#DROP a DEFAULT Constraint
ALTER TABLE Persons
ALTER City DROP DEFAULT;

44) MySQL CREATE INDEX Statement

#The CREATE INDEX statement is used to create indexes in tables.
#Indexes are used to retrieve data from the database more quickly
#than otherwise. The users cannot see the indexes,
#they are just used to speed up searches/queries.

CREATE INDEX index_name
ON table_name (column1, column2, ...);
#syntax
#Duplicate values are allowed

CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);
#CREATE UNIQUE INDEX Syntax

CREATE INDEX idx_lastname
ON Persons (LastName);
#The SQL statement below creates an index named
#"idx_lastname" on the "LastName" column in the "Persons" table

CREATE INDEX idx_pname
ON Persons (LastName, FirstName);
#to create an index on a combination of columns, you can list
#the column names within the parentheses, separated by commas

#DROP INDEX Statement
ALTER TABLE table_name
DROP INDEX index_name;

45) MySQL AUTO_INCREMENT

#Auto-increment allows a unique number to be generated
#automatically when a new record is inserted into a table.

#By default, the starting value for AUTO_INCREMENT is 1,
#and it will increment by 1 for each new record.

CREATE TABLE Persons (
    Personid int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (Personid)
);
#The following SQL statement defines the "Personid" column
#to be an auto-increment primary key field in the "Persons" table

ALTER TABLE Persons AUTO_INCREMENT=100;
#To let the AUTO_INCREMENT sequence start with another value

#When we insert a new record into the "Persons" table,
#we do NOT have to specify a value for the "Personid" column
#(a unique value will be added automatically)

46) MySQL Dates

#The most difficult part when working with dates is to be sure
#that the format of the date you are trying to insert,
#matches the format of the date column in the database.

#MySQL comes with the following data types for storing
#a date or a date/time value in the database
#DATE - format YYYY-MM-DD
#DATETIME - format: YYYY-MM-DD HH:MI:SS
#TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
#YEAR - format YYYY or YY

SELECT * FROM Orders WHERE OrderDate='2008-11-11'
#picking an order from a row with this data

#if we try to get the result using DATE from DATETIME column we don't receive it

47) MySQL CREATE VIEW Statement

#In SQL, a view is a virtual table based on the result-set of an SQL statement.
#A view contains rows and columns, just like a real table.
#The fields in a view are fields from one or more real tables in the database.
#You can add SQL statements and functions to a view and
#present the data as if the data were coming from one single table.

CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
#syntax

#A view always shows up-to-date data!
#The database engine recreates the view, every time a user queries it.

CREATE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName
FROM Customers
WHERE Country = 'Brazil';
#a view that shows all customers from Brazil

CREATE VIEW [Products Above Average Price] AS
SELECT ProductName, Price
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);
#selects every product in the "Products" table with a price higher than the average price

SELECT * FROM [Products Above Average Price];
#We can query the view above as follows

#MySQL Updating a View
#A view can be updated with the CREATE OR REPLACE VIEW statement.

CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
#syntax

CREATE OR REPLACE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName, City
FROM Customers
WHERE Country = 'Brazil';
#The following SQL adds the "City" column to the "Brazil Customers" view

DROP VIEW view_name;

DROP VIEW [Brazil Customers];

48) MySQL Data Types (Version 8.0)

# ========================================== String Data Types
#Data type	Description

CHAR(size)	#A FIXED length string (can contain letters,numbers, and special characters).
#The size parameter specifies the column length in characters - can be from 0 to 255.
#Default is 1

VARCHAR(size)	#A VARIABLE length string (can contain letters, numbers, and special characters).
#The size parameter specifies the maximum column length in characters - can be from 0 to 65535

BINARY(size)	#Equal to CHAR(), but stores binary byte strings. The size parameter specifies the column length in bytes. Default is 1
VARBINARY(size)	#Equal to VARCHAR(), but stores binary byte strings. The size parameter specifies the maximum column length in bytes.
TINYBLOB	#For BLOBs (Binary Large OBjects). Max length: 255 bytes
TINYTEXT	#Holds a string with a maximum length of 255 characters
TEXT(size)	#Holds a string with a maximum length of 65,535 bytes
BLOB(size)	#For BLOBs (Binary Large OBjects). Holds up to 65,535 bytes of data
MEDIUMTEXT	#Holds a string with a maximum length of 16,777,215 characters
MEDIUMBLOB	#For BLOBs (Binary Large OBjects). Holds up to 16,777,215 bytes of data
LONGTEXT	#Holds a string with a maximum length of 4,294,967,295 characters
LONGBLOB	#3For BLOBs (Binary Large OBjects). Holds up to 4,294,967,295 bytes of data

ENUM(val1, val2, val3, ...)	#A string object that can have only one value,
#chosen from a list of possible values. You can list up to 65535 values in an ENUM list.
#If a value is inserted that is not in the list, a blank value will be inserted. The values are sorted in the order you enter them

SET(val1, val2, val3, ...)	#A string object that can have 0 or more values, chosen from a list of possible values.
#You can list up to 64 values in a SET list

# ========================================== Numeric Data Types

BIT(size)	#A bit-value type. The number of bits per value is specified in size.
#The size parameter can hold a value from 1 to 64. The default value for size is 1.
TINYINT(size)	#A very small integer. Signed range is from -128 to 127. Unsigned range is from 0 to 255.
#The size parameter specifies the maximum display width (which is 255)
BOOL	#Zero is considered as false, nonzero values are considered as true.
BOOLEAN	#Equal to BOOL
SMALLINT(size)	#A small integer. Signed range is from -32768 to 32767. Unsigned range is from 0 to 65535.
#The size parameter specifies the maximum display width (which is 255)
MEDIUMINT(size)	#A medium integer. Signed range is from -8388608 to 8388607. Unsigned range is from 0 to 16777215.
#The size parameter specifies the maximum display width (which is 255)
INT(size)	#A medium integer. Signed range is from -2147483648 to 2147483647. Unsigned range is from 0 to 4294967295.
#The size parameter specifies the maximum display width (which is 255)
INTEGER(size)	#Equal to INT(size)
BIGINT(size)	#A large integer. Signed range is from -9223372036854775808 to 9223372036854775807.
#Unsigned range is from 0 to 18446744073709551615. The size parameter specifies the maximum display width (which is 255)
FLOAT(size, d)	#A floating point number. The total number of digits is specified in size.
#The number of digits after the decimal point is specified in the d parameter. This syntax is deprecated in MySQL 8.0.17, and it will be removed in future MySQL versions
FLOAT(p)	#A floating point number. MySQL uses the p value to determine whether to use FLOAT or DOUBLE for the resulting data type.
#If p is from 0 to 24, the data type becomes FLOAT(). If p is from 25 to 53, the data type becomes DOUBLE()
DOUBLE(size, d)	#A normal-size floating point number. The total number of digits is specified in size.
#The number of digits after the decimal point is specified in the d parameter
DOUBLE PRECISION(size, d)	 
DECIMAL(size, d)	#An exact fixed-point number. The total number of digits is specified in size.
#The number of digits after the decimal point is specified in the d parameter.
#The maximum number for size is 65. The maximum number for d is 30. The default value for size is 10. The default value for d is 0.
DEC(size, d)	#Equal to DECIMAL(size,d)

# ========================================== Date and Time Data Types

DATE	#A date. Format: YYYY-MM-DD. The supported range is from '1000-01-01' to '9999-12-31'
DATETIME(fsp)	#A date and time combination. Format: YYYY-MM-DD hh:mm:ss.
#The supported range is from '1000-01-01 00:00:00' to '9999-12-31 23:59:59'.
#Adding DEFAULT and ON UPDATE in the column definition to get automatic initialization and updating to the current date and time
TIMESTAMP(fsp)	#A timestamp. TIMESTAMP values are stored as the number of seconds since 
#the Unix epoch ('1970-01-01 00:00:00' UTC). Format: YYYY-MM-DD hh:mm:ss.
#The supported range is from '1970-01-01 00:00:01' UTC to '2038-01-09 03:14:07' UTC.
#Automatic initialization and updating to the current date and time can be specified using DEFAULT CURRENT_TIMESTAMP and
#ON UPDATE CURRENT_TIMESTAMP in the column definition
TIME(fsp)	#A time. Format: hh:mm:ss. The supported range is from '-838:59:59' to '838:59:59'
YEAR	#A year in four-digit format. Values allowed in four-digit format: 1901 to 2155, and 0000.
#MySQL 8.0 does not support year in two-digit format.

49) MySQL String Functions

Function		Description
ASCII			#Returns the ASCII value for the specific character

ASCII(character)
#syntax

SELECT ASCII(CustomerName) AS NumCodeOfFirstChar
FROM Customers;

CHAR_LENGTH		#Returns the length of a string (in characters)
CHARACTER_LENGTH	#Returns the length of a string (in characters)
CONCAT			#Adds two or more expressions together

CONCAT(expression1, expression2, expression3,...)
#Add three columns into one "Address" column:
SELECT CONCAT(Address, " ", PostalCode, " ", City) AS Address
FROM Customers;

CONCAT_WS		#Adds two or more expressions together with a separator

SELECT CONCAT_WS("-", "SQL", "Tutorial", "is", "fun!") AS ConcatenatedString;

FIELD			#Returns the index position of a value in a list of values
FIND_IN_SET		#Returns the position of a string within a list of strings
FORMAT			#Formats a number to a format like "#,###,###.##", rounded to a specified number of decimal places
INSERT			#Inserts a string within a string at the specified position and for a certain number of characters
INSTR			#Returns the position of the first occurrence of a string in another string
LCASE			#Converts a string to lower-case
LEFT			#Extracts a number of characters from a string (starting from left)
LENGTH			#Returns the length of a string (in bytes)
LOCATE			#Returns the position of the first occurrence of a substring in a string
LOWER			#Converts a string to lower-case
LPAD			#Left-pads a string with another string, to a certain length
LTRIM			#Removes leading spaces from a string
MID				#Extracts a substring from a string (starting at any position)
POSITION		#Returns the position of the first occurrence of a substring in a string
REPEAT			#Repeats a string as many times as specified
REPLACE			#Replaces all occurrences of a substring within a string, with a new substring
REVERSE			#Reverses a string and returns the result
RIGHT			#Extracts a number of characters from a string (starting from right)
RPAD			#Right-pads a string with another string, to a certain length
RTRIM			#Removes trailing spaces from a string
SPACE			#Returns a string of the specified number of space characters
STRCMP			#Compares two strings
SUBSTR			#Extracts a substring from a string (starting at any position)
SUBSTRING		#Extracts a substring from a string (starting at any position)
SUBSTRING_INDEX	#Returns a substring of a string before a specified number of delimiter occurs
TRIM			#Removes leading and trailing spaces from a string
UCASE			#Converts a string to upper-case
UPPER			#Converts a string to upper-case






