
#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query

# import the MySQLdb and sys modules
import MySQLdb
import sys
import numpy as np

mydata = []
mydata_X = []
mydata_Y = []
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "buddyadvisor",unix_socket="/opt/lampp/var/mysql/mysql.sock")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.

query = ("INSERT INTO refined_data "
               "(time, placetype, my_index) "
               "VALUES (%s, %s,%s)")
val = ('5:06:09','dc','3')
# query = "insert into `refined_data`(time, placetype, my_index)" +"values " + "('07:08:08','th',3);"
# qry = "select placetype from `refined_data`"
cursor.execute (query,val)
connection.commit()

# fetch all of the rows from the query
data = cursor.fetchall ()
print(data)

# close the cursor object
cursor.close ()

# close the connection
connection.close ()


# exit the program
sys.exit()

