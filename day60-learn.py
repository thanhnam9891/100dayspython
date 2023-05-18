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

difference = datetime.timedelta(days=14) # The difference I want

newDate = today + difference # Add today to the delta difference to see the date in 14 days time.

print(newDate)

holiday = datetime.date(year = 2022, month = 10, day = 30) # The date of my holiday

if holiday > today: # If my holiday is in the future
  print("Coming soon")
elif holiday < today: #If my holiday date has passed
  print("Hope you enjoyed it")
else: # If my holiday date is today
  print("HOLIDAY TIME!")