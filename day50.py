import os,time,random

print("🌟Idea Storage🌟")
print()

def clearscreen():
    time.sleep(2)
    os.system("cls")

while True:
    option=input("Add and idea or see a random idea? a/r. >")

    if option.lower() == "a":
        idea = input("Iput your idea. > ")
        f = open("my.ideas","+a")
        f.write(f"{idea}\n")
        f.close
        print("Nice! Your idea has been stored.")
        clearscreen()
    elif option.lower() == "r":
        f = open("my.ideas","r")
        list = f.read().split("\n")
        f.close()
        list.remove("")
        data=random.choice(list)
        print(data)
        clearscreen()
    else:
        print("Thank you!")
        break