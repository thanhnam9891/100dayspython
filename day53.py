import time,os
inventory = []

try:
    f=open("inventory.txt","r") # Only need read permissions here
    inventory = eval(f.read())
    f.close()
except Exception as errorload:
  print(errorload)

def add():
    item = input("Input the item to add: > ")
    inventory.append(item)
    print(f"{item} has been added to your inventory.")

def view():
  search = input("Input the item to view: > ")
  quantity = inventory.count(search)
  if quantity > 0:
     print (f"You have {quantity} {search} in your inventory.")
  else:
     print(f"There is no {search} in your inventory.")

def remove():
   search = input("Input the item to remove: > ")
   if search in inventory:
      inventory.remove(search)
      print(f"You have removed {search} from your inventory.")
   else:
      print(f"There is no {search} in your inventory.")
  
while True:
    print("🌟RPG Inventory🌟")
    print()
    option = input("1: Add\n2: View\n3: Remove\n >")
    if option == "1":
        add()
    elif option == "2":
        view()
    elif option == "3":
       remove()
    else:
        print("Thank You.")
        break

    f = open("inventory.txt", "w") 
    f.write(str(inventory)) 
    f.close()