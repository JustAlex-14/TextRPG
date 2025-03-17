
#Creating character
name = "Bob"
health = 100
weapon = "Sword"
strength = 3
print("Name: ", name, "\nHealth: ", health, "\nWeapon: ", weapon)  

#Creating Enemy 
enemy = "Skeleton"
e_health = 50
e_weapon = "Dagger"
e_strength = 1.5



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
   
def isAlive(enemy, e_health):
    if e_health <=0:
        print(enemy, " is dead!")
        return False
    else: return True
    
#Attack 
e_health = e_health - dmgCalc(strength, weapon)
if isAlive(enemy, e_health):
    print("Bob attacked a Skeleton. \nSkeleton has ", e_health, " health.")
e_health = e_health - dmgCalc(strength, weapon)
if isAlive(enemy, e_health):
    print("Bob attacked a Skeleton. \nSkeleton has ", e_health, " health.")
e_health = e_health - dmgCalc(strength, weapon)
if isAlive(enemy, e_health):
    print("Bob attacked a Skeleton. \nSkeleton has ", e_health, " health.")
e_health = e_health - dmgCalc(strength, weapon)
if isAlive(enemy, e_health):
    print("Bob attacked a Skeleton. \nSkeleton has ", e_health, " health.")