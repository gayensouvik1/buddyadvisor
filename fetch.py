
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
connection = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "buddyadvisor")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("select * from data where day=1")

# fetch all of the rows from the query
data = cursor.fetchall ()

mydata = np.array(data)

# close the cursor object
cursor.close ()

# close the connection
connection.close ()

mydata_X = mydata[:,6]
mydata_Y = mydata[:,3]
mydata_X_float = np.zeros(shape=(len(mydata_X),1))

for i in range(0, len(mydata_X)):
	mydata_X_float[i] = mydata_X[i].total_seconds()


from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(mydata_X_float,mydata_Y)


print(type(mydata_X_float))
print(type(mydata_Y))
print(mydata_X_float)
clf_score = clf.score(mydata_X_float,mydata_Y)
print(clf_score)

# exit the program
sys.exit()

