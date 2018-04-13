
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
cursor.execute ("select * from data where day=2 and user_id=2")

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

my_schedule = np.zeros(shape=(96,1))

for i in range(0,96):
	my_schedule[i] = i*900;


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(mydata_X_float,mydata_Y)



my_prediction = clf.predict(my_schedule)


print( my_prediction)
print(type(mydata_X_float))

# # print(type(mydata_X_float))
# # print(type(mydata_Y))
# # print(mydata_X_float)
# clf_score = clf.score(mydata_X_float,mydata_Y)
# print(clf_score)




# # plot google map

# mycoord_X = mydata[:,1]
# mycoord_Y = mydata[:,2]

# for i in range(0,len(mycoord_X)):
# 	mycoord_X[i] = mycoord_X[i]/10000000;
# 	mycoord_Y[i] = mycoord_Y[i]/10000000;
# from gmplot import gmplot
# gmap = gmplot.GoogleMapPlotter(77.8946302, 29.8622079, 13)
# # # Scatter points
# # top_attraction_lats = mycoord_X;
# # top_attraction_lons = mycoord_Y;
# # gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)
# gmap.draw("my_map.html")

# exit the program
sys.exit()

