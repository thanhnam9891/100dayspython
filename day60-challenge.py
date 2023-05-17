import datetime

myDate = datetime.date(year=2023, month=5, day=16)
today = datetime.date.today()

print(myDate)
print(today)

if myDate==today:
    print("OK")
else:
    print("none")

day = int(input("Day: ")) # Get all input as numbers. We're not at text input for months yet.
month = int(input("Month: "))
year = int(input("Year: "))

date = datetime.date(year, month, day)

print(date)