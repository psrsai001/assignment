from main import cursor, db

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS students(
id INT PRIMARY KEY AUTO_INCREMENT,
name CHAR(40) NOT NULL,
age INT(3) NOT NULL
);
"""
)
cursor.execute(
    """
SHOW tables;
"""
)
for row in cursor.fetchall():
    print(row)
db.commit()
