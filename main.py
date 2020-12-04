import sys
import matplotlib.pyplot as plt

from time import sleep

words = "Narrator: You wake up in a forest and you see a village in the distance and you need to get there."
for char in words:
    # sleep(0.05)
    sys.stdout.write(char)
slot1 = "Nothing"
slot2 = "Nothing"
slot3 = "Nothing"
slot4 = "Nothing"
slot5 = "Nothing"
slot6 = "Nothing"
slot7 = "Nothing"
slot8 = "Nothing"
slot9 = "Nothing"
x1 = 0
y2 = 0
Villagex = 3
Villagey = 4
bal = 60
the_blacksmithx = 3
the_blacksmithy = 6
the_armorsmithx = 4
the_armorsmithy = 6
the_chiefx = 5
the_chiefy = 6
blacksmithtimes = 0
villagetimes = 0
chieftimes = 0
health = 10
armorsmithtimes = 0
Chainmailhelmet = False
Chainmailchestplate = False
Chainmailleggings = False
Chainmailboots = False
Atvillage = False
Adventuretimes = 0
Amtmoved = 0
Day = 1
BasicSword = False
BasicAxe = False
BasicBow = False
Bothweapons = False


def training():
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global BasicSword
    global BasicAxe
    global BasicBow
    global Bothweapons
    print("Narrator: I didn't want to have to do this, but I stopped time so I can teach you how to fight.")
    if slot1 != "Nothing":
        if slot1 == "Basic Sword":
            BasicSword = True
        if slot1 == "Basic Axe":
            BasicAxe = True
        if slot1 == "Basic Bow":
            BasicBow = True
    if slot2 != "Nothing":
        if slot2 == "Basic Sword":
            BasicSword = True
        if slot2 == "Basic Axe":
            BasicAxe = True
        if slot2 == "Basic Bow":
            BasicBow = True
    if slot3 != "Nothing":
        if slot3 == "Basic Sword":
            BasicSword = True
        if slot3 == "Basic Axe":
            BasicAxe = True
        if slot3 == "Basic Bow":
            BasicBow = True
    if slot4 != "Nothing":
        if slot4 == "Basic Sword":
            BasicSword = True
        if slot4 == "Basic Axe":
            BasicAxe = True
        if slot4 == "Basic Bow":
            BasicBow = True
    if slot5 != "Nothing":
        if slot4 == "Basic Sword":
            BasicSword = True
        if slot4 == "Basic Axe":
            BasicAxe = True
        if slot5 == "Basic Bow":
            BasicBow = True
    if slot6 != "Nothing":
        if slot6 == "Basic Sword":
            BasicSword = True
        if slot6 == "Basic Axe":
            BasicAxe = True
        if slot6 == "Basic Bow":
            BasicBow = True
    if slot7 != "Nothing":
        if slot4 == "Basic Sword":
            BasicSword = True
        if slot4 == "Basic Axe":
            BasicAxe = True
        if slot4 == "Basic Bow":
            BasicBow = True
    if slot8 != "Nothing":
        if slot4 == "Basic Sword":
            BasicSword = True
        if slot4 == "Basic Axe":
            BasicAxe = True
        if slot4 == "Basic Bow":
            BasicBow = True
    if slot9 != "Nothing":
        if slot4 == "Basic Sword":
            BasicSword = True
        if slot4 == "Basic Axe":
            BasicAxe = True
        if slot4 == "Basic Bow":
            BasicBow = True
    if BasicSword:
        print("Ah, I see you have a basic sword good weapon for a mighty hero like yourself.")
    if BasicAxe:
        if BasicSword:
            print("Ah, I see you also have a basic axe good for damage though it has a big delay.")
            Bothweapons = True
        if not BasicSword:
            print("Ah, I see you have a basic axe good for damage though it has a big delay.")
    if BasicBow:
        if not BasicAxe and not BasicSword:
            print("Ah, I see you have a basic bow good for distance not the best damage though.")
        if BasicSword and not Bothweapons:
            print("Ah, I see you also have a basic bow good for distance not the best damage though.\n"
                  "Sword and bow is a very good match no one will be able to defend from you.")
        if BasicAxe and not Bothweapons:
            print("Ah, I see you also have a basic bow good for distance not the best damage though.\n"
                  "Axe and bow is not the best duo, but we will make do.")
        if Bothweapons:
            print("Ah, I see you also have a basic bow good for distance not the best damage though."
                  "All three weapons that was an interesting choice we'll see how that goes.")
    if BasicAxe and not BasicSword and not BasicBow:
        print("When you're fighting you first move one place in any direction or don't move at all. When you're "
              "fighting with your axe you have to be right in front of the enemy. And with your axe you have to wait"
              " 3 turns in between each time you use your axe. In these turns you can either move or attack with"
              " another weapon. Oh, it appears you don't have any other weapons. Well it might take a while, but"
              "you'll be able to defeat your enemies. Once you're done with your turn your enemy will go. ")
    if BasicSword and not BasicAxe and not BasicBow:
        print("When you're fighting you first move one place in any direction or don't move at all. When you're "
              "fighting with your sword you have to be right in front of the enemy. And with your sword you have to "
              "wait 2 turns in between each time you use your sword. In these turns you can either move or attack with"
              " another weapon. Oh, it appears you don't have any other weapons. Well it might take a while, but"
              "you'll be able to defeat your enemies. Once you're done with your turn your enemy will go. ")
    if BasicBow and not BasicAxe and not BasicBow:
        print("When you're fighting you first move one place in any direction or don't move at all. When you're "
              "fighting with your bow you can be up to 3 places away. And with your bow you only have to "
              "wait 1 turn in between each time you use your bow. In this turn you can either move or attack with"
              " another weapon. Oh, it appears you don't have any other weapons. Well it might take a while, but"
              "you'll be able to defeat your enemies. Once you're done with your turn your enemy will go. ")
    if BasicAxe and BasicBow and not BasicSword:
        print("When you're fighting you first move one place in any direction or don't move at all. When you're "
              "fighting with your axe you have to be right in front of the enemy. And with your axe you have to "
              "wait 3 turns in between each time you use your axe. In these turns you can either move or attack "
              "with another weapon. Once you're done with your turn your enemy will go.")
        sleep(5)
        print("When you're fighting with your bow you can be up to 3 places away. And with your bow you only have "
              "to wait 1 turn in between each time you use your bow. These two will make a very good duo and it "
              "shouldn't take long to defeat your enemy.")
    if BasicSword and BasicBow and not BasicAxe:
        print("When you're fighting you first move one place in any direction or don't move at all. When you're "
              "fighting with your bow you can be up to 3 spaces away. And with your bow you only have to "
              "wait 1 turn in between each time you use your bow. In these turns you can either move or attack "
              "with another weapon. Once you're done with your turn your enemy will go.")
        sleep(5)
        print("When you're fighting with your axe you have to be right in front of your enemy. And with your axe you "
              "have to wait 3 turns in between each time you use your axe. These two will make a very good duo and "
              "it shouldn't take long to defeat your enemy.")
    if BasicAxe and BasicSword and not BasicBow:
        print("When you're fighting you first move one place in any direction or don't move at all. When you're "
              "fighting with your axe you have to be right in front of the enemy. And with your axe you have to "
              "wait 3 turns in between each time you use your axe. In these turns you can either move or attack "
              "with another weapon. Once you're done with your turn your enemy will go.")
        sleep(5)
        print("When you're fighting with your sword you have to be right in front of your enemy. And with your sword "
              "you have to wait 2 turns in between each time you use your sword. These two don't make the best duo, but"
              "as long as you have good armor you should do fine.")
    if BasicAxe and BasicBow and BasicSword:
        print("When you're fighting you first move one place in any direction or don't move at all. When you're "
              "fighting with your axe you have to be right in front of the enemy. And with your axe you have to "
              "wait 3 turns in between each time you use your axe. In these turns you can either move or attack "
              "with another weapon. Once you're done with your turn your enemy will go.")
        sleep(5)
        print("When you're fighting with your sword you have to be right in front of your enemy. And with your sword "
              "you have to wait 2 turns in between each time you use your sword.")
        sleep(5)
        print("When you're fighting with your bow you can be up to 3 places away. And with your bow you only have "
              "to wait 1 turn in between each time you use your bow. These three will make a very good trio and as "
              "long as you do it right you will get an easy victory.")


