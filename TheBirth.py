# birth of c12
import csv
import datetime
# csv file (database)
# collect date from databases
with open('Birthday.csv','r') as birth:
    rawData = []
    birth.readline()
    birth.readline()
    header = ['name','day','month','year']
    reader = csv.DictReader(birth, fieldnames=header)
    for row in reader:
        rawData.append(row)

def whoOld(age:int):
    result = []
    for person in rawData:
        birthDate = datetime.datetime(int(person["year"]), int(person["month"]), int(person["day"]))
        if birthDate > datetime.datetime.now():
            checkYear = datetime.datetime.now().year - age
        else:
            checkYear = datetime.datetime.now().year - age- 1
        if int(person["year"]) == checkYear:
            result.append(person["name"])
    return result

# def theOldest():
# def theYoungest():
# mangkorn response...

def countdowntobirth(name:str):
    person = next(person for person in rawData if person["name"] == name)
    birth = datetime.datetime(int(person["year"]), int(person["month"]), int(person["day"]))
    now = datetime.datetime.now()
    now = int(now.strftime("%j"))
    birth = int(birth.strftime("%j"))
    if birth >= now:
        return birth-now
    else:
        return 365+birth-now

def nearestBirthDay():
    people = [person["name"] for person in rawData]
    duration = float('inf')
    for person in people:
        if countdowntobirth(person) < duration:
            result = person
        duration = min(countdowntobirth(person), duration)
    return result


def whoBornInMonth(month:int):
    result = [person["name"] for person in rawData if int(person["month"]) == month]
    # result = []
    # for person in rawData:
    #     if person["month"] == month:
    #         result.append(person["name"])
    return result


# def iszodiac(person):
# def whozodiac(zodiac:string):

# month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]