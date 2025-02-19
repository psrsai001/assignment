import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="your_password", database="wipro"
)

if db.is_connected():
    print("connection success")

else:
    print("connection failed")

cursor = db.cursor()
