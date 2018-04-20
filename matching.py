
#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query

# import the MySQLdb and sys modules


import sys

import numpy as np

from math import pi, sqrt, exp

sigma = 10
mu = 0

def gauss(n=96,sigma=10):
    r = range(-int(n/2),int(n/2)+1)
    return [1 / (sigma * sqrt(2*pi)) * exp(-float(x)**2/(2*sigma**2)) for x in r]

# mu, sigma = 0, 0.1
# s = np.random.normal(mu, sigma, 1000)
# print(s[0])
g = gauss(96,sigma)
g = np.roll(g,48)


# import matplotlib.pyplot as plt
# count, bins, ignored = plt.hist(g, 30, normed=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
# np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
# linewidth=2, color='r')
# plt.show()


# user_id = int(sys.argv[1])
user_id = sys.argv[1]
activity = sys.argv[2]
# user_id = "OPqacBiKHFYoieOI2abLCdSLHYx1"
# activity = "gym"


def cal(time):
	return 0

def filter(mydata,activity,time=-1):
	result = []
	if time==-1:
		start_time = 2
		end_time = 97
	else:
		start_time = time[0]
		end_time = time[1]

		start_time = cal(start_time)
		end_time = cal(end_time)

	for i in range(0,len(mydata)):
		count = 0
		for j in range (start_time,end_time+1):
			if(mydata[i][j]==activity):
				count = count + 1
		if count>0:
			result.append(mydata[i])
	return result


def similarity_matching(users1,users2):
	user1 = users1
	user2 = users2
	user1_id = user1[0]
	user2_id = user2[0]
	# print(user1_id,user2_id)
	user1 = np.delete(user1, 0, 0)
	user1 = np.delete(user1, 0, 0)
	user2 = np.delete(user2, 0, 0)
	user2 = np.delete(user2, 0, 0)

	score = 0

	for i in range(0,len(user1)):
		count = 0
		for j in range(0,len(user2)):
			if user1[j] == user2[j]:
				count = count + 1
		
		# print(count,g[i]*count)
		score = score+g[i]*count
		user1 = np.roll(user1,1)

	return score




import MySQLdb
import sys
import numpy as np


# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "buddyadvisor",unix_socket="/opt/lampp/var/mysql/mysql.sock")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("select * from schedule where day=1 order by user_id")

# fetch all of the rows from the query
data = cursor.fetchall ()

cursor.execute("select * from users")
users = cursor.fetchall()
users = np.array(users)

user_id = list(users[:,1]).index(user_id)+1

mydata = np.array(data)
mydata1 = filter(mydata,activity)

# print(mydata)
# mydata = mapping(data,placename)


# print(similarity_matching(mydata[user_id-1],mydata[0]))


result = []
for i in range (0,len(mydata1)):
	if (i+1)!=user_id:
		# print(i+1,user_id)
		result.append((i+1,similarity_matching(mydata[user_id-1],mydata1[i])))

result = sorted(result,key=lambda x: x[1],reverse=True)
w_result = ""+users[list(users[:,0]).index(str(result[0][0]))][1]

for i in range(1,len(result)):
	w_result = w_result+"\n"+users[list(users[:,0]).index(str(result[i][0]))][1]


print(w_result)
	
		

# close the cursor object
cursor.close ()

# close the connection
connection.close ()

# exit the program
sys.exit()

