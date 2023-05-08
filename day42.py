beast = {"name":None,"type":None, "special move":None,"hp":None,"mp":None}
for name in beast.keys():
  beast[name] = input(f"Input your beast's {name}: ").strip().lower()
print()
if beast["type"] == "earth":
    print("\033[31m", end="")
elif beast["type"] == "fire":
   print("\033[32m", end="")
elif beast["type"] == "air":
   print("\033[33m", end="")
elif beast["type"] == "water":
   print("\033[34m", end="")
elif beast["type"] == "spirit":
  print("\033[35m", end="")
  
print(f"Your beast is called {beast['name']}. It is an {beast['type']} beast with a special move of {beast['special move']}.")