import sqlite3

conn = sqlite3.connect("D:\\SQL\\store.db")
cursor = conn.cursor()

# List each order with the customer's first and last name.
cursor.execute("""SELECT orders.*, c.first_name, c.last_name
               FROM customers AS c 
               LEFT JOIN orders
               ON orders.customer_id=c.customer_id""")
rows=cursor.fetchall()
for row in rows:
    print(row)

# Show all products along with their category name.
cursor.execute(""" SELECT * FROM products 
               JOIN categories 
               ON products.category_id = categories.category_id""")
data=cursor.fetchall()
for item in data:
    print(item)

# List all reviews with the reviewer's email and the product name being reviewed.
cursor.execute("""SELECT reviews.*, c.email, p.product_name 
               FROM reviews
               JOIN customers AS c ON reviews.customer_id = c.customer_id
               JOIN products AS p ON reviews.product_id = p.product_id
               """)
reviews=cursor.fetchall()
for review in reviews:
    print(review)

# Show each order and which employee handled it.
cursor.execute(""" SELECT e.first_name, e.last_name, orders.*
               FROM orders 
               JOIN employees AS e ON orders.employee_id = e.employee_id""")
orders=cursor.fetchall()
for order in orders:
    print(order)

# list every customer whose country is not "Pakistan", showing their name and country.
cursor.execute(""" SELECT c.first_name, c.last_name, c.country
               FROM customers AS c
               WHERE NOT country="Pakistan"
               """)
customers=cursor.fetchall()
for cust in customers:
    print(cust)

# For each customer, find their total number of orders and total amount spent (join orders → order_items, multiply quantity × unit_price).
cursor.execute("""SELECT c.first_name,c.last_name, COUNT(orders.order_id), ROUND(SUM(order_items.quantity * order_items.unit_price),2)
               FROM customers AS c
               JOIN orders 
               ON c.customer_id = orders.customer_id
               JOIN order_items 
               ON orders.order_id = order_items.order_id
               GROUP BY c.first_name, c.last_name;
               """)
data=cursor.fetchall()
for item in data:
    print(item)

# Find the top 5 best-selling products by total quantity sold (order_items → products).
cursor.execute("""SELECT COUNT(products.product_id) AS order_count, products.product_name
               FROM products
               JOIN order_items
                 ON products.product_id = order_items.product_id
               GROUP BY products.product_id, products.product_name
               ORDER BY order_count DESC
               LIMIT 5;
               """)
products = cursor.fetchall()
for product in products:
    print(product)

# List each category with its average product price and number of products in it.
cursor.execute("""SELECT c.category_name AS [Category Name], ROUND(AVG(p.price),2) AS [Average Product Price], SUM(p.stock_qty) AS Quantity
              FROM categories AS c
              JOIN products AS p
                ON c.category_id = p.category_id
              GROUP BY c.category_name
              """)
headers=[column[0] for column in cursor.description]
print(headers)
categories = cursor.fetchall()
for cat in categories:
    print(cat)

# Find employees who have processed more than 30 orders (orders → employees, GROUP BY, HAVING).
cursor.execute("""SELECT e.first_name, e.last_name
              FROM employees AS e
              JOIN orders 
              ON e.employee_id = orders.employee_id
              GROUP BY e.first_name, e.last_name
              HAVING COUNT(orders.order_id) > 30;
              """)
employees=cursor.fetchall()
for emp in employees:
    print(emp)

# For each product, show its average review rating and number of reviews; include products with zero reviews (hint: LEFT JOIN).
cursor.execute("""SELECT p.product_name, ROUND(AVG(r.rating),2) , COUNT(p.product_id)
              FROM products AS p
              LEFT JOIN reviews AS r
               ON p.product_id = r.product_id
              GROUP BY p.product_name, p.product_id """)
reviews=cursor.fetchall()
for rev in reviews:
    print(rev)

# Find customers who have placed orders but never left a review (hint: LEFT JOIN + IS NULL, or NOT IN/NOT EXISTS).
cursor.execute("""SELECT c.first_name, c.last_name
               FROM customers AS c
               LEFT JOIN reviews
               ON c.customer_id = reviews.customer_id
               WHERE comment IS NULL
               """)
customers = cursor.fetchall()
for customer in customers:
    print(customer)

# Self-join challenge: list each employee alongside their manager's name.
cursor.execute("""SELECT e.first_name, e.last_name, m.first_name, m.last_name
            FROM employees AS e
            JOIN employees AS m
             ON m.employee_id = e.manager_id 
            """)
data=cursor.fetchall()
for item in data:
    print(item)

# Find the total revenue per country (customers → orders → order_items).
cursor.execute("""SELECT c.country, SUM(oi.quantity * oi.unit_price)
                FROM customers AS c
                JOIN orders 
                 ON c.customer_id = orders.customer_id
                JOIN order_items AS oi
                 ON orders.order_id = oi.order_id
                GROUP BY c.country """)
revenue = cursor.fetchall()
for rev in revenue:
    print(rev)

