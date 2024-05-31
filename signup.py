#!python.exe
#!C:/xampp/htdocs/trial/venv/Scripts/python.exe
#import cgi, cgitb
#import os
#form=cgi.FieldStorage()
#import mysql.connector

#cgitb.enable()

#print("Content-Type: text/html\n")

#mydb = mysql.connector.connect(
 # host="localhost",
  #user="root",
  #password="",
  #database="test"
#)

#print("<h1>Connected</h1>")
#uname= form.getvalue('name')
#uemail= form.getvalue('email')
#upassword= form.getvalue('pwd')

#mycursor = mydb.cursor()

#sql = "INSERT INTO signup (name, email, pwd) VALUES (%s, %s, %s)"
#val = (uname, uemail, upassword)
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")

#!C:/xampp/htdocs/trial/venv/Scripts/python.exe
import cgi
import cgitb
import mysql.connector

# Enable detailed error reporting
cgitb.enable()

print("Content-Type: text/html\n")

# Retrieve form data
form = cgi.FieldStorage()
uname = form.getvalue('name')
uemail = form.getvalue('email')
upassword = form.getvalue('pwd')

# Connect to the database
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="table"
    )
    #print("<h1>Connected</h1>")
except mysql.connector.Error as err:
    print(f"<p>Error: {err}</p>")
    exit()

# Check if form data is retrieved correctly
if not uname or not uemail or not upassword:
    print("<p>Error: Missing form data</p>")
    exit()

# Insert data into the database
try:
    mycursor = mydb.cursor()
    sql = "INSERT INTO signup (name, email, pwd) VALUES (%s, %s, %s)"
    val = (uname, uemail, upassword)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"<p>{mycursor.rowcount} User registered successfully.</p>")
except mysql.connector.Error as err:
    print(f"<p>Error: {err}</p>")
finally:
    mycursor.close()
    mydb.close()

