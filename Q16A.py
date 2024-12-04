import random

def goblin_encounter(user_name):
  global user_health #declaring the global variable in the context of the function
  damage = random.randint(1, 12)
  user_health = user_health - damage
  print (user_name,"encounters a goblin! The goblin attacks, dealing", damage,"damage.")

# Example usage:
user_name = "Adventurer"
user_health = 100
goblin_encounter(user_name)
print("Your health is", user_health)
