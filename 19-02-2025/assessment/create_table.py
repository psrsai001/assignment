from main import cursor, db

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS students(
id INT PRIMARY KEY AUTO_INCREMENT,
roll_no INT NOT NULL,
subject VARCHAR(40) NOT NULL,
result  ENUM('PASS', 'FAIL') DEFAULT 'PASS'
);
"""
)
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS customers(
id INT PRIMARY KEY AUTO_INCREMENT,
trans INT NOT NULL,
balance INT NOT NULL,
acc_type  ENUM('PREMIUM', 'NORMAL') DEFAULT 'NORMAL'
);
"""
)


cursor.execute("SHOW TABLES;")
for row in cursor.fetchall():
    print(row)
cursor.close()
