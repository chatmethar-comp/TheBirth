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

# ใครบ้างที่อายุ...ปี
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

def countdowntobirth(name:str):
    name = name.capitalize()
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
    # เขียนแบบเดียวกับด้านล่างแต่เป็นการเขียนแบบ inline
    # result = []
    # for person in rawData:
    #     if person["month"] == month:
    #         result.append(person["name"])
    return result

def time_lived(name:str):
    for person in rawData:
        if name==person["name"]:
            actual = datetime.datetime.now() - datetime.datetime(int(person["year"]), int(person["month"]), int(person["day"]))
            daylived=actual.days
    return daylived

def check_date(days:int):
    for person in rawData:
        day_check=time_lived((person["name"]))
        if days==day_check:
            return person["name"]

def theOldest():
    list_day=[]
    for person in rawData:
        day=time_lived(person["name"])
        list_day.append(day)
        list_day.sort()
    return check_date(list_day[-1])

def theYoungest():
    list_day = []
    for person in rawData:
        day = time_lived(person["name"])
        list_day.append(day)
        list_day.sort()
    return check_date(list_day[0])

def iszodiac(name:str):
    for person in rawData:
        if name==person["name"]:
            day=int(person["day"])
            month=int(person["month"])
            if month==1:
                if day>=21: return "Taurus"
                else: return "Aries"
            if month==2:
                if day>=20: return "Pisces"
                else: return "Taurus"
            if month==3:
                if day>=21: return "Aquarius"
                else: return "Pisces"
            if month==4:
                if day>=21: return "Capricorn"
                else: return "Aquarius"
            if month==5:
                if day>=22: return "Gemini"
                else: return "Capricorn"
            if month==6:
                if day>=22: return "Cancer"
                else: return "Gemini"
            if month==7:
                if day>=24: return "Leo"
                else: return "Cancer"
            if month==8:
                if day>=24: return "Virgo"
                else: return "Leo"
            if month==9:
                if day>=24: return "Libra"
                else: return "Virgo"
            if month==10:
                if day>=24: return "Scorpio"
                else: return "Libra"
            if month==11:
                if day>=23: return "Sagittarius"
                else: return "Scorpio"
            if month==12:
                if day>=22: return "Aries"
                else: return "Sagittarius"

def whozodiac(zodiac:str):
    # zodiacs = ["aries", "taurus", "pisces", "aquarius", "capricorn", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius"]
    result = []
    for person in rawData:
        if iszodiac(person["name"]) == zodiac:
            result.append(person["name"])
    return result
# month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]