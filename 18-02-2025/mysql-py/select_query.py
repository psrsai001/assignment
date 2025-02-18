from main import cnx

cursor = cnx.cursor()

cursor.execute(
    """
SHOW DATABASES;
"""
)

for data in cursor.fetchall():
    print(data)
