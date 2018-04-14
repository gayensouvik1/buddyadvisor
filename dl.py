
#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query

# import the MySQLdb and sys modules


def preprocessing(mydata,activities):
	for i in range(0,len(mydata)):
		if(mydata[i][5] not in activities):
			activities.append(mydata[i][5])


import MySQLdb
import sys
import numpy as np

mydata = []
mydata_X = []
mydata_Y = []
activities = []
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "buddyadvisor",unix_socket="/opt/lampp/var/mysql/mysql.sock")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("select * from refined_data where user_id=2")

# fetch all of the rows from the query
data = cursor.fetchall ()

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

mydata = np.array(data)
# mydata = mapping(data,placename)

preprocessing(mydata,activities)

x_train = mydata[:6]
y_train = mydata[:5]

x_training_set = []
y_training_set = []

x_sample = []


y_sample = data[10][5]





# x_training_set = np.append(x_training_set,x_sample,axis=0)
x_temp_sample = x_sample


for i in range (41,len(mydata)):
	x_sample = []

	for j in range (i-39,i):
		x_sample.append(activities.index(mydata[j][5]))
	y_sample = activities.index(mydata[j][5])
	x_training_set.append(x_sample)
	y_training_set.append(y_sample)

x_training_set = np.array(x_training_set)
y_training_set = np.array(y_training_set)

x_training_set = np.delete(x_training_set, (0), axis=0)
y_training_set = np.delete(y_training_set, (0), axis=0)
x_training_set.astype(int)
y_training_set.astype(int)

from keras.utils import to_categorical
x_training_set = to_categorical(x_training_set)
y_training_set = to_categorical(y_training_set)


print(x_training_set.shape)


# print(len(x_training_set[1]))
print(y_training_set.shape)


















import keras
from keras.models import Sequential
from keras.layers import Dense,LSTM, Dropout, Activation
from keras.optimizers import SGD

model = Sequential()

# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(LSTM(units=1024, activation='relu', input_shape=(39,223)))
model.add(Dense(units=223, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.fit(x_training_set, y_training_set, epochs=5, batch_size=32)

# classes = model.predict(x_test, batch_size=128)


# close the cursor object
cursor.close ()

# close the connection
connection.close ()

# exit the program
sys.exit()

