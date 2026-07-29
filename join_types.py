import sqlite3
conn = sqlite3.connect("D:\\SQL\\store.db")
cursor=conn.cursor()

# List all customers along with their orders. Include customers who have never ordered.
cursor.execute("""SELECT c.first_name, c.last_name, orders.order_id
                FROM customers AS c
                LEFT JOIN orders 
                 ON c.customer_id = orders.customer_id
            """)
customers=cursor.fetchall()
for customer in customers:
    print(customer)

# Find customers who have never placed an order (using LEFT JOIN + IS NULL).
cursor.execute("""SELECT c.first_name
                FROM customers AS c 
                LEFT JOIN orders 
                 ON c.customer_id = orders.customer_id
                WHERE orders.order_id IS NULL
                """)
customers=cursor.fetchall()
for cust in customers:
    print(cust)

# List all products and, if sold, how many times each was ordered — including products never sold.
cursor.execute("""SELECT  p.product_name, COUNT(oi.product_id)
                FROM products AS p
                LEFT JOIN order_items AS oi
                ON p.product_id = oi.product_id
                GROUP BY p.product_name
                """)
products=cursor.fetchall()
for product in products:
    print(product)

# Rewrite Q1 using RIGHT JOIN instead of LEFT JOIN (swap table order and reason through it).
cursor.execute("""SELECT c.first_name, orders.order_id
                FROM orders
                RIGHT JOIN customers AS c
                ON orders.customer_id = c.customer_id
                """)
data=cursor.fetchall()
for item in data:
    print(item)

newconn=sqlite3.connect("D:\\SQL\\practice.db")
obj=newconn.cursor()

# List all departments and their employees, ensuring departments with no employees still appear.
obj.execute("""SELECT d.department_name, e.name
            FROM employees AS e
            RIGHT JOIN departments AS d
            On e.department_id = d.department_id
            """)
dept=obj.fetchall()
for item in dept:
    print(item)

# List each employee alongside their manager's name.
obj.execute("""SELECT e.name AS Employees, m.name AS Managers
            FROM employees AS e
            JOIN employees AS m
            ON m.employee_id = e.manager_id
            """)
headers=[column[0] for column in obj.description]
print(headers)
employees=obj.fetchall()
for emp in employees:
    print(emp)

#Find all pairs of employees who work in the same department (avoid duplicate pairs like (A,B) and (B,A)).
obj.execute("""SELECT e1.name, e2.name, e1.department_id
            FROM employees AS e1
            JOIN employees AS e2
            ON e1.department_id = e2.department_id
            AND e1.employee_id < e2.employee_id;
            """)
employees=obj.fetchall()
for emp in employees:
    print(emp)

# Find products that belong to the same category but have different prices
obj.execute("""SELECT p1.product_name, p2.product_name, p1.category_id, ABS(p1.price-p2.price)
            FROM products AS p1
            JOIN products AS p2
            ON p1.category_id = p2.category_id
            AND p1.product_id < p2.product_id
            AND p1.price != p2.price""")
products=obj.fetchall()
for item in products:
    print(item)