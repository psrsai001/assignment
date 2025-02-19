from main import cursor, db

query = """
INSERT INTO customers(trans, balance, acc_type)
VALUES
(%s, %s, %s);
"""


def insert(trans: int, balance: int):
    acc_type = "PREMIUM" if balance >= 10_000 else "NORMAL"
    cursor.execute(query, (trans, balance, acc_type))

    for row in cursor.fetchall():
        print(row)


def select():
    cursor.execute("SELECT * FROM customers;")
    for row in cursor.fetchall():
        print(row)


while True:
    print("1) insert")
    print("2) display")
    print("3) exit")
    n = int(input("Enter your option: "))
    match n:
        case 1:
            trans = int(input("Enter trans: "))
            balance = int(input("Enter balance: "))
            insert(trans, balance)
        case 2:
            select()
        case 3:
            break
cursor.close()
db.commit()
