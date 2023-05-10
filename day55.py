
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
  name = input("aName > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("cls")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("cls")
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("cls")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
    
    menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    elif menu == "4":
        remove()
    else:
        break

    if fielExist:
        try:
          os.makedirs("day55backups")
        except:
          pass
        name = f"backup{random.randint(1,1000).txt}" 
        os.popen(f"cp day55todo.txt day55backups/{name}")
    
    f = open("day55todo.txt", "w") 
    f.write(str(todo)) 
    f.close()