villagetimes = 0
x1234 = 3
y1234 = 4


def the_village(x1, y2):
    global x1234
    global y1234
    y1234 = y2
    x1234 = x1
    if x1234 == 3 and y1234 == 6:
        from main import the_blacksmith
        the_blacksmith()
    if x1234 == 5 and y1234 == 6:
        from main import the_chief
        the_chief()
    if x1234 == 4 and y1234 == 6:
        from main import the_armorsmith
        the_armorsmith()
    global villagetimes
    from main import slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, plt, the_blacksmithx
    from main import the_blacksmithy, the_armorsmithx, the_armorsmithy, the_chiefy, the_chiefx
    villagetimes = villagetimes + 1
    if villagetimes == 1:
        print("\nYou have made it to the village there is many shops where you can buy equipment for your adventure.")
    main = input("type an action or help > ")
    if main == "Move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1234 = x1234 - float(amtmv)
            the_village(x1234, y1234)
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1234 = x1234 + float(amtmv)
            the_village(x1234, y1234)
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y1234 = y1234 - float(amtmv)
            the_village(x1234, y1234)
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y1234 = y1234 + float(amtmv)
            the_village(x1234, y1234)
    if main == "move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1234 = x1234 - float(amtmv)
            the_village(x1234, y1234)
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1234 = x1234 + float(amtmv)
            the_village(x1234, y1234)
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y1234 = y1234 - float(amtmv)
            the_village(x1234, y1234)
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y1234 = y1234 + float(amtmv)
            the_village(x1234, y1234)

    if main == "Drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_village(x1234, y1234)
    if main == "drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_village(x1234, y1234)
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_village(x1234, y1234)
    if main == "Inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_village(x1234, y1234)
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_village(x1234, y1234)
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_village(x1234, y1234)
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_village(x1234, y1234)
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_village(x1234, y1234)
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_village(x1234, y1234)
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_village(x1234, y1234)
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_village(x1234, y1234)
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_village(x1234, y1234)
    if main == "inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_village(x1234, y1234)
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_village(x1234, y1234)
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_village(x1234, y1234)
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_village(x1234, y1234)
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_village(x1234, y1234)
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_village(x1234, y1234)
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_village(x1234, y1234)
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_village(x1234, y1234)
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_village(x1234, y1234)
    if main == "Map":
        # plotting points as a scatter plot
        plt.scatter(x1234, y1234, label="You", color="green",
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
        the_village(x1234, y1234)
    if main == "map":
        # plotting points as a scatter plot
        plt.scatter(x1234, y1234, label="You", color="green",
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
        the_village(x1234, y1234)
    if main == "Help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nType bal to see how many coins you have\nThis is all not case sensitive")
        the_village(x1234, y1234)
    if main == "help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nType bal to see how many coins you have\nThis is all not case sensitive")
        the_village(x1234, y1234)
    if main == "balance":
        print("bal")
        the_village(x1234, y1234)
    if main == "Balance":
        print("bal")
        the_village(x1234, y1234)
    else:
        print("Didn't work try again")
        the_village(x1234, y1234)
