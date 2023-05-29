import os

class character():
    name = None
    hp = 100
    mp = 100

    def __init__(self,name):
        self.name = name

    def setStats(self,hp,mp):
        self.hp = hp
        self.mp = mp
    
    def print(self):
        print(f"Name:{self.name}\nHealth: {self.hp}\nMagic Points: {self.mp}\n")

class player(character):
    user = None
    lives = None
    alive = 3

    def __init__(self, user):
        self.name = "Player"
        self.user = user

    def print(self):
        print(f"Player\nName:{self.user}\nHealth: {self.hp}\nMagic Points: {self.mp}\nLives: {self.lives}\nAlive?: {self.alive}\n")

    def isAlived(self):
        if self.alive>0:
            return True
        else:
            return False

class enemy(character):
    type = None
    strength = None

    def __init__(self, name,type,strength):
        self.name = name
        self.type=type
        self.strength = strength

    def print(self):
        print(f"Name:{self.name}\nHealth: {self.hp}\nMagic Points: {self.mp}\nType:{self.type}\nStrength:{self.strength}\n")

class orc(enemy):
    speed = None

    def __init__(self, speed):
        self.speed = speed
        self.type = 'Orc'
        self.name = 'Enemy'
        self.strength=200

    def print(self):
        print(f"Name:{self.name}\nHealth: {self.hp}\nMagic Points: {self.mp}\nType:{self.type}\nStrength:{self.strength}\nSpeed: {self.speed}\n")
    
class vampire(enemy):
    day = True

    def __init__(self, day):
        self.tracker = day
        self.type = 'Vampire'
        self.name = 'Enemy'
        self.strength = 150

    def print(self):
        print(f"Name:{self.name}\nHealth: {self.hp}\nMagic Points: {self.mp}\nType:{self.type}\nStrength:{self.strength}\nDay/Night?: {self.day}\n")

os.system("clear")
print("🌟Generic RPG🌟\n")
david = player("David")
david.print()

boris = vampire(False)
boris.print()

bill = orc(80)
bill.print()
