import mysql.connector
database = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'Pj@123456'
)



#prepare a cursor object using cursor() method
cursorObject = database.cursor()

#Createa a database
# cursorObject.execute("CREATE DATABASE IF NOT EXISTS MinorProjectDB")
cursorObject.execute("CREATE DATABASE IF NOT EXISTS MinorProjectDB")
print("Database created successfully")