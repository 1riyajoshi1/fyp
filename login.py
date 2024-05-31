#!C:/xampp/htdocs/trial/venv/Scripts/python.exe
import mysql.connector
import cgi, cgitb
import urllib.request
#form = cgi.FieldStorage()
cgitb.enable()

print("Content-Type: text/html\n")

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="table"
)
form = cgi.FieldStorage()
uname=form.getvalue('username')
password1=form.getvalue('password')
mycursor =mydb.cursor()
sql="SELECT * FROM signup where name=%s and pwd=%s"
val=(uname,password1)
mycursor.execute(sql,val)

myresult = mycursor.fetchall()
if len(myresult)==0:
 print ("Invalid username or password...")
else:
 #from urllib.request import urlopen
 print("<script language='javascript'>window.location='http://localhost/trial/form.html'</script>")
 print()
 #url='http://localhost/form.html'
 #req=urllib.request.Request(url)
 #print(req.)
 #response =urllib.request.urlopen('')

 #response.geturl()