from BadAssRobot import Liker
import threading

# botusername = subscription(username,password,topics,active)

file = open('/Users/JohnLecomte/Documents/python/users.txt') # look up an example for this.

threads = []

for line in file:
	row = line.strip().split(":")
	username = row[0]
	password = row[1]
	tags = row[2].split(",")
	comments = row[3].split(",")
	active = row[4]
	if active == "liker" or active == "liker/commenter" or active == "liker/commenter/follower":
		new_thread = Liker(username,password,tags,comments,active)
		threads.append(new_thread)
		new_thread.start()
	else:
		pass
	


#random.choice([list])