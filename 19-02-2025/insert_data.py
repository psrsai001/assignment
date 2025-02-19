from main import cursor, db

cursor.execute(
    """
INSERT INTO students(name, age)
VALUES
('alice', 24),
('bob', 23),
('jhon', 25);
"""
)
cursor.execute("""SELECT * FROM students;""")
for row in cursor.fetchall():
    print(row)

cursor.close()
db.commit()
