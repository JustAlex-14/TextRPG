
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

    #Calculate damage of an attack 
    def dmgCalc(self, str, weapon):
        if weapon == "Sword":
            weaponDamage = 5
        elif weapon == "Axe":
            weaponDamage = 7
        elif weapon == "Dagger":
            weaponDamage = 3
        damage = str * weaponDamage
        return damage
    
    def attack(self, victim):
        dmgDealt = self.dmgCalc(self.strength, self.weapon)
        victim.health = victim.health - dmgDealt
        if self.isAlive(self.health):
            print(self.name, " attacked ", victim.type,". \n",
                  victim.type, " has ", victim.health, " health.")
            
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

#Creating Enemies
enemy1 = Enemy("Skeleton", 50, "Dagger", 1.5, 1)
enemy2 = Enemy("Orc", 75, "Axe", 2, 1)



choice = input("Do you want to attack: (y/n)\n")
if choice == "y":
    chooseEnemy = int(input("Which enemy do you want to attack? - Select number\n 1. Skeleton\n 2. Orc\n"))
    if chooseEnemy == 1:
        player.attack(enemy1)
    elif chooseEnemy == 2:
        player.attack(enemy2)
