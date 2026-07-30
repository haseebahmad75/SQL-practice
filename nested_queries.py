import sqlite3

connection=sqlite3.connect("D:\\SQL\\company.db")
cursor=connection.cursor()

# Find the names of employees who earn more than the average salary of all employees.
cursor.execute("""SELECT emp_name
                FROM employees
                WHERE salary > (
                SELECT AVG(salary)
                FROM employees) 
            """)
print(cursor.fetchall())

# Find the customer(s) with the highest total single order amount.
cursor.execute("""SELECT * FROM customers
                WHERE cust_id = (
                SELECT cust_id 
                FROM orders 
                WHERE amount = (
                SELECT MAX(amount)
                FROM orders)
                )
            """)
print(cursor.fetchall())

# List products that have never appeared in order_items (use NOT IN with a subquery).
cursor.execute("""SELECT * FROM products 
                WHERE product_id NOT IN(
                SELECT product_id
                FROM order_items)
            """)
products=cursor.fetchall()
for product in products:
    print(product)

# Find employees who work in the same department as Ali Raza, excluding Ali Raza himself.
cursor.execute("""SELECT * FROM employees 
                WHERE dept_id =(
                SELECT dept_id 
                FROM employees
                WHERE emp_name='Ali Raza')
                AND NOT emp_name='Ali Raza'
            """)
print(cursor.fetchall())

# Get a combined list of cities from customers and locations from departments, with no duplicates.
cursor.execute("""SELECT city FROM customers
                UNION
                SELECT location FROM departments""")
this_list=cursor.fetchall()
for item in this_list:
    print(item[0]) # this index will remove the parentheses and comma in result 

# List the names of employees who are managers (appear in manager_id column)
# UNION employees who earn more than 130,000 — as one distinct list of names.
cursor.execute("""SELECT emp_name FROM employees 
                WHERE emp_id IN(
                SELECT manager_id
                FROM employees)
                UNION 
                SELECT emp_name FROM employees 
                WHERE salary > 130000
            """)
print(cursor.fetchall())