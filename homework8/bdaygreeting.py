from collections import defaultdict
from datetime import datetime


users = {
            "Arina" : "2002/07/09",
            "Andrew" : "1997/07/12",
            "Milla" : "2010/07/12",
            "Dima" : "1987/07/08",
            "Tony" : "1976/07/08"
}

def get_birthdays_per_week(users):
    birth = defaultdict(list)
    now = datetime.now()
    i = 0
    while i < 8:
        for name, birth_day in users.items():
            key_birth = (datetime.strptime(birth_day, "%Y/%m/%d"))
            date_birthday = datetime(year = now.year, month = key_birth.month, day = key_birth.day).strftime("%m/%d")
            now_birth = (datetime(year = now.year, month = now.month, day = now.day + i)).strftime("%m/%d")
            if now_birth in date_birthday:
                date_birthday = datetime(year = now.year, month =key_birth.month, day = key_birth.day).strftime("%A")
                birth[date_birthday].append(name)
        i += 1
    birth["Monday"].extend(birth["Sunday"])
    birth["Monday"].extend(birth["Saturday"])
    birth["Sunday"].clear()
    birth["Saturday"].clear()
    for key, value in birth.items():
        if len(value) <= 0:
            continue
        print(key, end=": ")
        print(*value, sep=", ")

get_birthdays_per_week(users)