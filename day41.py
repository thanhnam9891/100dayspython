website = {"name":None,"url":None, "description":None,"rate":None}
for name in website.keys():
  website[name] = input(f"{name}: ")
print()
for name, value in website.items():
  print(f"{name}: {value}")