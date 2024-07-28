import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Pj@123456'
)
# database = mysql.connector.connect(
#     host = 'minorprojectdb.cvemqsvgrfqo.eu-north-1.rds.amazonaws.com',
#     user = 'root',
#     password = 'parnjainthegreat'
# )



#prepare a cursor object using cursor() method
cursorObject = database.cursor()

#Createa a database
# cursorObject.execute("CREATE DATABASE IF NOT EXISTS MinorProjectDB")
cursorObject.execute("CREATE DATABASE IF NOT EXISTS MinorProjectDB")
print("Database created successfully")