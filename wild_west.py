import sys
import random

onOff = "Y"
location = (0, 0)
has_chicken = False
has_gun = False
has_seen_angel = False
has_seen_saia = False

def print_location(location):
    if location == (0,0):
        print("--Your name is Sarah the Ninja. Your archnemisis is Shirley\n"
              "  'Angel' Spade and he has challenged you to a shoot out at\n"
              "  high noon. Find a gun or you might die!")
        print("  ")
        print("You are in the middle of town. Type 'n' for north, 's' for\n"
              "south, 'e' for east, or 'w' for west.")
    elif location == (-1, 1):
        print("You are northwest of the crossroads.")
    elif location == (0, 1):
        print("You are north of the crossroads.")
    elif location == (1, 1):
        print("You are northeast of the crossroads.")
    elif location == (-1, 0):
        print("You are west of the crossroads.")
    elif location == (1, 0):
        print("You are east of the crossroads.")
    elif location == (-1, -1):
        print("You are southwest of the crossroads.")
    elif location == (0, -1):
        print("You are south of the crossroads.")
    elif location == (1, -1):
        print("You are southeast of the crossroads.")
    else:
        print("You're off the map!")

def get_random_location():
    while True:
        location = (random.randint(-1, 1),
            random.randint(-1, 1))
        if location != (0, 0):
            return location

def init_world(onOff):
    global chicken_location, gun_location, town_location
    chicken_location = get_random_location()
    town_location = None
    while town_location == None or town_location == chicken_location:
        town_location = get_random_location()
    gun_location = None
    print ("TURN ON DEBUG? Y/N: ")
    onOff = input()
  
    if onOff == "Y":
      while (gun_location == None or
        gun_location == town_location or
        gun_location == chicken_location):
          gun_location = get_random_location()
          print("The chicken is at: ", chicken_location)
          print("The gun is at: ", gun_location)
          print("The middle of town is at: ", town_location)
        
def move_player(command, location):
    if command == "n":
        if (location[1] == 1):
            print("You can't go that way!")
        else:
            location = (location[0], location[1] + 1)
    elif command == "s":
        if (location[1] == -1):
            print("You can't go that way!")
        else:
            location = (location[0], location[1] -1)
    elif command == "e":
        if (location[0] == 1):
            print("You can't go that way!")
        else:
            location = (location[0] + 1, location[1])
    elif command == "w":
        if (location[0] == -1):
            print("You can't go that way!")
        else:
            location = (location[0] - 1, location[1])
    elif command == "q":
        print("Goodbye!")
        sys.exit()
    else:
        print("\nSorry, I don't understand what you typed.")
        print("Try typing 'n' for north, 's' for south, 'e' for east, or 'w' for west.")
        print("Type 'q' to quit.")

    return location

def do_special_room(location):
    global chicken_location, gun_location, town_location
    if location == chicken_location:
        return do_chicken()
    elif location == gun_location:
        return do_gun()
    elif location == town_location:
        return do_highnoon()

def do_chicken():
    global has_chicken
    if has_chicken:
        print("--What are you waiting for? You have to get the gun before\n"
              "  high noon!")
    else:
        print("--You found a Golden Chicken. Maybe you can use this to get\n"
              "  another item?")
        has_chicken = True
    return False

def do_gun():
    global has_chicken, has_gun, has_seen_angel, has_seen_saia
    if has_seen_saia:
        if has_chicken:
            print("--Saia gratefully gives you the gun and snatches the chicken\n"
                  "  from your hands. She then kicks you out.")
            print("--You equip the gun. Now get to the middle of town, it's\n"
                  "  high noon!")
            has_gun = True
        else:
            print("--You shouldn't've come back if you didn't have the chicken.\n"
                  "--Saia is so annoyed with you that she grabs the gun and\n"
                  "  shoots you. You didn't even make it to high noon, you loser.")
            print(" ")
            print("-----You Died-----")
            sys.exit()
    else:
        print("--You walk into Saia's Shop and see the gun right away. You\n"
              "  reach for it, but Saia slams a (sharpened???) fork down\n"
              "  into the wood in front of the gun.")
        print("--'You can have this gun if you find me the Golden Chicken.\n"
              "   I really want chicken and waffles, but only with the best chicken.'")
        print("--You agree and Saia kicks you out of her store.")
        has_seen_saia = True
        
    return False

def do_highnoon():
    global has_chicken, has_gun, has_seen_angel
    if has_gun:
        if has_seen_angel:
            print("--You draw your gun as fast as you can, but this time\n"
                  "  Angel was ready for you. You don't even get a chance\n"
                  "  to fire before you're dead.")
            print(" ")
            print("-----You Died-----")
        else:
            print("--You grab your gun and whip it out. You shoot as fast as you\n"
                  "  can and kill Angel! The town thanks you.")
            print(" ")
            print("*~*~*~*~*~You Win!~*~*~*~*~*")
            sys.exit()
    else:
        if has_seen_angel: 
            print("--Since you didn't get a weapon, Angel draws his gun and shoots\n"
                  "  Sarah.")
            print("--Good job, you killed Sarah the Ninja.")
            print("--Shame on you  >:(")
            print(" ")
            print("-----You Died-----")
            sys.exit()
        else:
            print("--You walk into the middle of town. You see Angel and are\n"
                  "  about to draw your gun when you realize you don't have one!")
            print("--You run away as fast as you can and Angel warns you not to\n"
                  "  come back until you have a gun or he'll kill you!")
            has_seen_angel = True
    return False
        

init_world(onOff)

while True:
    print_location(location)
    back_to_middle = do_special_room(location)
    if back_to_middle:
        location = (0, 0)
        continue
    print("\nWhich direction do you wish to travel?")
    print("Type 'n' for north, 's' for south, 'e' for east or 'w' for west.")
    in_string = input()
    location = move_player(in_string, location)
    print()
