import sys
import random

onOff = "Y"
has_begun_game= False;
location = (0, 0)
has_wallet = False
has_gun = False
has_seen_shirley = False
has_seen_shopkeeper = False

def print_intro(location):
    print("This game takes place on a 3x3 grid. Use (X, Y) coordinates\n
           to get around. You may turn on the debug to see where the items\n
           needed to win the game are.")
    print("  ")
    print("--------------------------------------------------------------------")


def print_location(location):
    if location == (0,0) and has_begun_game == False:
        print("--You are the Sheriff. Your archnemisis is Shirley\n"
              "  Spade the Outlaw and he has challenged you to a\n
                 shoot out at high noon. Find a gun or you might die!")
        print("  ")
        print("--Hint: Don't go to the middle of town unless you have a gun!")
        print("  ")
        print("----------------------------------------------------------------")
        print("You are in the middle of town. Type 'n' for north, 's' for\n"
              "south, 'e' for east, or 'w' for west.")
    elif location == (0,0) and has_begun_game == True:
        print("You are at the crossroads.")
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
    global wallet_location, gun_location, town_location
    wallet_location = get_random_location()
    town_location = None
    while town_location == None or town_location == wallet_location:
        town_location = get_random_location()
    gun_location = None
    print ("TURN ON DEBUG? Y/N: ")
    onOff = input()
  
    if onOff == "Y":
      while (gun_location == None or
        gun_location == town_location or
        gun_location == wallet_location):
          gun_location = get_random_location()
          print("The wallet is at: ", wallet_location)
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
    global wallet_location, gun_location, town_location
    if location == wallet_location:
        return do_wallet()
    elif location == gun_location:
        return do_gun()
    elif location == town_location:
        return do_highnoon()

def do_wallet():
    global has_wallet
    if has_wallet:
        print("--What are you waiting for? You have to get the gun before\n"
              "  high noon!")
    else:
        print("--You found a wallet. Maybe you can use this to get\n"
              "  another item?")
        has_wallet = True
    return False

def do_gun():
    global has_wallet, has_gun, has_seen_shirley, has_seen_shopkeeper
    if has_seen_shopkeeper:
        if has_gun:
            print("--The shopkeeper gratefully gives you the gun and snatches the wallet\n"
                  "  from your hands. She then kicks you out.")
            print("--You equip the gun. Now get to the middle of town, it's\n"
                  "  high noon!")
            has_gun = True
        else:
            print("--You shouldn't've come back if you didn't have the wallet.\n"
                  "--The shopkeeper is so annoyed with you that she grabs the gun and\n"
                  "  shoots you. You didn't even make it to high noon. Way to go.")
            print(" ")
            print("-----You Died-----")
            sys.exit()
    else:
        print("--You walk into the General Store and see the gun right away. You\n"
              "  reach for it, but the shopkeeper slams a knife down\n"
              "  into the wood in front of the gun.")
        print("--'You can have this gun if you find my missing wallet.\n"
              "   I lost it around town somewhere.'")
        print("--You agree and the shopkeeper kicks you out of her store.")
        has_seen_shopkeep = True
        
    return False

def do_highnoon():
    global has_wallet, has_gun, has_seen_shirley
    if has_gun:
        if has_seen_shirley:
            print("--You draw your gun as fast as you can, but this time\n"
                  "  Shirley was ready for you. You don't even get a chance\n"
                  "  to fire before you're dead.")
            print(" ")
            print("-----You Died-----")
        else:
            print("--You grab your gun and whip it out. You shoot as fast as you\n"
                  "  can and kill Shirley! The town thanks you.")
            print(" ")
            print("*~*~*~*~*~You Win!~*~*~*~*~*")
            sys.exit()
    else:
        if has_seen_shirley: 
            print("--Since you didn't get a weapon, Shirley draws his gun and shoots\n"
                  "  you.")
            print("--Good job, Shirley shot the Sheriff (but not the Deputy).")
            print(" ")
            print("-----You Died-----")
            sys.exit()
        else:
            print("--You walk into the middle of town. You see Shirley and are\n"
                  "  about to draw your gun when you realize you don't have one!")
            print("--You run away as fast as you can and Shirley warns you not to\n"
                  "  come back until you have a gun or he'll kill you!")
            has_seen_shirley = True
    return False
        
def print_intro(location)
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