def the_realadventure():
    global x1
    global y2
    global Adventuretimes
    Adventuretimes = Adventuretimes+1
    if Adventuretimes == 1:
        print("Narrator: Welcome to the adventure you can move 3 spaces a day until you have to sleep. If you check the"
              " map you will see where you are and how far the final boss is. You will be"
              " walking through a dark forest so watch out for any obstacles that might come your way. \nOnce you get"
              " to the final boss I will teach you how to fight. Hopefully I don't have to teach you any earlier. ")
        y2 = 7
        x1 = 5
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global Villagex
    global Villagey
    global Amtmoved
    global Day
    if Amtmoved == 3:
        Amtmoved = 0
        Day = Day+1
    if Day == 2:
        print("Welcome to Day 2, nothing seems to have happened and you watch the sun rise behind the trees. You can't"
              " see anything, but you feel like something is watching you.")
    if Day == 3:
        print("Before you able to go to sleep on the night of day 2 you look at the moon and see it is a full moon that"
              " night, then you hear a low growling sound and from seemingly out of nowhere a werewolf jumps out at "
              "you, but before it can reach you it stops in mid-air.")
        training()
    main = input("type an action or help > ")
    if main == "dev":
        dev_mode()
    if main == "Move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
    if main == "move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
    if main == "Drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_realadventure()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_realadventure()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_realadventure()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_realadventure()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_realadventure()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_realadventure()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_realadventure()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_realadventure()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_realadventure()
    if main == "drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_realadventure()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_realadventure()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_realadventure()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_realadventure()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_realadventure()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_realadventure()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_realadventure()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_realadventure()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_realadventure()
    if main == "Inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_realadventure()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_realadventure()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_realadventure()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_realadventure()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_realadventure()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_realadventure()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_realadventure()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_realadventure()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_realadventure()
    if main == "inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_realadventure()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_realadventure()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_realadventure()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_realadventure()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_realadventure()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_realadventure()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_realadventure()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_realadventure()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_realadventure()
    if main == "Map":
        # x-axis values
        x = [x1]
        # y-axis values
        y = [y2]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(10, 11, label="The Final Boss", color="green",
                    marker=".", s=30)

        # x-axis label
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Map')
        # showing legend
        plt.legend()

        # function to show the plot
        plt.show()
        the_realadventure()
    if main == "map":
        # x-axis values
        x = [x1]
        # y-axis values
        y = [y2]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(10, 11, label="The Final Boss", color="green",
                    marker=".", s=30)

        # x-axis label
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Map')
        # showing legend
        plt.legend()

        # function to show the plot
        plt.show()
        the_realadventure()
    if main == "Help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nThis is all not case sensitive")
        the_realadventure()
    if main == "help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nThis is all not case sensitive")
        the_realadventure()
    if main == "balance":
        print("bal")
        the_realadventure()
    if main == "Balance":
        print("bal")
        the_realadventure()
    else:
        print("Didn't work try again")
        the_realadventure()


def the_adventure():
    print("The Chief: Hello traveler, for the past few years our village has been sorrounded by formidable monsters,"
          " which prevent access in and out of the village. They have let us live in peace and in return we don't try"
          " and disrupt their business. It has stopped the village from expanding and in a few years there will be no"
          " village. If you defeat their boss at the top of the mountain then you will be in control of the monsters"
          " and free our village. While fighting type health to see how much health you have left if this drops to or "
          "below zero then you have to restart. It is automatically at 10 hearts. This challenge is not for the weak "
          "and you must make sure you are up for the task.")
    continue1 = input("Would you like to start the adventure?: ")
    if continue1 == "Yes":
        the_realadventure()
    if continue1 == "yes":
        the_realadventure()
    else:
        the_village()


def the_chief():
    global y2
    global chieftimes
    chieftimes = chieftimes + 1
    if chieftimes == 1:
        print("Hello, traveler welcome to my village where you can buy equipment for your adventures there is a "
              "blacksmith to buy weapons and an armorsmith to buy armor. You can buy from them using coins, "
              "but since you don't seem to have any I will give you 400 coins to start with. You can come back "
              "to me when you are ready to start your adventure. Have fun shopping.")
        global bal
        bal = 400
        y2 = y2 - 1
        the_village()
    else:
        print("Welcome back traveler are you ready to start your adventure")
        start = input("Yes or No: ")
        if start == "Yes":
            the_adventure()
        if start == "yes":
            the_adventure()
        else:
            print("Ok you can keep shopping.")
            y2 = y2-1
            the_village()


