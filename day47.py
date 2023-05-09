import os, time, random

toptrumps = {}
toptrumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
toptrumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
toptrumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
toptrumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

def clearscreen():
    time.sleep(3)
    os.system("clear")

def prettyPrint():
  print("Characters: \n\n")
  
  for key, value in toptrumps.items():
    # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
    print(key)

while True:
  clearscreen()
  print("TOP TRUMPS")
  print("===========")
  prettyPrint()
  yourchoice = input("Pick your character \n>")
  computerchoice = random.choice(list(toptrumps.keys()))
  print("Computer has picked ",computerchoice)
  yourstat = input("Choose your stat: Intelligence, Speed, Guile or Baldness Level \n>")
  print(f"{yourchoice}:{toptrumps[yourchoice][yourstat]}")
  print(f"{computerchoice}:{toptrumps[computerchoice][yourstat]}")
  if toptrumps[yourchoice][yourstat] > toptrumps[computerchoice][yourstat]:
    print(yourchoice," wins")
  elif toptrumps[yourchoice][yourstat] < toptrumps[computerchoice][yourstat]:
    print(computerchoice," wins")
  else:
    print("Draw")