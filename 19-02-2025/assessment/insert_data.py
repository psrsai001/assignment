from main import cursor, db

query = """
INSERT INTO students(roll_no, subject, result)
VALUES
(%s, %s, %s);
"""


# data = [(1, "Maths", 25), (1, "Physics", 90), (1, "Chemistry", 13)]
#
# data = list(map(lambda x: (x[0], x[1], "PASS" if x[2] >= 25 else "FAIL"), data))
# print(data)
#
def insert(roll_no: int, sub: str, marks: int):
    result = "PASS" if marks >= 25 else "FAIL"
    cursor.execute(query, (roll_no, sub, result))

    for row in cursor.fetchall():
        print(row)


def select():
    cursor.execute("SELECT * FROM students;")
    for row in cursor.fetchall():
        print(row)


while True:
    print("1) insert")
    print("2) display")
    print("3) exit")
    n = int(input("Enter your option: "))
    match n:
        case 1:
            roll_no = int(input("Enter roll_no: "))
            sub = input("Enter subject: ")
            marks = int(input("Enter marks: "))
            insert(roll_no, sub, marks)
        case 2:
            select()
        case 3:
            break
cursor.close()
db.commit()
