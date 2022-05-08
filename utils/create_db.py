import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="abc28051987A")

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE gema")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:

    print(db)

