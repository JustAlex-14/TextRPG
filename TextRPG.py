
class Character:
    def __init__(self, health, weapon, strength, level):
        self.health = health
        self.weapon = weapon
        self.strength = strength 
        self.level = level
    
    def isAlive(self, health):
        if health <=0:
            print(self.name, " is dead!")
            return False
        else: return True

    def takeDamage(self, damageReceived, attacker):
        self.health = self.health - damageReceived
        if self.isAlive(self.health):
            print(attacker.name, " attacked ", self.type,". \n", 
                  self.type, " has ", self.health, " health.")
            
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

#TODO
#Fix type error
choice = input("Do you want to attack: (y/n)\n")
if choice == "y":
    playerDamage = dmgCalc(player.strength, player.weapon)
    enemy1.takeDamage(playerDamage, player)



   