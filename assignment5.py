# Assignment 5
# SQLite Database Program

import sqlite3

# Create / Connect Database
conn = sqlite3.connect('db1.db')

# Create Cursor
cur = conn.cursor()

# -----------------------------------
# 1) Create Tables
# -----------------------------------

sql = """
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    city VARCHAR(50),
    age INTEGER
)
"""
cur.execute(sql)

sql = """
CREATE TABLE IF NOT EXISTS course (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name VARCHAR(50),
    fees INTEGER
)
"""
cur.execute(sql)

sql = """
CREATE TABLE IF NOT EXISTS faculty (
    faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,
    faculty_name VARCHAR(50),
    subject VARCHAR(50)
)
"""
cur.execute(sql)

# -----------------------------------
# 2) Insert Records
# -----------------------------------

sql = """
INSERT INTO student (name, city, age)
VALUES
('Pankaj', 'Delhi', 20),
('Rahul', 'Mumbai', 21),
('Amit', 'Jaipur', 19)
"""
cur.execute(sql)

sql = """
INSERT INTO course (course_name, fees)
VALUES
('Python', 15000),
('Java', 18000),
('DBMS', 12000)
"""
cur.execute(sql)

sql = """
INSERT INTO faculty (faculty_name, subject)
VALUES
('Amit Sir', 'Python'),
('Neha Maam', 'Java'),
('Raj Sir', 'DBMS')
"""
cur.execute(sql)

# -----------------------------------
# 3) Different SELECT Operations
# -----------------------------------

print("\nAll Students")
sql = "SELECT * FROM student"
data = cur.execute(sql)

for row in data:
    print(row)

print("\nStudents from Delhi")
sql = "SELECT * FROM student WHERE city='Delhi'"
data = cur.execute(sql)

for row in data:
    print(row)

print("\nCourse Names")
sql = "SELECT course_name FROM course"
data = cur.execute(sql)

for row in data:
    print(row)

# -----------------------------------
# 4) Update Data
# -----------------------------------

sql = """
UPDATE student
SET city='Pune'
WHERE id=2
"""
cur.execute(sql)

print("\nData Updated Successfully")

# -----------------------------------
# 5) Delete Data
# -----------------------------------

sql = """
DELETE FROM student
WHERE id=3
"""
cur.execute(sql)

print("Data Deleted Successfully")

# -----------------------------------
# 6) Final Student Table
# -----------------------------------

print("\nFinal Student Table")

sql = "SELECT * FROM student"
data = cur.execute(sql)

for row in data:
    print(row)

# Save Changes
conn.commit()

# Close Connection
conn.close()

#---------------------------------
# OUTPUT
#---------------------------------
# [Running] python -u "c:\Users\PANKAJ\Documents\intership\class 1\assignment5.py"

# All Students
# (1, 'Pankaj', 'Delhi', 20)
# (2, 'Rahul', 'Mumbai', 21)
# (3, 'Amit', 'Jaipur', 19)

# Students from Delhi
# (1, 'Pankaj', 'Delhi', 20)

# Course Names
# ('Python',)
# ('Java',)
# ('DBMS',)

# Data Updated Successfully
# Data Deleted Successfully

# Final Student Table
# (1, 'Pankaj', 'Delhi', 20)
# (2, 'Rahul', 'Pune', 21)

# [Done] exited with code=0 in 1.216 seconds

