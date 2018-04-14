
#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query

# import the MySQLdb and sys modules
import MySQLdb
import sys
import numpy as np
from datetime import timedelta	
from datetime import datetime
from math import floor
fobject=[]
outputarray=[]
activities = []
def preprocessing(mydata,activities):
  for i in range(0,len(mydata)):
    if(mydata[i][3] not in activities):
      activities.append(mydata[i][3])


def my_range(start, end, step):
  while start <= end:
    yield start
    start += step

def push1(data,i):
  tempobject = []
  for  j in my_range(i-480,i-1,1):
    tempobject.append(activities.index(data[j][3]))
  for  j in my_range(i-1470,i-1410,1):
    tempobject.append(activities.index(data[j][3]))
  for  j in my_range(i-10110,i-10050,1):
    tempobject.append(activities.index(data[j][3]))
  for  j in my_range(i-10110,i-10050,1):
    tempobject.append(activities.index(data[j][3]))
  for  j in my_range(i-20190,i-20130,1):
    tempobject.append(activities.index(data[j][3]))
  for  j in my_range(i-30270,i-30210,1):
    tempobject.append(activities.index(data[j][3]))
  fobject.append(tempobject)


def make_data(data):
  for k in my_range(22,floor(len(data)/1440),1):
    for i in my_range(1440*(k-1),(1440*k)-1,1):
      push1(data,i)
      # print("hello")
      # print(activities.index(data[i][3])
      outputarray.append(activities.index(data[i][3]))



            



# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "buddyadvisor",unix_socket="/opt/lampp/var/mysql/mysql.sock")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("select * from continuous_data")
data1 =cursor.fetchall()
print(len(data1))
preprocessing(data1,activities)
print(len(activities))
make_data(data1)
data = np.array(fobject,dtype=str)
print(len(data))
x_training_set = data
y_training_set = np.array(outputarray)
x_training_set.astype(int)
y_training_set.astype(int)

from keras.utils import to_categorical
x_training_set = to_categorical(x_training_set)
y_training_set = to_categorical(y_training_set)

print(x_training_set.shape)
print(y_training_set.shape)

connection.close()