def the_armorsmith():
    global x1
    global y2
    if x1 != 4 and y2 != 6:
        the_village()
    global armorsmithtimes
    armorsmithtimes = armorsmithtimes + 1
    if armorsmithtimes == 1:
        print("Welcome to the armorsmith where you can buy armor to defend yourself from your enemies type armorsmith "
              "to talk to the armorsmith.")
    else:
        print("Welcome back to the armorsmith where you can buy your armor to defend yourself remember you can type"
              "armorsmith to talk to the armorsmith.")
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global Villagex
    global Villagey
    global bal
    global Chainmailhelmet
    global Chainmailleggings
    global Chainmailchestplate
    global Chainmailboots
    main = input("type an action or help > ")
    if main == "dev":
        dev_mode()
    if main == "Move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            the_game()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_game()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_game()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_armorsmith()
    if main == "move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            the_game()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_game()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_game()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_armorsmith()
    if main == "Drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_game()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_game()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_game()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_game()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_game()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_game()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_armorsmith()
    if main == "drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_game()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_game()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_game()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_game()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_game()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_game()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_armorsmith()
    if main == "Inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_game()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_game()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_game()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_game()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_game()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_game()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_game()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_game()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_armorsmith()
    if main == "inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_game()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_game()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_game()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_game()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_game()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_game()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_game()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_game()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_armorsmith()
    if main == "Map":
        # x-axis values
        x = [x1]
        # y-axis values
        y = [y2]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(the_blacksmithx, the_blacksmithy, label="The Blacksmith", color="green",
                    marker=".", s=30)
        plt.scatter(the_armorsmithx, the_armorsmithy, label="The Armorsmith", color="green",
                    marker="P", s=30)
        plt.scatter(the_chiefx, the_chiefy, label="The Chief", color="green",
                    marker="D", s=30)

        # x-axis label
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Map')
        # showing legend
        plt.legend()

        # function to show the plot
        plt.show()
        the_armorsmith()
    if main == "map":
        # x-axis values
        x = [x1]
        # y-axis values
        y = [y2]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(the_blacksmithx, the_blacksmithy, label="The Blacksmith", color="green",
                    marker=".", s=30)
        plt.scatter(the_armorsmithx, the_armorsmithy, label="The Armorsmith", color="green",
                    marker="P", s=30)
        plt.scatter(the_chiefx, the_chiefy, label="The Chief", color="green",
                    marker="D", s=30)

        # x-axis label
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Map')
        # showing legend
        plt.legend()

        # function to show the plot
        plt.show()
        the_armorsmith()
    if main == "Help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nThis is all not case sensitive")
        the_armorsmith()
    if main == "help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nThis is all not case sensitive")
        the_armorsmith()
    if main == "balance":
        print("bal")
        the_armorsmith()
    if main == "Balance":
        print("bal")
        the_armorsmith()
    if main == "Shop":
        print("Armor:               Stats:          Cost:\n"
              "Chainmail Helmet     2 Protection    40 coins\n"
              "Chainmail Chestplate 2 Protection    40 coins\n"
              "Chainmail Leggings   2 Protection    40 coins\n"
              "Chainmail Boots      2 Protection    40 coins")
        item = input("What would you like to buy or type anything to not buy anything: ")
        if item == "Chainmail Helmet":
            if bal == 40:
                bal = bal-40
                Chainmailhelmet = True
                print("You now have a chainmail helmet.")
                the_armorsmith()
            else:
                print("You don't have enough coins")
                the_armorsmith()
        if item == "chainmail helmet":
            if bal == 40:
                bal = bal-40
                Chainmailhelmet = True
                print("You now have a chainmail helmet.")
                the_armorsmith()
            else:
                print("You don't have enough coins")
                the_armorsmith()
        if item == "Chainmail Chestplate":
            if bal == 40:
                bal = bal - 40
                Chainmailchestplate = True
                print("You now have a chainmail chestplate.")
                the_armorsmith()
            else:
                print("You don't have enough coins")
                the_armorsmith()
        if item == "chainmail chestplate":
            if bal == 40:
                bal = bal - 40
                Chainmailchestplate = True
                print("You now have a chainmail chestplate.")
                the_armorsmith()
            else:
                print("You don't have enough coins")
                the_armorsmith()
        if item == "Chainmail Leggings":
            if bal == 40:
                bal = bal - 40
                Chainmailleggings = True
                print("You now have a chainmail leggings.")
                the_armorsmith()
            else:
                print("You don't have enough coins")
                the_armorsmith()
        if item == "chainmail leggings":
            if bal == 40:
                bal = bal - 40
                Chainmailleggings = True
                print("You now have a chainmail leggings.")
                the_armorsmith()
            else:
                print("You don't have enough coins")
                the_armorsmith()
        if item == "Chainmail Boots":
            if bal == 40:
                bal = bal - 40
                Chainmailboots = True
                print("You now have a chainmail boots.")
                the_armorsmith()
            else:
                print("You don't have enough coins")
                the_armorsmith()
        if item == "chainmail boots":
            if bal == 40:
                bal = bal - 40
                Chainmailboots = True
                print("You now have a chainmail boots.")
                the_armorsmith()
            else:
                print("You don't have enough coins")
                the_armorsmith()
        else:
            print("Ok, have a nice day!")
            the_armorsmith()
    if main == "shop":
        print("Weapon:         Stats:                      Cost:\n"
              "Basic Sword     3 Damage, 2 turns           60 coins\n"
              "Basic Axe       5 Damage, 3 turns           80 coins\n"
              "Basic Bow       2 Damage, 1 turn, 3 distance 100 coins\n")
        item = input("Would like to buy something: ")
        if item == "Basic Sword":
            if bal >= 60:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic sword is now in slot 1 and you have 60 less coins!")
                    bal = bal - 60
                    slot1 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "2":
                    print("Ok, your basic sword is now in slot 2 and you have 60 less coins!")
                    bal = bal - 60
                    slot2 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "3":
                    print("Ok, your basic sword is now in slot 3 and you have 60 less coins!")
                    bal = bal - 60
                    slot3 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "4":
                    print("Ok, your basic sword is now in slot 4 and you have 60 less coins!")
                    bal = bal - 60
                    slot4 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "5":
                    print("Ok, your basic sword is now in slot 5 and you have 60 less coins!")
                    bal = bal - 60
                    slot5 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "6":
                    print("Ok, your basic sword is now in slot 6 and you have 60 less coins!")
                    bal = bal - 60
                    slot6 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "7":
                    print("Ok, your basic sword is now in slot 7 and you have 60 less coins!")
                    bal = bal - 60
                    slot7 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "8":
                    print("Ok, your basic sword is now in slot 8 and you have 60 less coins!")
                    bal = bal - 60
                    slot8 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "9":
                    print("Ok, your basic sword is now in slot 9 and you have 60 less coins!")
                    bal = bal - 60
                    slot9 = "Basic Sword"
                    the_armorsmith()
            else:
                print("You don't have enough coins.")
                the_armorsmith()
        if item == "basic sword":
            if bal >= 60:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic sword is now in slot 1 and you have 60 less coins!")
                    bal = bal - 60
                    slot1 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "2":
                    print("Ok, your basic sword is now in slot 2 and you have 60 less coins!")
                    bal = bal - 60
                    slot2 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "3":
                    print("Ok, your basic sword is now in slot 3 and you have 60 less coins!")
                    bal = bal - 60
                    slot3 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "4":
                    print("Ok, your basic sword is now in slot 4 and you have 60 less coins!")
                    bal = bal - 60
                    slot4 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "5":
                    print("Ok, your basic sword is now in slot 5 and you have 60 less coins!")
                    bal = bal - 60
                    slot5 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "6":
                    print("Ok, your basic sword is now in slot 6 and you have 60 less coins!")
                    bal = bal - 60
                    slot6 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "7":
                    print("Ok, your basic sword is now in slot 7 and you have 60 less coins!")
                    bal = bal - 60
                    slot7 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "8":
                    print("Ok, your basic sword is now in slot 8 and you have 60 less coins!")
                    bal = bal - 60
                    slot8 = "Basic Sword"
                    the_armorsmith()
                if slotweapon == "9":
                    print("Ok, your basic sword is now in slot 9 and you have 60 less coins!")
                    bal = bal - 60
                    slot9 = "Basic Sword"
                    the_armorsmith()
            else:
                print("You don't have enough coins.")
                the_armorsmith()
        if item == "Basic Axe":
            if bal >= 80:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your Basic Axe is now in slot 1 and you have 80 less coins!")
                    bal = bal - 80
                    slot1 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "2":
                    print("Ok, your Basic Axe is now in slot 2 and you have 80 less coins!")
                    bal = bal - 80
                    slot2 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "3":
                    print("Ok, your Basic Axe is now in slot 3 and you have 80 less coins!")
                    bal = bal - 80
                    slot3 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "4":
                    print("Ok, your Basic Axe is now in slot 4 and you have 80 less coins!")
                    bal = bal - 80
                    slot4 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "5":
                    print("Ok, your Basic Axe is now in slot 5 and you have 80 less coins!")
                    bal = bal - 80
                    slot5 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "6":
                    print("Ok, your Basic Axe is now in slot 6 and you have 80 less coins!")
                    bal = bal - 80
                    slot6 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "7":
                    print("Ok, your Basic Axe is now in slot 7 and you have 80 less coins!")
                    bal = bal - 80
                    slot7 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "8":
                    print("Ok, your Basic Axe is now in slot 8 and you have 80 less coins!")
                    bal = bal - 80
                    slot8 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "9":
                    print("Ok, your Basic Axe is now in slot 9 and you have 80 less coins!")
                    bal = bal - 80
                    slot9 = "Basic Axe"
                    the_armorsmith()
            else:
                print("You don't have enough coins.")
                the_armorsmith()
        if item == "basic axe":
            if bal >= 80:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your Basic Axe is now in slot 1 and you have 80 less coins!")
                    bal = bal - 80
                    slot1 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "2":
                    print("Ok, your Basic Axe is now in slot 2 and you have 80 less coins!")
                    bal = bal - 80
                    slot2 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "3":
                    print("Ok, your Basic Axe is now in slot 3 and you have 80 less coins!")
                    bal = bal - 80
                    slot3 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "4":
                    print("Ok, your Basic Axe is now in slot 4 and you have 80 less coins!")
                    bal = bal - 80
                    slot4 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "5":
                    print("Ok, your Basic Axe is now in slot 5 and you have 80 less coins!")
                    bal = bal - 80
                    slot5 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "6":
                    print("Ok, your Basic Axe is now in slot 6 and you have 80 less coins!")
                    bal = bal - 80
                    slot6 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "7":
                    print("Ok, your Basic Axe is now in slot 7 and you have 80 less coins!")
                    bal = bal - 80
                    slot7 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "8":
                    print("Ok, your Basic Axe is now in slot 8 and you have 80 less coins!")
                    bal = bal - 80
                    slot8 = "Basic Axe"
                    the_armorsmith()
                if slotweapon == "9":
                    print("Ok, your Basic Axe is now in slot 9 and you have 80 less coins!")
                    bal = bal - 80
                    slot9 = "Basic Axe"
                    the_armorsmith()
            else:
                print("You don't have enough coins.")
                the_armorsmith()
        if item == "Basic Bow":
            if bal >= 100:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic bow is now in slot 1 and you have 100 less coins!")
                    bal = bal - 100
                    slot1 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "2":
                    print("Ok, your basic bow is now in slot 2 and you have 100 less coins!")
                    bal = bal - 100
                    slot2 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "3":
                    print("Ok, your basic bow is now in slot 3 and you have 100 less coins!")
                    bal = bal - 100
                    slot3 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "4":
                    print("Ok, your basic bow is now in slot 4 and you have 100 less coins!")
                    bal = bal - 100
                    slot4 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "5":
                    print("Ok, your basic bow is now in slot 5 and you have 100 less coins!")
                    bal = bal - 100
                    slot5 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "6":
                    print("Ok, your basic bow is now in slot 6 and you have 100 less coins!")
                    bal = bal - 100
                    slot6 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "7":
                    print("Ok, your basic bow is now in slot 7 and you have 100 less coins!")
                    bal = bal - 100
                    slot7 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "8":
                    print("Ok, your basic bow is now in slot 8 and you have 100 less coins!")
                    bal = bal - 100
                    slot8 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "9":
                    print("Ok, your basic bow is now in slot 9 and you have 100 less coins!")
                    bal = bal - 100
                    slot9 = "Basic Bow"
                    the_armorsmith()
            else:
                print("You don't have enough coins.")
                the_armorsmith()
        if item == "basic bow":
            if bal >= 100:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic bow is now in slot 1 and you have 100 less coins!")
                    bal = bal - 100
                    slot1 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "2":
                    print("Ok, your basic bow is now in slot 2 and you have 100 less coins!")
                    bal = bal - 100
                    slot2 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "3":
                    print("Ok, your basic bow is now in slot 3 and you have 100 less coins!")
                    bal = bal - 100
                    slot3 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "4":
                    print("Ok, your basic bow is now in slot 4 and you have 100 less coins!")
                    bal = bal - 100
                    slot4 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "5":
                    print("Ok, your basic bow is now in slot 5 and you have 100 less coins!")
                    bal = bal - 100
                    slot5 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "6":
                    print("Ok, your basic bow is now in slot 6 and you have 100 less coins!")
                    bal = bal - 100
                    slot6 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "7":
                    print("Ok, your basic bow is now in slot 7 and you have 100 less coins!")
                    bal = bal - 100
                    slot7 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "8":
                    print("Ok, your basic bow is now in slot 8 and you have 100 less coins!")
                    bal = bal - 100
                    slot8 = "Basic Bow"
                    the_armorsmith()
                if slotweapon == "9":
                    print("Ok, your basic bow is now in slot 9 and you have 100 less coins!")
                    bal = bal - 100
                    slot9 = "Basic Bow"
                    the_armorsmith()
            else:
                print("You don't have enough coins.")
                the_armorsmith()
        else:
            print("Ok, have a nice day!")
            the_armorsmith()
    if main == "Armorsmith":
        if blacksmithtimes == 1:
            firsttime = "Armorsmith: Welcome to my shop where you can buy armor to protect you against your enemies " \
                        "if you type shop you can see a listing of what armor you can buy and purchase it if you'd " \
                        "like. If you'd like to leave move any direction."
            for char2 in firsttime:
                sleep(0.05)
                sys.stdout.write(char2)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many coins it takes to buy a "
                      "piece of armor.")
            if meaning == "weapon name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            if meaning == "Stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many coins it takes to buy a "
                      "piece of armor.")
            if meaning == "Weapon Name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            the_armorsmith()
        else:
            secondtime = "Armorsmith: Hello traveler welcome back to the armor shop and remember if you type " \
                         "shop you will see a list of what armor is available to you and purchase them. " \
                         "If you'd like to leave move any direction."
            for char1 in secondtime:
                sleep(0.05)
                sys.stdout.write(char1)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many coins it takes to buy a "
                      "piece of armor.")
            if meaning == "weapon name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            if meaning == "Stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many coins it takes to buy a "
                      "piece of armor.")
            if meaning == "Weapon Name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            the_armorsmith()
    if main == "armorsmith":
        if blacksmithtimes == 1:
            firsttime = "Blacksmith: Hello traveler welcome to shop if you type shop you will see a list of what is " \
                        "available to you and purchase them with your coins. If you'd like to leave move any " \
                        "direction."
            for char2 in firsttime:
                sleep(0.05)
                sys.stdout.write(char2)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("The cost of a weapon quite simply determines how many coins it takes to buy a weapon.")
            if meaning == "weapon name":
                print("The name of a weapon determines what kind of weapon it is and how high its stats are so "
                      "basically the cooler the name the better the weapon.")
            the_armorsmith()
        else:
            secondtime = "Blacksmith: Hello traveler welcome back to the blacksmith shop and remember if you type " \
                         "shop you will see a list of what is available to you and purchase them with your coins. " \
                         "If you'd like to leave move any direction."
            for char1 in secondtime:
                sleep(0.05)
                sys.stdout.write(char1)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("The cost of a weapon quite simply determines how many coins it takes to buy a weapon.")
            if meaning == "weapon name":
                print("The name of a weapon determines what kind of weapon it is and how high its stats are so "
                      "basically the cooler the name the better the weapon.")
            the_armorsmith()

    else:
        print("Didn't work try again")
        the_blacksmith()


