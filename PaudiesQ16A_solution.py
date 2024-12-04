import random

def goblin_encounter(user_name):
  global user_health #declaring the global variable in the context of the function
  damage = random.randint(1, 6)
  user_health = user_health - damage
  print (user_name,"encounters a goblin! The goblin attacks, dealing", damage,"damage.")

def health_potion():
    global user_health
    heal = random.randint(1,4)
    user_health = user_health + heal
    print("You found a health potion. You have been healed by", heal, "points.")
    
def dragon_encounter(user_name):
  global user_health #declaring the global variable in the context of the function
  damage = random.randint(1, 20)
  user_health = user_health - (5 + damage)
  print (user_name,"encounters a dragon! The dragon attacks, dealing", 5+damage,"damage.")

# Example usage:
user_name = input("Please enter your character's name: ")
print("Your character is called", user_name)
print("You encounter two paths (1) leads to a forest, (2) leads to a canyon.")
user_health = 100

validate = False

while validate == False:
    path = input("Which path do you choose 1 or 2? ")    
    if path == "1":
        goblin_encounter(user_name)
        print("Your health is", user_health)
        validate = True
    elif path == "2":
        dragon_encounter(user_name)
        health_potion()
        validate = True

print("Your health is", user_health)