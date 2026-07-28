import sqlite3

conn = sqlite3.connect("D:\\store.db")
cursor = conn.cursor()

# # List each order with the customer's first and last name.
# cursor.execute("""SELECT orders.*, c.first_name, c.last_name
#                FROM customers AS c 
#                LEFT JOIN orders
#                ON orders.customer_id=c.customer_id""")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)

# # Show all products along with their category name.
# cursor.execute(""" SELECT * FROM products 
#                JOIN categories 
#                ON products.category_id = categories.category_id""")
# data=cursor.fetchall()
# for item in data:
#     print(item)

# # List all reviews with the reviewer's email and the product name being reviewed.
# cursor.execute("""SELECT reviews.*, c.email, p.product_name 
#                FROM reviews
#                JOIN customers AS c ON reviews.customer_id = c.customer_id
#                JOIN products AS p ON reviews.product_id = p.product_id
#                """)
# reviews=cursor.fetchall()
# for review in reviews:
#     print(review)

# # Show each order and which employee handled it.
# cursor.execute(""" SELECT e.first_name, e.last_name, orders.*
#                FROM orders 
#                JOIN employees AS e ON orders.employee_id = e.employee_id""")
# orders=cursor.fetchall()
# for order in orders:
#     print(order)

# # list every customer whose country is not "Pakistan", showing their name and country.
# cursor.execute(""" SELECT c.first_name, c.last_name, c.country
#                FROM customers AS c
#                WHERE NOT country="Pakistan"
#                """)
# customers=cursor.fetchall()
# for cust in customers:
#     print(cust)

# # For each customer, find their total number of orders and total amount spent (join orders → order_items, multiply quantity × unit_price).
# cursor.execute("""SELECT c.first_name,c.last_name, COUNT(orders.order_id), ROUND(SUM(order_items.quantity * order_items.unit_price),2)
#                FROM customers AS c
#                JOIN orders 
#                ON c.customer_id = orders.customer_id
#                JOIN order_items 
#                ON orders.order_id = order_items.order_id
#                GROUP BY c.first_name, c.last_name;
#                """)
# data=cursor.fetchall()
# for item in data:
#     print(item)

# # Find the top 5 best-selling products by total quantity sold (order_items → products).
# cursor.execute("""SELECT COUNT(products.product_id) AS order_count, products.product_name
#                FROM products
#                JOIN order_items
#                  ON products.product_id = order_items.product_id
#                GROUP BY products.product_id, products.product_name
#                ORDER BY order_count DESC
#                LIMIT 5;
#                """)
# products = cursor.fetchall()
# for product in products:
#     print(product)

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