def dev_mode():
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global bal
    print("Welcome to dev mode where you basically can do anything.")
    devinput = input("What would you like to do: ")
    if devinput == "dest":
        dest = input("Where would you like to go: ")
        if dest == "blacksmith":
            the_blacksmith()
        if dest == "village":
            the_village()
        if dest == "armorsmith":
            the_armorsmith()
        if dest == "adventure":
            the_realadventure()
    if devinput == "money":
        money = input("How much would you like: ")
        bal = float(money) + bal
    if devinput == "slot":
        slot23 = input("Slot: ")
        if slot23 == "1":
            weapon = input("Weapon: ")
            slot1 = weapon
            print("Now, " + weapon + " is in slot 1.")
        if slot23 == "2":
            weapon = input("Weapon: ")
            slot2 = weapon
            print("Now, " + weapon + " is in slot 2.")
        if slot23 == "3":
            weapon = input("Weapon: ")
            slot3 = weapon
            print("Now, " + weapon + " is in slot 3.")
        if slot23 == "4":
            weapon = input("Weapon: ")
            slot4 = weapon
            print("Now, " + weapon + " is in slot 4.")
        if slot23 == "5":
            weapon = input("Weapon: ")
            slot5 = weapon
            print("Now, " + weapon + " is in slot 5.")
        if slot23 == "6":
            weapon = input("Weapon: ")
            slot6 = weapon
            print("Now, " + weapon + " is in slot 6.")
        if slot23 == "7":
            weapon = input("Weapon: ")
            slot7 = weapon
            print("Now, " + weapon + " is in slot 7.")
        if slot23 == "8":
            weapon = input("Weapon: ")
            slot8 = weapon
            print("Now, " + weapon + " is in slot 8.")
        if slot23 == "9":
            weapon = input("Weapon: ")
            slot9 = weapon
            print("Now, " + weapon + " is in slot 9.")


