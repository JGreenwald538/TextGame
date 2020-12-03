import sys
import matplotlib.pyplot as plt

from time import sleep

words = "You wake up in a forest and you see a village in the distance and you need to get there."
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


def the_adventure():
    print("The Chief: Hello traveler, for the past few years our village has been sorrounded by formidable monsters,"
          " which prevent access in and out of the village. They have let us live in peace and in return we don't try"
          " and disrupt their business. It has stopped the village from expanding and in a few years there will be no"
          " village. If you defeat their boss at the top of the mountain then you will be in control of the monsters"
          " and free our village. This challenge is not for the weak  ")


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


def dev_mode():
    global bal
    print("Welcome to dev mode where you basically can do anything.")
    devinput = input("What would you like to do: ")
    if devinput == "Destination":
        dest = input("Where would you like to go: ")
        if dest == "blacksmith":
            the_blacksmith()
        if dest == "village":
            the_village()
    if devinput == "Money":
        money = input("How much would you like: ")
        bal = float(money) + bal


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
                print("The cost of a weapon quite simply determines how many coins it takes to buy a weapon.")
            if meaning == "weapon name":
                print("The name of a weapon determines what kind of weapon it is and how high its stats are so "
                      "basically the cooler the name the better the weapon.")
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
                print("The cost of a weapon quite simply determines how many coins it takes to buy a weapon.")
            if meaning == "weapon name":
                print("The name of a weapon determines what kind of weapon it is and how high its stats are so "
                      "basically the cooler the name the better the weapon.")
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
                print("The cost of a weapon quite simply determines how many coins it takes to buy a weapon.")
            if meaning == "weapon name":
                print("The name of a weapon determines what kind of weapon it is and how high its stats are so "
                      "basically the cooler the name the better the weapon.")
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
                print("The cost of a weapon quite simply determines how many coins it takes to buy a weapon.")
            if meaning == "weapon name":
                print("The name of a weapon determines what kind of weapon it is and how high its stats are so "
                      "basically the cooler the name the better the weapon.")
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
    if x1 == 3 and y2 == 4:
        the_village()
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
