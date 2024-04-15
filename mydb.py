import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password'

	)

# create a cursor object

cursorObject = dataBase.cursor()

#Create a database

cursorObject.execute("CREATE DATABASE jska")

print("All Done!")