def the_blacksmith():
    global x1
    global y2
    if x1 != 3 and y2 != 6:
        the_village()
    global blacksmithtimes
    blacksmithtimes = blacksmithtimes+1
    if blacksmithtimes == 1:
        print("\nThis is the blacksmith where you can buy weapons to fight your enemies with. Type Blacksmith to talk "
              "to the blacksmith.")
    else:
        print("Welcome back to the blacksmith type shop to buy weapons or blacksmith to speak with the blacksmith "
              "again")
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global Villagex
    global Villagey
    global bal
    main = input("type an action or help > ")
    if main == "dev":
        dev_mode()
    if main == "Move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            the_game()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_game()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_game()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_blacksmith()
    if main == "move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            the_game()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_game()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_game()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_blacksmith()
    if main == "Drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_game()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_game()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_game()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_game()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_game()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_game()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_blacksmith()
    if main == "drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_game()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_game()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_game()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_game()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_game()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_game()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_blacksmith()
    if main == "Inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_game()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_game()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_game()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_game()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_game()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_game()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_game()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_game()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_blacksmith()
    if main == "inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_game()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_game()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_game()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_game()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_game()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_game()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_game()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_game()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_blacksmith()
    if main == "Map":
        # x-axis values
        x = [x1]
        # y-axis values
        y = [y2]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(the_blacksmithx, the_blacksmithy, label="The Blacksmith", color="green",
                    marker=".", s=30)
        plt.scatter(the_armorsmithx, the_armorsmithy, label="The Armorsmith", color="green",
                    marker="P", s=30)
        plt.scatter(the_chiefx, the_chiefy, label="The Chief", color="green",
                    marker="D", s=30)

        # x-axis label
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Map')
        # showing legend
        plt.legend()

        # function to show the plot
        plt.show()
        the_blacksmith()
    if main == "map":
        # x-axis values
        x = [x1]
        # y-axis values
        y = [y2]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(the_blacksmithx, the_blacksmithy, label="The Blacksmith", color="green",
                    marker=".", s=30)
        plt.scatter(the_armorsmithx, the_armorsmithy, label="The Armorsmith", color="green",
                    marker="P", s=30)
        plt.scatter(the_chiefx, the_chiefy, label="The Chief", color="green",
                    marker="D", s=30)

        # x-axis label
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Map')
        # showing legend
        plt.legend()

        # function to show the plot
        plt.show()
        the_blacksmith()
    if main == "Help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nThis is all not case sensitive")
        the_blacksmith()
    if main == "help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nThis is all not case sensitive")
        the_blacksmith()
    if main == "balance":
        print("bal")
        the_blacksmith()
    if main == "Balance":
        print("bal")
        the_blacksmith()
    if main == "Shop":
        print("Weapon:         Stats:                      Cost:\n"
              "Basic Sword     3 Damage, 2 turns           60 coins\n"
              "Basic Axe       5 Damage, 3 turns           80 coins\n"
              "Basic Bow       2 Damage, 1 turn, 3 distance 100 coins\n")
        item = input("What would you like to buy or type anything to not buy anything: ")
        if item == "Basic Sword":
            if bal >= 60:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic sword is now in slot 1 and you have 60 less coins!")
                    bal = bal-60
                    slot1 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your basic sword is now in slot 2 and you have 60 less coins!")
                    bal = bal-60
                    slot2 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your basic sword is now in slot 3 and you have 60 less coins!")
                    bal = bal-60
                    slot3 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your basic sword is now in slot 4 and you have 60 less coins!")
                    bal = bal-60
                    slot4 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your basic sword is now in slot 5 and you have 60 less coins!")
                    bal = bal-60
                    slot5 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your basic sword is now in slot 6 and you have 60 less coins!")
                    bal = bal-60
                    slot6 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your basic sword is now in slot 7 and you have 60 less coins!")
                    bal = bal-60
                    slot7 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your basic sword is now in slot 8 and you have 60 less coins!")
                    bal = bal-60
                    slot8 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your basic sword is now in slot 9 and you have 60 less coins!")
                    bal = bal-60
                    slot9 = "Basic Sword"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        if item == "basic sword":
            if bal >= 60:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic sword is now in slot 1 and you have 60 less coins!")
                    bal = bal - 60
                    slot1 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your basic sword is now in slot 2 and you have 60 less coins!")
                    bal = bal - 60
                    slot2 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your basic sword is now in slot 3 and you have 60 less coins!")
                    bal = bal - 60
                    slot3 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your basic sword is now in slot 4 and you have 60 less coins!")
                    bal = bal - 60
                    slot4 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your basic sword is now in slot 5 and you have 60 less coins!")
                    bal = bal - 60
                    slot5 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your basic sword is now in slot 6 and you have 60 less coins!")
                    bal = bal - 60
                    slot6 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your basic sword is now in slot 7 and you have 60 less coins!")
                    bal = bal - 60
                    slot7 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your basic sword is now in slot 8 and you have 60 less coins!")
                    bal = bal - 60
                    slot8 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your basic sword is now in slot 9 and you have 60 less coins!")
                    bal = bal - 60
                    slot9 = "Basic Sword"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        if item == "Basic Axe":
            if bal >= 80:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your Basic Axe is now in slot 1 and you have 80 less coins!")
                    bal = bal - 80
                    slot1 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your Basic Axe is now in slot 2 and you have 80 less coins!")
                    bal = bal - 80
                    slot2 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your Basic Axe is now in slot 3 and you have 80 less coins!")
                    bal = bal - 80
                    slot3 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your Basic Axe is now in slot 4 and you have 80 less coins!")
                    bal = bal - 80
                    slot4 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your Basic Axe is now in slot 5 and you have 80 less coins!")
                    bal = bal - 80
                    slot5 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your Basic Axe is now in slot 6 and you have 80 less coins!")
                    bal = bal - 80
                    slot6 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your Basic Axe is now in slot 7 and you have 80 less coins!")
                    bal = bal - 80
                    slot7 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your Basic Axe is now in slot 8 and you have 80 less coins!")
                    bal = bal - 80
                    slot8 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your Basic Axe is now in slot 9 and you have 80 less coins!")
                    bal = bal - 80
                    slot9 = "Basic Axe"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        if item == "basic axe":
            if bal >= 80:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your Basic Axe is now in slot 1 and you have 80 less coins!")
                    bal = bal - 80
                    slot1 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your Basic Axe is now in slot 2 and you have 80 less coins!")
                    bal = bal - 80
                    slot2 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your Basic Axe is now in slot 3 and you have 80 less coins!")
                    bal = bal - 80
                    slot3 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your Basic Axe is now in slot 4 and you have 80 less coins!")
                    bal = bal - 80
                    slot4 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your Basic Axe is now in slot 5 and you have 80 less coins!")
                    bal = bal - 80
                    slot5 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your Basic Axe is now in slot 6 and you have 80 less coins!")
                    bal = bal - 80
                    slot6 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your Basic Axe is now in slot 7 and you have 80 less coins!")
                    bal = bal - 80
                    slot7 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your Basic Axe is now in slot 8 and you have 80 less coins!")
                    bal = bal - 80
                    slot8 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your Basic Axe is now in slot 9 and you have 80 less coins!")
                    bal = bal - 80
                    slot9 = "Basic Axe"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        if item == "Basic Bow":
            if bal >= 100:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic bow is now in slot 1 and you have 100 less coins!")
                    bal = bal-100
                    slot1 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your basic bow is now in slot 2 and you have 100 less coins!")
                    bal = bal-100
                    slot2 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your basic bow is now in slot 3 and you have 100 less coins!")
                    bal = bal-100
                    slot3 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your basic bow is now in slot 4 and you have 100 less coins!")
                    bal = bal-100
                    slot4 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your basic bow is now in slot 5 and you have 100 less coins!")
                    bal = bal-100
                    slot5 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your basic bow is now in slot 6 and you have 100 less coins!")
                    bal = bal-100
                    slot6 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your basic bow is now in slot 7 and you have 100 less coins!")
                    bal = bal-100
                    slot7 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your basic bow is now in slot 8 and you have 100 less coins!")
                    bal = bal-100
                    slot8 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your basic bow is now in slot 9 and you have 100 less coins!")
                    bal = bal-100
                    slot9 = "Basic Bow"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        if item == "basic bow":
            if bal >= 100:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic bow is now in slot 1 and you have 100 less coins!")
                    bal = bal-100
                    slot1 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your basic bow is now in slot 2 and you have 100 less coins!")
                    bal = bal-100
                    slot2 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your basic bow is now in slot 3 and you have 100 less coins!")
                    bal = bal-100
                    slot3 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your basic bow is now in slot 4 and you have 100 less coins!")
                    bal = bal-100
                    slot4 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your basic bow is now in slot 5 and you have 100 less coins!")
                    bal = bal-100
                    slot5 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your basic bow is now in slot 6 and you have 100 less coins!")
                    bal = bal-100
                    slot6 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your basic bow is now in slot 7 and you have 100 less coins!")
                    bal = bal-100
                    slot7 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your basic bow is now in slot 8 and you have 100 less coins!")
                    bal = bal-100
                    slot8 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your basic bow is now in slot 9 and you have 100 less coins!")
                    bal = bal-100
                    slot9 = "Basic Bow"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        else:
            print("Ok, have a nice day!")
            the_blacksmith()
    if main == "shop":
        print("Weapon:         Stats:                      Cost:\n"
              "Basic Sword     3 Damage, 2 turns           60 coins\n"
              "Basic Axe       5 Damage, 3 turns           80 coins\n"
              "Basic Bow       2 Damage, 1 turn, 3 distance 100 coins\n")
        item = input("Would like to buy something: ")
        if item == "Basic Sword":
            if bal >= 60:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic sword is now in slot 1 and you have 60 less coins!")
                    bal = bal - 60
                    slot1 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your basic sword is now in slot 2 and you have 60 less coins!")
                    bal = bal - 60
                    slot2 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your basic sword is now in slot 3 and you have 60 less coins!")
                    bal = bal - 60
                    slot3 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your basic sword is now in slot 4 and you have 60 less coins!")
                    bal = bal - 60
                    slot4 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your basic sword is now in slot 5 and you have 60 less coins!")
                    bal = bal - 60
                    slot5 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your basic sword is now in slot 6 and you have 60 less coins!")
                    bal = bal - 60
                    slot6 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your basic sword is now in slot 7 and you have 60 less coins!")
                    bal = bal - 60
                    slot7 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your basic sword is now in slot 8 and you have 60 less coins!")
                    bal = bal - 60
                    slot8 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your basic sword is now in slot 9 and you have 60 less coins!")
                    bal = bal - 60
                    slot9 = "Basic Sword"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        if item == "basic sword":
            if bal >= 60:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic sword is now in slot 1 and you have 60 less coins!")
                    bal = bal - 60
                    slot1 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your basic sword is now in slot 2 and you have 60 less coins!")
                    bal = bal - 60
                    slot2 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your basic sword is now in slot 3 and you have 60 less coins!")
                    bal = bal - 60
                    slot3 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your basic sword is now in slot 4 and you have 60 less coins!")
                    bal = bal - 60
                    slot4 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your basic sword is now in slot 5 and you have 60 less coins!")
                    bal = bal - 60
                    slot5 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your basic sword is now in slot 6 and you have 60 less coins!")
                    bal = bal - 60
                    slot6 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your basic sword is now in slot 7 and you have 60 less coins!")
                    bal = bal - 60
                    slot7 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your basic sword is now in slot 8 and you have 60 less coins!")
                    bal = bal - 60
                    slot8 = "Basic Sword"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your basic sword is now in slot 9 and you have 60 less coins!")
                    bal = bal - 60
                    slot9 = "Basic Sword"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        if item == "Basic Axe":
            if bal >= 80:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your Basic Axe is now in slot 1 and you have 80 less coins!")
                    bal = bal - 80
                    slot1 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your Basic Axe is now in slot 2 and you have 80 less coins!")
                    bal = bal - 80
                    slot2 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your Basic Axe is now in slot 3 and you have 80 less coins!")
                    bal = bal - 80
                    slot3 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your Basic Axe is now in slot 4 and you have 80 less coins!")
                    bal = bal - 80
                    slot4 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your Basic Axe is now in slot 5 and you have 80 less coins!")
                    bal = bal - 80
                    slot5 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your Basic Axe is now in slot 6 and you have 80 less coins!")
                    bal = bal - 80
                    slot6 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your Basic Axe is now in slot 7 and you have 80 less coins!")
                    bal = bal - 80
                    slot7 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your Basic Axe is now in slot 8 and you have 80 less coins!")
                    bal = bal - 80
                    slot8 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your Basic Axe is now in slot 9 and you have 80 less coins!")
                    bal = bal - 80
                    slot9 = "Basic Axe"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        if item == "basic axe":
            if bal >= 80:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your Basic Axe is now in slot 1 and you have 80 less coins!")
                    bal = bal - 80
                    slot1 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your Basic Axe is now in slot 2 and you have 80 less coins!")
                    bal = bal - 80
                    slot2 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your Basic Axe is now in slot 3 and you have 80 less coins!")
                    bal = bal - 80
                    slot3 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your Basic Axe is now in slot 4 and you have 80 less coins!")
                    bal = bal - 80
                    slot4 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your Basic Axe is now in slot 5 and you have 80 less coins!")
                    bal = bal - 80
                    slot5 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your Basic Axe is now in slot 6 and you have 80 less coins!")
                    bal = bal - 80
                    slot6 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your Basic Axe is now in slot 7 and you have 80 less coins!")
                    bal = bal - 80
                    slot7 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your Basic Axe is now in slot 8 and you have 80 less coins!")
                    bal = bal - 80
                    slot8 = "Basic Axe"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your Basic Axe is now in slot 9 and you have 80 less coins!")
                    bal = bal - 80
                    slot9 = "Basic Axe"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        if item == "Basic Bow":
            if bal >= 100:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic bow is now in slot 1 and you have 100 less coins!")
                    bal = bal - 100
                    slot1 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your basic bow is now in slot 2 and you have 100 less coins!")
                    bal = bal - 100
                    slot2 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your basic bow is now in slot 3 and you have 100 less coins!")
                    bal = bal - 100
                    slot3 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your basic bow is now in slot 4 and you have 100 less coins!")
                    bal = bal - 100
                    slot4 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your basic bow is now in slot 5 and you have 100 less coins!")
                    bal = bal - 100
                    slot5 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your basic bow is now in slot 6 and you have 100 less coins!")
                    bal = bal - 100
                    slot6 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your basic bow is now in slot 7 and you have 100 less coins!")
                    bal = bal - 100
                    slot7 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your basic bow is now in slot 8 and you have 100 less coins!")
                    bal = bal - 100
                    slot8 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your basic bow is now in slot 9 and you have 100 less coins!")
                    bal = bal - 100
                    slot9 = "Basic Bow"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        if item == "basic bow":
            if bal >= 100:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    print("Ok, your basic bow is now in slot 1 and you have 100 less coins!")
                    bal = bal - 100
                    slot1 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "2":
                    print("Ok, your basic bow is now in slot 2 and you have 100 less coins!")
                    bal = bal - 100
                    slot2 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "3":
                    print("Ok, your basic bow is now in slot 3 and you have 100 less coins!")
                    bal = bal - 100
                    slot3 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "4":
                    print("Ok, your basic bow is now in slot 4 and you have 100 less coins!")
                    bal = bal - 100
                    slot4 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "5":
                    print("Ok, your basic bow is now in slot 5 and you have 100 less coins!")
                    bal = bal - 100
                    slot5 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "6":
                    print("Ok, your basic bow is now in slot 6 and you have 100 less coins!")
                    bal = bal - 100
                    slot6 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "7":
                    print("Ok, your basic bow is now in slot 7 and you have 100 less coins!")
                    bal = bal - 100
                    slot7 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "8":
                    print("Ok, your basic bow is now in slot 8 and you have 100 less coins!")
                    bal = bal - 100
                    slot8 = "Basic Bow"
                    the_blacksmith()
                if slotweapon == "9":
                    print("Ok, your basic bow is now in slot 9 and you have 100 less coins!")
                    bal = bal - 100
                    slot9 = "Basic Bow"
                    the_blacksmith()
            else:
                print("You don't have enough coins.")
                the_blacksmith()
        else:
            print("Ok, have a nice day!")
            the_blacksmith()
    if main == "Blacksmith":
        if blacksmithtimes == 1:
            firsttime = "Blacksmith: Hello traveler welcome to shop if you type shop you will see a list of what is " \
                        "available to you and purchase them with your coins. If you'd like to leave move any " \
                        "direction."
            for char2 in firsttime:
                sleep(0.05)
                sys.stdout.write(char2)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many coins it takes to buy a weapon"
                      ".")
            if meaning == "weapon name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            if meaning == "Stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many coins it takes to buy a weapon"
                      ".")
            if meaning == "Weapon Name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            the_blacksmith()
        else:
            secondtime = "Blacksmith: Hello traveler welcome back to the blacksmith shop and remember if you type " \
                         "shop you will see a list of what is available to you and purchase them with your coins. " \
                         "If you'd like to leave move any direction."
            for char1 in secondtime:
                sleep(0.05)
                sys.stdout.write(char1)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many coins it takes to buy a weapon"
                      ".")
            if meaning == "weapon name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            if meaning == "Stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many coins it takes to buy a weapon"
                      ".")
            if meaning == "Weapon Name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            the_blacksmith()
    if main == "blacksmith":
        if blacksmithtimes == 1:
            firsttime = "Blacksmith: Hello traveler welcome to shop if you type shop you will see a list of what is " \
                        "available to you and purchase them with your coins. If you'd like to leave move any " \
                        "direction."
            for char2 in firsttime:
                sleep(0.05)
                sys.stdout.write(char2)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many coins it takes to buy a weapon"
                      ".")
            if meaning == "weapon name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            if meaning == "Stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many coins it takes to buy a weapon"
                      ".")
            if meaning == "Weapon Name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            the_blacksmith()
        else:
            secondtime = "Blacksmith: Hello traveler welcome back to the blacksmith shop and remember if you type " \
                         "shop you will see a list of what is available to you and purchase them with your coins. " \
                         "If you'd like to leave move any direction."
            for char1 in secondtime:
                sleep(0.05)
                sys.stdout.write(char1)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many coins it takes to buy a weapon"
                      ".")
            if meaning == "weapon name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            if meaning == "Stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many coins it takes to buy a weapon"
                      ".")
            if meaning == "Weapon Name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            the_blacksmith()

    else:
        print("Didn't work try again")
        the_blacksmith()


