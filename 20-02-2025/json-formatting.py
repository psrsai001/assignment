import json

data = {
    "first_name": "alice",
    "last_name": "jonathan",
    "age": 24,
}


def write_json_data():
    try:
        with open("create_data.json", "x") as f:
            json.dump(data, f, indent=2)
    except FileExistsError as e:
        print(e)


def read_json_data():
    try:
        with open("create_data.json", "r") as f:
            data = json.load(f)
            print(data)
    except FileNotFoundError as e:
        print(e)


write_json_data()
read_json_data()
