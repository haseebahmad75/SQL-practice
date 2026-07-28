import sqlite3

conn=sqlite3.connect("D:\\students.db")

cursor=conn.cursor()
# we have written the query as multi-line string bcz it is easier to read like this, it can also be written on a single line
cursor.execute("""CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER,
               department TEXT
               )""")

students = [
    ("Haseeb", 20, "CS"),
    ("Ali", 21, "SE"),
    ("Sara", 19, "AI"),
    ("Ayesha", 22, "IT")
]

cursor.executemany("INSERT INTO students(name,age,department) VALUES(?,?,?)", students)

conn.commit()
print("Data saved successfully")

cursor.execute("SELECT * FROM students")
rows=cursor.fetchall()
for row in rows:
 print(row)

cursor.execute("SELECT * FROM students LIMIT 10") # LIMIT gives us a certain number of rows
print(cursor.fetchall())
cursor.execute("SELECT DISTINCT name FROM students")
print(cursor.fetchall())

# The following SQL selects all customers that do NOT start with the letter "A":
cursor.execute("SELECT * FROM Customers WHERE CustomerName NOT LIKE 'A%'")

# The following SQL selects all customers with a CustomerID NOT between 10 and 60:
cursor.execute("SELECT * FROM Customers WHERE CustomerID NOT BETWEEN 10 AND 60")

# The following SQL selects all customers with City NOT IN "Paris" or "London":
cursor.execute("SELECT * FROM Customers WHERE NOT City='Paris' OR NOT City='London'")
conn.close()