def the_village():
    global x1
    global y2
    if x1 == 3 and y2 == 6:
        the_blacksmith()
    if x1 == 5 and y2 == 6:
        the_chief()
    if x1 == 4 and y2 == 6:
        the_armorsmith()
    global villagetimes
    villagetimes = villagetimes + 1
    if villagetimes == 1:
        print("\nYou have made it to the village there is many shops where you can buy equipment for your adventure.")
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global Villagex
    global Villagey

    main = input("type an action or help > ")
    if main == "dev":
        dev_mode()
    if main == "Move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            the_game()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_game()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_game()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_village()
    if main == "move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            the_game()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_game()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_game()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_village()
    if main == "Drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_game()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_game()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_game()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_game()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_game()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_game()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_village()
    if main == "drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_game()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_game()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_game()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_game()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_game()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_game()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_village()
    if main == "Inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_game()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_game()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_game()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_game()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_game()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_game()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_game()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_game()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_village()
    if main == "inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_game()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_game()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_game()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_game()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_game()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_game()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_game()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_game()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_village()
    if main == "Map":
        # x-axis values
        x = [x1]
        # y-axis values
        y = [y2]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(the_blacksmithx, the_blacksmithy, label="The Blacksmith", color="green",
                    marker=".", s=30)
        plt.scatter(the_armorsmithx, the_armorsmithy, label="The Armorsmith", color="green",
                    marker="P", s=30)
        plt.scatter(the_chiefx, the_chiefy, label="The Chief", color="green",
                    marker="D", s=30)

        # x-axis label
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Map')
        # showing legend
        plt.legend()

        # function to show the plot
        plt.show()
        the_village()
    if main == "map":
        # x-axis values
        x = [x1]
        # y-axis values
        y = [y2]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(the_blacksmithx, the_blacksmithy, label="The Blacksmith", color="green",
                    marker=".", s=30)
        plt.scatter(the_armorsmithx, the_armorsmithy, label="The Armorsmith", color="green",
                    marker="P", s=30)
        plt.scatter(the_chiefx, the_chiefy, label="The Chief", color="green",
                    marker="D", s=30)

        # x-axis label
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Map')
        # showing legend
        plt.legend()

        # function to show the plot
        plt.show()
        the_village()
    if main == "Help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nThis is all not case sensitive")
        the_village()
    if main == "help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nThis is all not case sensitive")
        the_village()
    if main == "balance":
        print("bal")
        the_village()
    if main == "Balance":
        print("bal")
        the_village()
    else:
        print("Didn't work try again")
        the_village()


