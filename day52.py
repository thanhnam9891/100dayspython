import time,os
orderlist = []

try:
    f=open("orderlist.txt","r") # Only need read permissions here
    orderlist = eval(f.read())
    f.close()
except Exception as errorload:
  print(errorload)

def prettyPrint():
  print()
  for row in orderlist:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

def add():
    try:
        quantity = int(input("How many pizza? > "))
    except:
        quantity = int(input("You must input a numerical character, try again. > "))
    size = input("What Size? (s/m/l) > ")
    name = input("Name please > ")
    if size == "s":
       total = round(3.99 * quantity)
    elif size == "m":
        total = round(5.99 * quantity)
    else:
       total = round(7.99 * quantity)
  
    row = [name, size, quantity,total]
    orderlist.append(row)
    print(f"Thanks {name}, your pizza is cost {total}")

def view():
  h1 = "Name"
  h2 = "Size"
  h3 = "Quantity"
  h4 = "Total"
  print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}")
  
  for row in orderlist:
    print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}")
  
while True:
  print("🌟Dave's Dodgy Pizzas🌟")
  print()
  option = input("1: Order Pizza\n2: View Order\n >")
  if option == "1":
    add()
  elif option == "2":
    view()
  else:
    break

  f = open("orderlist.txt", "w") 
  f.write(str(orderlist)) 
  f.close()