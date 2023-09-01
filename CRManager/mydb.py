import mysql.connector

# initialize mysql connection
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root1',
)

cur = db.cursor()

cur.execute("CREATE DATABASE crmdb")