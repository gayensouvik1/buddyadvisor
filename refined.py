
#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query

# import the MySQLdb and sys modules
import MySQLdb
import sys
import numpy as np
from datetime import timedelta	

mydata = []
mydata_X = []
mydata_Y = []
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "buddyadvisor",unix_socket="/opt/lampp/var/mysql/mysql.sock")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("select * from data")

# fetch all of the rows from the query
data = cursor.fetchall ()

mydata = np.array(data)



mydata_X = mydata[:,6]
mydata_Y = mydata[:,5]
mydata_day = mydata[:,8]

my_refined_X = []
my_refined_Y = []

seconds = mydata_X[0].total_seconds()
closest = (seconds % 3600) // 60
closest = closest - closest%15
temp = closest
info = 0
day = mydata_day[0]
dict = [mydata_Y[0]]

for i in range(1, len(mydata_X)):

	seconds = mydata_X[i].total_seconds()

	hour = seconds//3600
	closest = (seconds % 3600) // 60

	closest = closest - closest%15
	# print(temp,closest)
	
	if(temp!=closest):
		sortedlist = sorted(dict,key=dict.count,reverse=True)
		# print(sortedlist)
		my_refined_X.append([hour*3600+temp*60,sortedlist[0],i])
		temp = closest
		day = mydata_day[i]
		dict = []
		info = i

	dict.append(mydata_Y[i])


print(my_refined_X[0][0])


for i in range(0, len(my_refined_X)):
	h = (my_refined_X[i][0] // 3600) 
	m = (my_refined_X[i][0] % 3600) // 60
	insert = ("INSERT INTO refined_data "
	               "(user_id,longitude, latitude,placetype,placedetails,placename,time,date, day) "
	               "VALUES (%s,%s, %s,%s,%s,%s,%s,%s,%s)")
	tm = ""+str(int(h))+":"+str(int(m))+":00"
	ind = my_refined_X[i][2]
	val = (str(mydata[ind][0]),str(mydata[ind][1]),str(mydata[ind][2]),str(mydata[ind][3]),str(mydata[ind][4]),str(my_refined_X[i][1]),tm,str(mydata[ind][7]),str(mydata[ind][8]))
	cursor.execute (insert,val)

connection.commit()

# close the cursor object
cursor.close ()

# close the connection
connection.close ()

# ,]

# mydata_X_float = np.zeros(shape=(len(mydata_X),1))

# for i in range(0, len(mydata_X)):
# 	mydata_X_float[i] = mydata_X[i].total_seconds()


# from sklearn.naive_bayes import GaussianNB
# clf = GaussianNB()
# clf.fit(mydata_X_float,mydata_Y)


# print(type(mydata_X_float))
# print(type(mydata_Y))
# print(mydata_X_float)
# clf_score = clf.score(mydata_X_float,mydata_Y)
# print(clf_score)

# exit the program
sys.exit()

