import sqlite3

connection=sqlite3.connect("D:\\SQL\\company.db")
cursor=connection.cursor()

# For each employee, find those who earn more than the average salary of their own department.
cursor.execute("""SELECT e1.emp_name
                FROM employees AS e1
                WHERE salary > (
                SELECT AVG(e2.salary)
                FROM employees AS e2
                WHERE e1.dept_id=e2.dept_id)
            """)
print(cursor.fetchall())

# Find employees who earn the highest salary within their department (i.e., their department's max).
cursor.execute("""SELECT e1.emp_name
                FROM employees AS e1
                WHERE e1.salary = (
                SELECT MAX(e2.salary)
                FROM employees AS e2
                WHERE e2.dept_id=e1.dept_id)
            """)
print(cursor.fetchall())

# Find customers whose total order amount is higher than the average total order amount across all customers (correlated aggregate comparison).
cursor.execute("""SELECT cust_name
                FROM customers
                WHERE cust_id IN
                (
                   SELECT cust_id FROM orders
                   GROUP BY cust_id
                   HAVING SUM(amount) >
                    (
                      SELECT AVG(total_amount)
                      FROM
                      (
                        SELECT SUM(amount) AS total_amount
                        FROM orders
                        GROUP BY cust_id
                      )
                    )
                )
            """)
print(cursor.fetchall())

# For each order, show orders whose amount is greater than the average amount of all other orders by the same customer (excluding the current order).
cursor.execute("""SELECT o.*
                FROM orders AS o
                WHERE o.amount > (
                   SELECT AVG(e.amount)
                   FROM orders AS e
                   WHERE e.cust_id=o.cust_id
                   AND e.order_id <> o.order_id)
                """)
# AND NOT statement is written inside the subquery because it means while calculating this customer's average, don't include the current order
print(cursor.fetchall())
