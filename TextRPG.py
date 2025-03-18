
class Character:
    def __init__(self, health, weapon, strength, level):
        self.health = health
        self.weapon = weapon
        self.strength = strength 
        self.level = level

class Player(Character):
    def __init__(self, name, health, weapon, strength, level):
        super().__init__(health, weapon, strength, level)
        self.name = name   

class Enemy(Character):
    def __init__(self, type, health, weapon, strength, level):
        super().__init__(health, weapon, strength, level)
        self.type = type

#Creating character
player = Player("Bob", 100, "Sword", 3, 1)
print("Name: ", player.name, "\nHealth: ", player.health, "\nWeapon: ", player.weapon)  

#Creating Enemy 
enemy1 = Enemy("Skeleton", 50, "Dagger", 1.5, 1)

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


choice = input("Do you want to attack: (y/n)\n")
if choice == "y":
    playerDamage = dmgCalc(player.strength, player.weapon)
    enemy1.health = enemy1.health - playerDamage
    if isAlive(enemy1.type, enemy1.health):
        print("Bob attacked a Skeleton. \nSkeleton has ", enemy1.health, " health.")

   