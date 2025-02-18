from datetime import datetime

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