from datetime import datetime
from flask import abort

# Функция для возврата формата времени в заданном формате
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# словарь со значениями Персонажей
PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    }
}
# Та самая функция для вызова со стороны сервера
def read_all():
    return list(PEOPLE.values())

def create_person(person):
    lname = person.get("lname")
    fname = person.get("fname")

    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp()
        }
        return PEOPLE[lname], 201
    else:
        abort(
            406,
            f"Person  with last name {lname} already exists"
        )

def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )