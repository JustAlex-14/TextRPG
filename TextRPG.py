
class Character:
    def __init__(self, name, health, weapon, strength):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.strength = strength 

class Enemy:
    def __init__(self, type, health, weapon, strength):
        self.type = type
        self.health = health
        self.weapon = weapon
        self.strength = strength 

#Creating character
player = Character("Bob", 100, "Sword", 3)
print("Name: ", player.name, "\nHealth: ", player.health, "\nWeapon: ", player.weapon)  

#Creating Enemy 
enemy1 = Enemy("Skeleton", 50, "Dagger", 1.5)

#Calculate damage of an attack 
def dmgCalc(str, weapon):
    if weapon == "Sword":
        weaponDamage = 5
    elif weapon == "Axe":
        weaponDamage = 7
    elif weapon == "Dagger":
        weaponDamage = 3
    damage = str * weaponDamage
    return damage
   
def isAlive(enemy, health):
    if health <=0:
        print(enemy, " is dead!")
        return False
    else: return True
    
#Attack 
playerDamage = dmgCalc(player.strength, player.weapon)
enemy1.health = enemy1.health - playerDamage
if isAlive(enemy1.name, enemy1.health):
    print("Bob attacked a Skeleton. \nSkeleton has ", enemy1.health, " health.")
enemy1.health = enemy1.health - playerDamage
if isAlive(enemy1.name, enemy1.health):
    print("Bob attacked a Skeleton. \nSkeleton has ", enemy1.health, " health.")
enemy1.health = enemy1.health - playerDamage
if isAlive(enemy1.name, enemy1.health):
    print("Bob attacked a Skeleton. \nSkeleton has ", enemy1.health, " health.")
enemy1.health = enemy1.health - playerDamage
if isAlive(enemy1.name, enemy1.health):
    print("Bob attacked a Skeleton. \nSkeleton has ", enemy1.health, " health.")


    