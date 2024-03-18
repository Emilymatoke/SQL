# when working wit sqlite3 import package

import sqlite3

#first create database then connect- gives a path  
#storing referenced = variable
conn = sqlite3.connect ('moringa.db')

#create tables
#student
#tms
#tms_students

#the execute command allows us to execute sql queries to sql engines
conn.execute('''CREATE TABLE IF NOT EXISTS students(
             id INTEGER PRIMARY KEY, 
             name TEXT NOT NULL,
             email TEXT NULL

);''')


conn.execute('''CREATE TABLE IF NOT EXISTS tms(
            id INTEGER PRIMARY KEY, 
             name TEXT NOT NULL,
             email TEXT NULL,
             staffnumber INTEGER NOT NULL 
);''')


conn.execute('''CREATE TABLE IF NOT EXISTS tms_students(
            id INTEGER PRIMARY KEY, 
            tmsid INTEGER ,
            studentsid INTEGER,
            FOREIGN KEY(tmsid) REFERENCES tms(id),
             FOREIGN KEY(studentsid) REFERENCES students(id)
);''')
# CRUD
name = "Elizabeth Matoke"
email = "eliza@gmail.com"

#CREATE A RECORD
#INSERT QUERY is used to insert records to a DB table
# Prepared statements : sql injections ; what is this?
#create a cursor object to access query methods from sqlite package
cursor = conn.cursor ()

#before inserting a record check for presence of record
cursor.execute("SELECT id from students WHERE name = ? AND email = ?", (name, email))
existing_record = cursor.fetchone()

if not existing_record :
    conn.execute("INSERT INTO students (name, email) VALUES(?,?)", (name, email))
else :
    print("Record already exists")


#READ A RECORD
#We use SELECT namecolumn1, namecolumn2 FROM tablename or
# SELECT *(all columns) FROM tablename
#Returns a list
result = conn.execute("SELECT * FROM students")
#loop to see data
for row in result :
    print(f"id: {row[0]}, Name:{row[1]}, Email:{row[2]}")


#TO UPDATE
#UPDATE tablename SET fieldname = ?, fieldname =? WHERE id = ?, (values, ?)
conn.execute("UPDATE students SET NAME = ? WHERE id = ?",("Moraa", 1))
    

#DELETE record
#DELETE FROM tablename-deletes everything
#DELETE FROM tablename WHERE fieldname = ?, (value,)
conn.execute("DELETE FROM students WHERE id = ?", (2,))






#commit changes
conn.commit()



#close connection
conn.close()




