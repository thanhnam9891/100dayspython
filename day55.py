
import os, time, random
todo = []
fielExist = True

try:
   f = open("day55todo.txt","r")
   todo = eval(f.read())
except:
   fielExist = False

def add():
  time.sleep(1)
  os.system("cls")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")
