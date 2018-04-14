#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query

# import the MySQLdb and sys modules
import MySQLdb
import sys
import numpy as np
from datetime import timedelta	
from datetime import datetime

previousarray=[]
prearray=[]
fobject=[[]]
threshold=timedelta(minutes=20)
def push1(data,writedate):
    query="insert into continuous_data (user_id,date_time,placetype,place_name) values ("+str(data[0])+",'"+str(writedate)+"','"+data[2]+"','"+data[3]+"');"
    cursor.execute(query)

def handleresult(newdata,startdate):
	if not newdata:		
		if ((startdate-previousarray[1])<threshold):
			push1(previousarray,startdate)
		else:
			push1(prearray,startdate)

	else:
		previousarray[1]=startdate
		previousarray[2]=newdata[0][1]
		previousarray[3]=newdata[0][2]
		push1(previousarray,startdate)





mydata = []
mydata_X = []
mydata_Y = []
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "buddyadvisor",unix_socket="/opt/lampp/var/mysql/mysql.sock")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("select * from data where user_id=2 order by date desc limit 1")
data1 =cursor.fetchall()

cursor.execute("select * from data where user_id=2 order by date,time limit 1")
# fetch all of the rows from the query
data2 = cursor.fetchall ()
#startdate=datetime(data2[0][7],data2[0][6])
enddate=data1[0][7]
dt1=data2[0][7]
dt2=data2[0][6]
startdate=datetime(dt1.year,dt1.month,dt1.day+1)

dt1=data1[0][7]
dt2=data1[0][6]
enddate=datetime(dt1.year,dt1.month,dt1.day+1)

previousarray=[data2[0][0],startdate,"ambiguous","ambiguous"]
prearray=previousarray
print(startdate)
print(enddate)

while(startdate<enddate):
		startdate=startdate + timedelta(seconds=60)
		query="select user_id,placetype,place_name from data where user_id=2 and date='"+str(startdate.date())+"' and time like '"+str(startdate.strftime("%H:%M"))+"%' limit 1;"
		cursor.execute(query)
		newdata=cursor.fetchall()
		handleresult(newdata,startdate)

connection.commit()