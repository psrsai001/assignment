import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="your_password", database="assessment"
)

cursor = db.cursor()
