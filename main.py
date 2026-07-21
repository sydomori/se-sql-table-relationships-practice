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

#customers and their orders
q = """
 SELECT contactFirstName, contactLastName, amount, paymentDate
 FROM customers
 JOIN payments ON payments.customerNumber = customers.customerNumber
 ORDER BY amount DESC
"""

df = pd.read_sql_query(q, conn)
print(df.head())

#orders, order details and product details(many to many)
q = """
SELECT
    contactFirstName,
    contactLastName,
    productName,
    quantityOrdered,
    orderDate
FROM customers
JOIN orders
    USING(customerNumber)
JOIN orderdetails
    USING(orderNumber)
JOIN products
    USING (productCode)
ORDER BY orderDate DESC
;"""
df = pd.read_sql(q, conn)
print('Total number of results:', len(df))
df.head()

