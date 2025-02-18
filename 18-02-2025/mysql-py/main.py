import mysql.connector

# Establish a connection
connection = mysql.connector.connect(
    host="localhost",  # Host where MySQL is running
    user="root",  # Your MySQL username
    password="your_password",  # Your MySQL password
)

# Check if the connection was successful
if connection.is_connected():
    print("Successfully connected to MySQL!")

# Create a cursor to execute queries
cursor = connection.cursor()

# Example: Create a simple query
cursor.execute("SHOW DATABASES")

# Fetch and print the result
for db in cursor.fetchall():
    print(db)

# Clean up: Close the cursor and connection
cursor.close()
connection.close()