def the_game():
    global Atvillage
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global x1
    global y2
    global Villagex
    global Villagey
    if Atvillage:
        the_village()
    if x1 == 3 and y2 == 4:
        the_village()
        Atvillage = True
    main = input("\ntype an action or help > ")
    if main == "dev":
        dev_mode()
    if main == "Move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1-float(amtmv)
            the_game()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_game()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_game()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_game()
    if main == "move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1-float(amtmv)
            the_game()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_game()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_game()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_game()
    if main == "Drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_game()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_game()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_game()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_game()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_game()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_game()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_game()
    if main == "drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_game()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_game()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_game()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_game()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_game()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_game()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_game()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_game()
    if main == "Inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_game()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_game()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_game()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_game()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_game()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_game()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_game()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_game()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_game()
    if main == "inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_game()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_game()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_game()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_game()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_game()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_game()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_game()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_game()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_game()
    if main == "Map":
        # x-axis values
        x = [x1]
        # y-axis values
        y = [y2]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(Villagex, Villagey, label="Village", color="green",
                    marker=".", s=30)

        # x-axis label
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Map')
        # showing legend
        plt.legend()

        # function to show the plot
        plt.show()
        the_game()
    if main == "map":
        # x-axis values
        x = [x1]
        # y-axis values
        y = [y2]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(Villagex, Villagey, label="Village", color="green",
                    marker=".", s=30)

        # x-axis label
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Map')
        # showing legend
        plt.legend()

        # function to show the plot
        plt.show()
        the_game()
    if main == "Help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nThis is all not case sensitive")
        the_game()
    if main == "help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nThis is all not case sensitive")
        the_game()
    if main == "bal":
        print(bal)
        the_game()
    else:
        print("Didn't work try again")
        the_game()


the_game()
