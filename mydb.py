import mysql.connector


dataBase = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "test"
	)

cursorObject = dataBase.cursor()

cursorObject.execute("create database elderco")

print("All done")