import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

#employees and their offices
q = """
 SELECT firstName, lastName, city, state
 FROM employees
 JOIN offices ON employees.officeCode = offices.officeCode
 ORDER BY firstName, lastName
"""

df = pd.read_sql_query(q, conn)
print(df)

#customers and their orders
q = """
 SELECT contactFirstName, contactLastName, orderNumber, orderDate, status 
 FROM customers
 JOIN orders ON orders.customerNumber = customers.customerNumber
"""

df = pd.read_sql_query(q, conn)
print(df.head())
