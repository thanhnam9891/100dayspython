import datetime

print("🌟Event Countdown Timer🌟")

event= input("Event Name > ")
eventday = int(input("Day: ")) # Get all input as numbers. We're not at text input for months yet.
eventmonth = int(input("Month: "))
eventyear = int(input("Year: "))
eventdate = datetime.date(eventyear, eventmonth, eventday)
today = datetime.date.today()

difference = eventdate-today
difference = difference.days

if difference == 0:
    message = "Today is your birthday. Happy birthday to you."
elif difference < 0:
    message = "Hope you enjoyed your bithday"
else:
    message = f"Your birthday is {difference} day(s) left."

print(message)