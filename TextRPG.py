
class Character:
    def __init__(self, health, weapon, strength, level):
        self.health = health
        self.weapon = weapon
        self.strength = strength 
        self.level = level
    
    def isAlive(self):
        if self.health <=0:
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
    
    #TODO 
    #Remove enemy from list when killed 
    def attack(self, victim):
        dmgDealt = self.dmgCalc(self.strength, self.weapon)
        victim.health = victim.health - dmgDealt
        if victim.isAlive():
            print(self.name, "attacked", victim.type,". \n",
                  victim.type, "has", victim.health, "health.")
        elif not victim.isAlive():
            print(self.name, "killed", victim.type,".")

class Player(Character):
    def __init__(self, name, health, weapon, strength, level, coins):
        super().__init__(health, weapon, strength, level)
        self.name = name   

class Enemy(Character):
    def __init__(self, type, health, weapon, strength, level):
        super().__init__(health, weapon, strength, level)
        self.type = type

#Creating character
player = Player("Bob", 100, "Sword", 3, 1, 0)
#print("Name: ", player.name, "\nHealth: ", player.health, "\nWeapon: ", player.weapon)  

#Creating Enemies
#TODO 
#Return skeleton's health back to 50 after testing
enemy1 = Enemy("Skeleton", 5, "Dagger", 1.5, 1)
enemy2 = Enemy("Orc", 75, "Axe", 2, 1)
enemies = [enemy1, enemy2]

def attackSequence():
    print("Which enemy do you want to attack? - Select number\n")
    for x in enemies:
        print(enemies.index(x)+1,"-", x.type)
    chooseEnemy = int(input("\n"))-1
    player.attack(enemies[chooseEnemy])
    if enemies[chooseEnemy].isAlive() == False: 
        enemies.pop((chooseEnemy))
    attackAgain = input("Do you want to attack again? (y/n)\n")
    if attackAgain == "y": 
        attackSequence()
        
choice = input("Do you want to attack: (y/n)\n")
if choice == "y":
    attackSequence()

#Room 1 Plan:
##Skeleton and orc 
##Skeleton throws a dagger at player landing in the doorframe beside player's head 
##Ask player if they want to fight or retreat 
##if retreat, random chance of success, low odds of success
##engage in battle, give player first attack, choose who they want to attack
##keep fighting till both are dead 
##take in turns for player and enemies to attack 
##once enemies are dead, allow player to explore the room:
###chest with health potion - inventory system needs to be built 
###corpse in the corner of the room - if examined, will find a small bag with gold coins - wallet system i.e.attribute added to player class
###loot bodies - dagger from skeleton and rusty key from orc 
###doorway leading to room 2 
###guard action on your turn instead of an attack - random chance of parry, low odds - random chance of guard failing, low odds 
