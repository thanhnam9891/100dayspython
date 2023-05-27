from replit import db
import datetime, os,time

def add():
  time.sleep(1)
  os.system("clear")
  timestamp=datetime.datetime.now()
  print(f"Created at: {timestamp}")
  new = input ("> ")
  db[timestamp] = new

def view():
  keys = db.keys()
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"{key} {db[key]}")

password = input("Password: ")
currentpassword = "nopass"

if password !=currentpassword:
  print("Wrong Password.")
  exit()
while True:
  os.system("clear")
  menu = input("1. Add\n2.View\n>")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  else:
    break