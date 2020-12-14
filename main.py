import sys
import matplotlib.pyplot as plt
import random
from time import sleep
Atvillage = False
if not Atvillage:
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
Adventuretimes = 0
Amtmoved = 0
Day = 1
BasicSword = False
BasicAxe = False
BasicBow = False
Bothweapons = False
x123 = 0
y123 = 0
firstimefight = False
Werewolfx = 0
Werewolfy = 1
Werewolf_Health = 20
Werewolf_Ground = False
Attacks = False
Moves = False
Werewolfattacks = False
Werewolfmoves = False
Werewolfgooddistancex = False
Werewolfgooddistancey = False
Playeronground = False
Completefirstfight = False
Timesfinalboss = 0
Minotaurx = 0
Minotaury = 2
Minotaur_Health = 30
Minotaur_Ground = False
Minotaurattacks = 0
Minotaurmoves = 0
Minotaurgooddistancex = False
Minotaurgooddistancey = False
Timesdied = 0
Shot = False
Axeturns = 4
Swordturns = 3
Bowturns = 2
Axeused = False
Swordused = False
Bowused = False
DayMessage = False


def the_village():
    global slot1
    global x1
    global y2
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    if x1 == 3 and y2 == 6:
        the_blacksmith()
    if x1 == 5 and y2 == 6:
        the_chief()
    if x1 == 4 and y2 == 6:
        the_armorsmith()
    global villagetimes
    villagetimes = villagetimes + 1
    if villagetimes == 1:
        print("\nYou have made it to the village there is many shops where you can buy equipment for your adventure. "
              "You should talk to the chief first.")
    main = input("type an action or help > ")
    if main == "Move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            the_village()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_village()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_village()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_village()
    if main == "move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            the_village()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_village()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_village()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_village()

    if main == "Drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_village()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_village()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_village()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_village()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_village()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_village()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_village()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_village()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_village()
    if main == "drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_village()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_village()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_village()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_village()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_village()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_village()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_village()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_village()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_village()
    if main == "Inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_village()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_village()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_village()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_village()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_village()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_village()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_village()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_village()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_village()
    if main == "inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_village()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_village()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_village()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_village()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_village()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_village()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_village()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_village()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_village()
    if main == "Map":
        # plotting points as a scatter plot
        plt.scatter(x1, y2, label="You", color="green",
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
        # plotting points as a scatter plot
        plt.scatter(x1, y2, label="You", color="green",
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
              "to see this menu \nType balance to see how many points you have\nThis is all not case sensitive")
        the_village()
    if main == "help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nType balance to see how many points you have\nThis is all not case sensitive")
        the_village()
    if main == "balance":
        print("You have " + str(bal) + "points.")
        the_village()
    if main == "Balance":
        print("You have " + str(bal) + "points.")
        the_village()
    else:
        print("Didn't work try again")
        the_village()


def the_final_boss():
    global health
    global Timesfinalboss
    global x123
    global y123
    global Attacks
    global Moves
    global Playeronground
    global health
    global firstimefight
    global Minotaurx
    global Minotaury
    global Minotaur_Health
    global Minotaur_Ground
    global Minotaurattacks
    global Minotaurmoves
    global Minotaurgooddistancex
    global Minotaurgooddistancey
    global Completefirstfight
    global Timesdied
    global Shot
    global Bowused
    global Bowturns
    global Axeturns
    global Axeused
    global Swordturns
    global Swordused
    global Day
    Timesfinalboss = Timesfinalboss + 1
    if Timesfinalboss == 1:
        print("Narrator: I stopped time again. I just wanted to tell you that you should aim for the chest it's his "
              "most vulnerable and will do one extra damage no matter the weapon. And, there is a chance that the "
              "minotaur can move 2 spaces. \nBesides that everything is the same as the previous battle and you have "
              "completely healed since that one. Good luck warrior I believe in you.")
        health = 10
        x123 = 0
        y123 = 0
        Attacks = False
        Moves = False
        Playeronground = False
        Shot = False
        Axeused = False
        Swordused = False
        Bowused = False
        Bowturns = 2
        Swordturns = 3
        Axeturns = 4
        sleep(3)
        print("The Minotaur gets up and gets ready to fight.")
    if Minotaur_Ground:
        Minotaurmoves = True
    if Minotaur_Health <= 0:
        print("The rest of the minotaurs: A deal's a deal I guess so we'll back off from the village. You reply, 'And"
              " you'll leave the mountains. They reply, 'What?' You say 'You heard me get out of here' They run away"
              " and you return to the village. They all are cheery to see you and throw a whole party for you. \nThe "
              " chief hands you 300 points and says 'Thank you for saving us come back anytime'")
        again = input("Would you like to play again?: ")
        if again == "Yes":
            the_game()
        if again == "yes":
            the_game()
        else:
            print("Ok, thank you for playing!")
            sleep(2)
            exit()
    if health <= 0:
        print("Well, I guess you died sucks for you. You have to go to the village. Have fun.")
        Day = 1
        the_realadventure()
    if Attacks and Moves and not Minotaur_Ground and not Minotaurmoves:
        minotaurdistancex = Minotaurx - x123
        minotaurdistancey = Minotaury - y123
        if minotaurdistancey > 0:
            Minotaury = Minotaury - 1
            print("The minotaur approaches you.")
            Minotaurmoves = True
        if minotaurdistancey < 0:
            Minotaury = Minotaury + 1
            print("The minotaur approaches you.")
            Minotaurmoves = True
        if minotaurdistancex > 0:
            Minotaurx = Minotaurx - 1
            print("The minotaur approaches you.")
            Minotaurmoves = True
        if minotaurdistancex < 0:
            Minotaurx = Minotaurx + 1
            print("The minotaur approaches you.")
            Minotaurmoves = True
        rannum1 = random.randint(1, 5)
        if rannum1 == 5:
            minotaurdistancex = Minotaurx - x123
            minotaurdistancey = Minotaury - y123
            if minotaurdistancey > 0:
                Minotaury = Minotaury - 1
                print("The minotaur approaches you again.")
                Minotaurmoves = True
                the_final_boss()
            if minotaurdistancey < 0:
                Minotaury = Minotaury + 1
                print("The minotaur approaches you again.")
                Minotaurmoves = True
                the_final_boss()
            if minotaurdistancex > 0:
                Minotaurx = Minotaurx - 1
                print("The minotaur approaches you again.")
                Minotaurmoves = True
                the_final_boss()
            if minotaurdistancex < 0:
                Minotaurx = Minotaurx + 1
                print("The minotaur approaches you again.")
                Minotaurmoves = True
                the_final_boss()
        the_final_boss()
    if Minotaur_Ground:
        Minotaur_Ground = False
    if Attacks and Moves and not Minotaurattacks:
        minotaurdistancex = Minotaurx - x123
        minotaurdistancey = Minotaury - y123
        if minotaurdistancex == 1 or minotaurdistancex == 0 or minotaurdistancex == -1:
            Minotaurgooddistancex = True
        if minotaurdistancex != 1 and minotaurdistancex != 0 and minotaurdistancex != -1:
            Minotaurgooddistancex = False
        if minotaurdistancey == 1 or minotaurdistancey == 0 or minotaurdistancey == -1:
            Minotaurgooddistancey = True
        if minotaurdistancey != 1 and minotaurdistancey != 0 and minotaurdistancey != -1:
            Minotaurgooddistancey = False
        if Minotaurgooddistancey and Minotaurgooddistancex:
            ran_num = random.randint(1, 4)
            if ran_num == 1:
                if Chainmailhelmet:
                    print("The minotaur hits your head, but your helmet blocked some of the damage and did only "
                          "1 heart.")
                    health = health - 1
                    Minotaurattacks = True
                    the_final_boss()
                else:
                    print("The minotaur hits your head, but your helmet and did 2 hearts of damage.")
                    health = health - 2
                    Minotaurattacks = True
                    the_final_boss()
            if ran_num == 2:
                if Chainmailchestplate:
                    print("The minotaur hits your chest, but your chestplate blocked some of the damage and did only "
                          "1 heart.")
                    health = health - 1
                    Minotaurattacks = True
                    the_final_boss()
                else:
                    print("The minotaur hit your chest and did 2 hearts of damage.")
                    health = health - 2
                    Minotaurattacks = True
                    the_final_boss()
            if ran_num == 3:
                if Chainmailleggings:
                    print("The minotaur hit your head, but your leggings blocked some of the damage and did only "
                          "1 heart.")
                    health = health - 1
                    Minotaurattacks = True
                    ran_num1 = random.randint(1, 2)
                    if ran_num1 == 2:
                        print("Unfortunately, the minotaur pierced through your armor and you fell on to the ground."
                              " You will not be able to move next turn.")
                        Playeronground = True
                        the_final_boss()
                    if ran_num1:
                        the_final_boss()
                else:
                    print("The minotaur hit your legs and did 2 hearts of damage. ")
                    health = health - 2
                    Minotaurattacks = True
                    the_final_boss()
            if ran_num == 4:
                if Chainmailboots:
                    print("The minotaur hit your feet, but your boots blocked some of the damage and did only "
                          "1 heart.")
                    health = health - 1
                    ran_num1 = random.randint(1, 2)
                    Minotaurattacks = True
                    if ran_num1 == 2:
                        print("Unfortunately, the minotaur pierced through your armor and you fell on to the ground."
                              " You will not be able to move next turn.")
                        Playeronground = True
                        the_final_boss()
                    if ran_num1 == 1:
                        the_final_boss()

                else:
                    print("The minotaur hit your feet your head and did 2 hearts of damage. ")
                    health = health - 2
                    Minotaurattacks = True
                    the_final_boss()
        else:
            print("The minotaur is not close enough to hurt you.")
            Minotaurattacks = True
            if Shot:
                rannum = random.randint(1, 3)
                if rannum == 1:
                    print("The minotaur takes the arrow out of his body and throws it at you.")
                    rannum1 = random.randint(1, 4)
                    if rannum1 == 1:
                        if Chainmailhelmet:
                            print("The arrow brushes your head, but your helmet blocks some of the damage and it only "
                                  "deals 1 damage.")
                            health = health - 1
                            Shot = False
                        else:
                            print("The arrow brushes your head and it does 2 damage.")
                            health = health - 2
                            Shot = False
                    if rannum1 == 2:
                        if Chainmailboots:
                            print("The arrow brushes your feet, but your boots blocks some of the damage and it only "
                                  "deals 1 damage.")
                            health = health - 1
                            Shot = False
                        else:
                            print("The arrow brushes your feet and it does 2 damage.")
                            health = health - 2
                            Shot = False
                    if rannum1 == 3:
                        if Chainmailchestplate:
                            print("The arrow brushes your chest, but your chestplate blocks some of the damage and it "
                                  "only deals 1 damage.")
                            health = health - 1
                            Shot = False
                        else:
                            print("The arrow brushes your chest and it does 2 damage.")
                            health = health - 2
                            Shot = False
                    if rannum1 == 4:
                        if Chainmailleggings:
                            print("The arrow brushes your legs, but your leggings blocks some of the damage and it only"
                                  " deals 1 damage.")
                            health = health - 1
                            Shot = False
                        else:
                            print("The arrow brushes your head and it does 2 damage.")
                            health = health - 2
                            Shot = False
            the_final_boss()
    if Attacks and Moves and Minotaurattacks and Minotaurmoves:
        Attacks = False
        Moves = False
        Minotaurattacks = False
        Minotaurmoves = False
        if Axeused:
            Axeturns = Axeturns - 1
            if Axeturns == 0:
                Axeused = False
                Axeturns = 4
        if Swordused:
            Swordturns = Swordturns - 1
            if Swordturns == 0:
                Swordused = False
                Swordturns = 3
        if Bowused:
            Bowturns = Bowturns - 1
            if Bowturns == 0:
                Bowused = False
                Bowturns = 2
    if Playeronground:
        Moves = True
        Playeronground = False
    move = input("Type help or your action > ")
    if move == "move":
        if not Moves:
            if not Playeronground:
                direction = input("Which direction would you like to move(north, south, east, west): ")
                if direction == "north":
                    y123 = y123+1
                    Moves = True
                    the_final_boss()
                if direction == "south":
                    y123 = y123-1
                    Moves = True
                    the_final_boss()
                if direction == "east":
                    x123 = x123+1
                    Moves = True
                    the_final_boss()
                if direction == "west":
                    x123 = x123-1
                    Moves = True
                    the_final_boss()
            else:
                print("You are on the ground you cannot move.")
                the_final_boss()
        else:
            print("You already moved this turn.")
            the_final_boss()
    if move == "Move":
        if not Moves:
            if not Playeronground:
                direction = input("Which direction would you like to move(north, south, east, west): ")
                if direction == "north":
                    y123 = y123+1
                    Moves = True
                if direction == "south":
                    y123 = y123-1
                    Moves = True
                if direction == "east":
                    x123 = x123+1
                    Moves = True
                if direction == "west":
                    x123 = x123-1
                    Moves = True
            else:
                print("You are on the ground you cannot move.")
                the_final_boss()
        else:
            print("You already moved this turn.")
            the_final_boss()
    if move == "map":
        # x-axis values
        x = [x123]
        # y-axis values
        y = [y123]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(Minotaurx, Minotaury, label="Minotaur", color="green",
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
        the_final_boss()
    if move == "Map":
        # x-axis values
        x = [x123]
        # y-axis values
        y = [y123]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(Minotaurx, Minotaury, label="Minotaur", color="green",
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
        the_final_boss()
    if move == "Attack":
        if not Attacks:
            weapon123 = input("What weapon would you like to attack with?(Basic Sword, Basic Axe, Basic Bow): ")
            if weapon123 == "Basic Sword":
                if BasicSword:
                    if not Swordused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury:
                            Swordused = True
                            ran_num = random.randint(1, 4)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 3 damage and an extra 1 because it's "
                                      "his chest.")
                                Minotaur_Health = Minotaur_Health - 4
                                Attacks = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 3 damage.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 3 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 3
                                Minotaur_Ground = True
                                Attacks = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the head dealing 3 damage.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic sword.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Swordturns) + " turn(s) until you can use your sword.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Sword.")
                    the_final_boss()
            if weapon123 == "Basic Axe":
                if BasicAxe:
                    if not Axeused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury:
                            Axeused = True
                            ran_num = random.randint(1, 5)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 5 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 6
                                Attacks = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 5 damage.")
                                Minotaur_Health = Minotaur_Health - 5
                                Attacks = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 5 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 5
                                Minotaur_Ground = True
                                Attacks = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the head dealing 5 damage.")
                                Minotaur_Health = Minotaur_Health - 5
                                Attacks = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic axe.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Axeturns) + " turn(s) until you can use your axe.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Axe.")
                    the_final_boss()
            if weapon123 == "Basic Bow":
                if BasicBow:
                    if not Bowused:

                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury or \
                            123-2 == Minotaurx or x123+2 == Minotaurx or y123-2 == Minotaury or y123+2 == Minotaury or \
                                x123-3 == Minotaurx or x123+3 == Minotaurx or y123-3 == Minotaury or \
                                y123+3 == Minotaury:
                            Bowused = True
                            ran_num = random.randint(1, 5)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 2 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 2 damage.")
                                Minotaur_Health = Minotaur_Health - 2
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 2 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 2
                                Minotaur_Ground = True
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the chest dealing 2 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 5:
                                print("You hit the minotaur in the head dealing 2 damage.")
                                Minotaur_Health = Minotaur_Health - 2
                                Attacks = True
                                Shot = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic bow.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Bowturns) + " turn(s) until you can use your bow.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Bow.")
                    the_final_boss()
            if weapon123 == "basic sword":
                if BasicSword:
                    if not Swordused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury:
                            Swordused = True
                            ran_num = random.randint(1, 4)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 3 damage and an extra 1 because it's "
                                      "his chest.")
                                Minotaur_Health = Minotaur_Health - 4
                                Attacks = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 3 damage.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 3 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 3
                                Minotaur_Ground = True
                                Attacks = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the head dealing 3 damage.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic sword.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Swordturns) + " turn(s) until you can use your sword.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Sword.")
                    the_final_boss()
            if weapon123 == "basic axe":
                if BasicAxe:
                    if not Axeused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury:
                            Axeused = True
                            ran_num = random.randint(1, 5)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 5 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 6
                                Attacks = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 5 damage.")
                                Minotaur_Health = Minotaur_Health - 5
                                Attacks = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 5 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 5
                                Minotaur_Ground = True
                                Attacks = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the head dealing 5 damage.")
                                Minotaur_Health = Minotaur_Health - 5
                                Attacks = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic axe.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Axeturns) + " turn(s) until you can use your axe.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Axe.")
                    the_final_boss()
            if weapon123 == "basic bow":
                if BasicBow:
                    if not Bowused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury or \
                            123-2 == Minotaurx or x123+2 == Minotaurx or y123-2 == Minotaury or y123+2 == Minotaury or \
                                x123-3 == Minotaurx or x123+3 == Minotaurx or y123-3 == Minotaury or \
                                y123+3 == Minotaury:
                            Bowused = True
                            ran_num = random.randint(1, 5)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 2 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 2 damage.")
                                Minotaur_Health = Minotaur_Health - 2
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 2 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 2
                                Minotaur_Ground = True
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the chest dealing 2 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 5:
                                print("You hit the minotaur in the head dealing 2 damage.")
                                Minotaur_Health = Minotaur_Health - 2
                                Attacks = True
                                Shot = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic bow.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Bowturns) + " turn(s) until you can use your bow.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Bow.")
                    the_final_boss()
        else:
            print("You already attacked this turn.")
            the_final_boss()
    if move == "attack":
        if not Attacks:
            weapon123 = input("What weapon would you like to attack with?(Basic Sword, Basic Axe, Basic Bow): ")
            if weapon123 == "Basic Sword":
                if BasicSword:
                    if not Swordused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury:
                            Swordused = True
                            ran_num = random.randint(1, 4)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 3 damage and an extra 1 because it's "
                                      "his chest.")
                                Minotaur_Health = Minotaur_Health - 4
                                Attacks = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 3 damage.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 3 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 3
                                Minotaur_Ground = True
                                Attacks = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the head dealing 3 damage.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic sword.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Swordturns) + " turn(s) until you can use your sword.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Sword.")
                    the_final_boss()
            if weapon123 == "Basic Axe":
                if BasicAxe:
                    if not Axeused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury:
                            Axeused = True
                            ran_num = random.randint(1, 4)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 5 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 6
                                Attacks = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 5 damage.")
                                Minotaur_Health = Minotaur_Health - 5
                                Attacks = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 5 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 5
                                Minotaur_Ground = True
                                Attacks = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the head dealing 5 damage.")
                                Minotaur_Health = Minotaur_Health - 5
                                Attacks = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic axe.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Axeturns) + " turn(s) until you can use your axe.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Axe.")
                    the_final_boss()
            if weapon123 == "Basic Bow":
                if BasicBow:
                    if not Bowused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury or \
                            123-2 == Minotaurx or x123+2 == Minotaurx or y123-2 == Minotaury or y123+2 == Minotaury or \
                                x123-3 == Minotaurx or x123+3 == Minotaurx or y123-3 == Minotaury or \
                                y123+3 == Minotaury:
                            Bowused = True
                            ran_num = random.randint(1, 5)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 2 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 2 damage.")
                                Minotaur_Health = Minotaur_Health - 2
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 2 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 2
                                Minotaur_Ground = True
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the chest dealing 2 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 5:
                                print("You hit the minotaur in the head dealing 2 damage.")
                                Minotaur_Health = Minotaur_Health - 2
                                Attacks = True
                                Shot = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic bow.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Bowturns) + " turn(s) until you can use your bow.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Bow.")
                    the_final_boss()
            if weapon123 == "basic sword":
                if BasicSword:
                    if not Swordused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury:
                            Swordused = True
                            ran_num = random.randint(1, 4)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 3 damage and an extra 1 because it's "
                                      "his chest.")
                                Minotaur_Health = Minotaur_Health - 4
                                Attacks = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 3 damage.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 3 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 3
                                Minotaur_Ground = True
                                Attacks = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the head dealing 3 damage.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic sword.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Swordturns) + " turn(s) until you can use your sword.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Sword.")
                    the_final_boss()
            if weapon123 == "basic axe":
                if BasicAxe:
                    if not Axeused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury:
                            Axeused = True
                            ran_num = random.randint(1, 4)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 5 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 6
                                Attacks = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 5 damage.")
                                Minotaur_Health = Minotaur_Health - 5
                                Attacks = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 5 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 5
                                Minotaur_Ground = True
                                Attacks = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the head dealing 5 damage.")
                                Minotaur_Health = Minotaur_Health - 5
                                Attacks = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic axe.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Axeturns) + " turn(s) until you can use your axe.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Axe.")
                    the_final_boss()
            if weapon123 == "basic bow":
                if BasicBow:
                    if not Bowused:
                        if x123-1 == Minotaurx or x123+1 == Minotaurx or y123-1 == Minotaury or y123+1 == Minotaury or \
                            123-2 == Minotaurx or x123+2 == Minotaurx or y123-2 == Minotaury or y123+2 == Minotaury or \
                                x123-3 == Minotaurx or x123+3 == Minotaurx or y123-3 == Minotaury or \
                                y123+3 == Minotaury:
                            Bowused = True
                            ran_num = random.randint(1, 5)
                            if ran_num == 1:
                                print("You hit the minotaur in the chest dealing 2 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 2:
                                print("You hit the minotaur in the head dealing 2 damage.")
                                Minotaur_Health = Minotaur_Health - 2
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 3:
                                print("You hit the minotaur in the leg dealing 2 damage and making him fall to the "
                                      "ground.")
                                Minotaur_Health = Minotaur_Health - 2
                                Minotaur_Ground = True
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 4:
                                print("You hit the minotaur in the chest dealing 2 damage and an extra 1 damage because"
                                      " it's his chest.")
                                Minotaur_Health = Minotaur_Health - 3
                                Attacks = True
                                Shot = True
                                the_final_boss()
                            if ran_num == 5:
                                print("You hit the minotaur in the head dealing 2 damage.")
                                Minotaur_Health = Minotaur_Health - 2
                                Attacks = True
                                Shot = True
                                the_final_boss()
                        else:
                            print("You aren't close enough to attack to the minotaur with a basic bow.")
                            the_final_boss()
                    else:
                        print("You have to wait " + str(Bowturns) + " turn(s) until you can use your bow.")
                        the_final_boss()
                else:
                    print("You don't have a Basic Bow.")
                    the_final_boss()
        else:
            print("You already attacked this turn.")
            the_final_boss()
    if move == "skip move":
        skipmove = input("Would you like to skip your move?: ")
        if skipmove == "Yes":
            Moves = True
            the_final_boss()
        if skipmove == "yes":
            Moves = True
            the_final_boss()
        else:
            the_final_boss()
    if move == "Skip Move":
        skipmove = input("Would you like to skip your move?: ")
        if skipmove == "Yes":
            Moves = True
            the_final_boss()
        if skipmove == "yes":
            Moves = True
            the_final_boss()
        else:
            the_final_boss()
    if move == "skip attack":
        skipmove = input("Would you like to skip your attack?: ")
        if skipmove == "Yes":
            Attacks = True
            the_final_boss()
        if skipmove == "yes":
            Attacks = True
            the_final_boss()
        else:
            the_final_boss()
    if move == "Skip Attack":
        skipmove = input("Would you like to skip your attack?: ")
        if skipmove == "Yes":
            Moves = True
            the_final_boss()
        if skipmove == "yes":
            Moves = True
            the_final_boss()
        else:
            the_final_boss()
    if move == "health":
        print("You have " + str(health) + " hearts.")
        the_final_boss()
    if move == "Health":
        print("You have " + str(health) + " hearts.")
        the_final_boss()
    if move == "help":
        print("If you type health then you can see how many hearts you have left.\n"
              "If you type move then you can move in one direction once, if you are not on the ground.\n"
              "If you type map you can see where you are and where the minotaur is.\n"
              "If you type attack you can attack the minotaur anytime before or after moving.\n"
              "If you type skip move you can skip your move.\n"
              "If you type skip attack you can skip your attack\n"
              "This all not case sensitive.")
    if move == "Help":
        print("If you type health then you can see how many hearts you have left.\n"
              "If you type move then you can move in one direction once, if you are not on the ground.\n"
              "If you type map you can see where you are and where the minotaur is.\n"
              "If you type attack you can attack the minotaur anytime before or after moving.\n"
              "If you type skip move you can skip your move.\n"
              "If you type skip attack you can skip your attack\n"
              "This all not case sensitive.")
    else:
        print("That didn't work try again.")
    the_final_boss()


def thefirstfight():
    global x123
    global y123
    global firstimefight
    global Werewolfx
    global Werewolfy
    global Werewolf_Health
    global Werewolf_Ground
    global Attacks
    global Moves
    global Werewolfattacks
    global Werewolfmoves
    global Werewolfgooddistancex
    global Werewolfgooddistancey
    global health
    global Playeronground
    global Completefirstfight
    global Shot
    global Bowused
    global Axeused
    global Swordused
    global Axeturns
    global Swordturns
    global Bowturns
    global Day
    global x1
    global y2
    firstimefight = firstimefight+1
    if firstimefight == 1:
        print("Suddenly the werewolf starts moving again, but you move out of the way so that it doesn't hit you. It is"
              " your turn. You can type map to see where the werewolf is.")
    if Werewolf_Health == 0:
        print("Narrator: Congratulations, you defeated the werewolf now time to get back to the adventure.")
        Completefirstfight = True
        the_realadventure()
    if health == 0:
        print("Well, I guess you died sucks for you. You have to go back to the village. Have fun.")
        Day = 1
        x1 = 3
        y2 = 4
        the_village()
    if Werewolf_Ground:
        Werewolfmoves = True
    if Attacks and Moves and not Werewolf_Ground and not Werewolfmoves:
        werewolfdistancex = Werewolfx - x123
        werewolfdistancey = Werewolfy - y123
        if werewolfdistancey > 0:
            Werewolfy = Werewolfy - 1
            print("The Werewolf approaches you.")
            Werewolfmoves = True
            thefirstfight()
        if werewolfdistancey < 0:
            Werewolfy = Werewolfy + 1
            print("The Werewolf approaches you.")
            Werewolfmoves = True
            thefirstfight()
        if werewolfdistancex > 0:
            Werewolfx = Werewolfx - 1
            print("The Werewolf approaches you.")
            Werewolfmoves = True
            thefirstfight()
        if werewolfdistancex < 0:
            Werewolfx = Werewolfx + 1
            print("The Werewolf approaches you.")
            Werewolfmoves = True
            thefirstfight()
    if Werewolf_Ground:
        Werewolf_Ground = False
    if Attacks and Moves and not Werewolfattacks:
        werewolfdistancex = Werewolfx - x123
        werewolfdistancey = Werewolfy - y123
        if werewolfdistancex == 1 or werewolfdistancex == 0 or werewolfdistancex == -1:
            Werewolfgooddistancex = True
        if werewolfdistancex != 1 and werewolfdistancex != 0 and werewolfdistancex != -1:
            Werewolfgooddistancex = False
        if werewolfdistancey == 1 or werewolfdistancey == 0 or werewolfdistancey == -1:
            Werewolfgooddistancey = True
        if werewolfdistancey != 1 and werewolfdistancey != 0 and werewolfdistancey != -1:
            Werewolfgooddistancey = False
        if Werewolfgooddistancey and Werewolfgooddistancex:
            ran_num = random.randint(1, 4)
            if ran_num == 1:
                if Chainmailhelmet:
                    print("The werewolf hit your head, but your helmet blocked some of the damage and did only "
                          "1 heart.")
                    health = health - 1
                    Werewolfattacks = True
                    thefirstfight()
                else:
                    print("The werewolf hit your head and did 2 hearts of damage.")
                    health = health - 2
                    Werewolfattacks = True
                    thefirstfight()
            if ran_num == 2:
                if Chainmailchestplate:
                    print("The werewolf hit your chest, but your chestplate blocked some of the damage and did only "
                          "1 heart.")
                    health = health - 1
                    Werewolfattacks = True
                    thefirstfight()
                else:
                    print("The werewolf hit your chest and did 2 hearts of damage.")
                    health = health - 2
                    Werewolfattacks = True
                    thefirstfight()
            if ran_num == 3:
                if Chainmailleggings:
                    print("The werewolf hit your legs, but your leggings blocked some of the damage and did only "
                          "1 heart.")
                    health = health - 1
                    Werewolfattacks = True
                    ran_num1 = random.randint(1, 2)
                    if ran_num1 == 2:
                        print("Unfortunately, the werewolf pierced through your armor and you fell on to the ground."
                              " You will not be able to move next turn.")
                        Playeronground = True
                        thefirstfight()
                    if ran_num1:
                        thefirstfight()
                else:
                    print("The werewolf hit your legs and did 2 hearts of damage. ")
                    health = health - 2
                    Werewolfattacks = True
                    thefirstfight()
            if ran_num == 4:
                if Chainmailboots:
                    print("The werewolf hit your feet, but your boots blocked some of the damage and did only "
                          "1 heart.")
                    health = health - 1
                    Werewolfattacks = True
                    ran_num1 = random.randint(1, 2)
                    if ran_num1 == 2:
                        print("Unfortunately, the werewolf pierced through your armor and you fell on to the ground."
                              " You will not be able to move next turn.")
                        Playeronground = True
                        thefirstfight()
                    if ran_num1 == 1:
                        thefirstfight()

                else:
                    print("The werewolf hit your feet and did 2 hearts of damage. ")
                    health = health - 2
                    Werewolfattacks = True
                    thefirstfight()
        else:
            print("The werewolf is not close enough to hurt you.")
            Werewolfattacks = True
            if Shot:
                rannum = random.randint(1, 3)
                if rannum == 1:
                    print("The werewolf takes the arrow out of his body and throws it at you.")
                    rannum1 = random.randint(1, 4)
                    if rannum1 == 1:
                        if Chainmailhelmet:
                            print("The arrow brushes your head, but your helmet blocks some of the damage and it only "
                                  "deals 1 damage.")
                            health = health - 1
                            Shot = False
                        else:
                            print("The arrow brushes your head and it does 2 damage.")
                            health = health - 2
                            Shot = False
                    if rannum1 == 2:
                        if Chainmailboots:
                            print("The arrow brushes your feet, but your boots blocks some of the damage and it only "
                                  "deals 1 damage.")
                            health = health - 1
                            Shot = False
                        else:
                            print("The arrow brushes your feet and it does 2 damage.")
                            health = health - 2
                            Shot = False
                    if rannum1 == 3:
                        if Chainmailchestplate:
                            print("The arrow brushes your chest, but your chestplate blocks some of the damage and it "
                                  "only deals 1 damage.")
                            health = health - 1
                            Shot = False
                        else:
                            print("The arrow brushes your chest and it does 2 damage.")
                            health = health - 2
                            Shot = False
                    if rannum1 == 4:
                        if Chainmailleggings:
                            print("The arrow brushes your legs, but your leggings blocks some of the damage and it only"
                                  " deals 1 damage.")
                            health = health - 1
                            Shot = False
                        else:
                            print("The arrow brushes your head and it does 2 damage.")
                            health = health - 2
                            Shot = False
            thefirstfight()
    if Moves and Attacks and Werewolfmoves and Werewolfattacks:
        Moves = False
        Attacks = False
        Werewolfattacks = False
        Werewolfmoves = False
        if Axeused:
            Axeturns = Axeturns - 1
            if Axeturns == 0:
                Axeused = False
                Axeturns = 3
        if Swordused:
            Swordturns = Swordturns - 1
            if Swordturns == 0:
                Swordused = False
                Swordturns = 2
        if Bowused:
            Bowturns = Bowturns - 1
            if Bowturns == 0:
                Bowused = False
                Bowturns = 1
    if Playeronground:
        Moves = True
        Playeronground = False
    move = input("Type help or your action > ")
    if move == "move":
        if not Playeronground:
            if not Moves:
                direction = input("Which direction would you like to move(north, south, east, west): ")
                if direction == "north":
                    y123 = y123+1
                    Moves = True
                    thefirstfight()
                if direction == "south":
                    y123 = y123-1
                    Moves = True
                    thefirstfight()
                if direction == "east":
                    x123 = x123+1
                    Moves = True
                    thefirstfight()
                if direction == "west":
                    x123 = x123-1
                    Moves = True
                    thefirstfight()
            else:
                print("You already moved this turn.")
                thefirstfight()
        else:
            print("You are on the ground you cannot move.")
    if move == "Move":
        if not Playeronground:
            if not Moves:
                direction = input("Which direction would you like to move(north, south, east, west): ")
                if direction == "north":
                    y123 = y123+1
                    Moves = True
                    thefirstfight()
                if direction == "south":
                    y123 = y123-1
                    Moves = True
                    thefirstfight()
                if direction == "east":
                    x123 = x123+1
                    Moves = True
                    thefirstfight()
                if direction == "west":
                    x123 = x123-1
                    Moves = True
                    thefirstfight()
            else:
                print("You already moved this turn.")
                thefirstfight()
        else:
            print("You are on the ground you cannot move.")
    if move == "map":
        # x-axis values
        x = [x123]
        # y-axis values
        y = [y123]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(Werewolfx, Werewolfy, label="Werewolf", color="green",
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
        thefirstfight()
    if move == "Map":
        # x-axis values
        x = [x123]
        # y-axis values
        y = [y123]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="You", color="green",
                    marker="*", s=30)
        plt.scatter(Werewolfx, Werewolfy, label="Werewolf", color="green",
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
        thefirstfight()
    if move == "Attack":
        if not Attacks:
            weapon123 = input("What weapon would you like to attack with?(Basic Sword, Basic Axe, Basic Bow): ")
            if weapon123 == "Basic Sword":
                if BasicSword:
                    if not Swordused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy:
                            Swordused = True
                            ran_num = random.randint(1, 4)
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 3 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 3
                                Werewolf_Ground = True
                                Attacks = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the head dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic sword.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Swordturns) + " turn(s) until you can use your sword.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Sword.")
                    thefirstfight()
            if weapon123 == "Basic Axe":
                if BasicAxe:
                    if not Axeused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy:
                            ran_num = random.randint(1, 5)
                            Axeused = True
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 5 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 5
                                Werewolf_Ground = True
                                Attacks = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the head dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic axe.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Axeturns) + " turn(s) until you can use your axe.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Axe.")
                    thefirstfight()
            if weapon123 == "Basic Bow":
                if BasicBow:
                    if not Bowused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy or \
                            123-2 == Werewolfx or x123+2 == Werewolfx or y123-2 == Werewolfy or y123+2 == Werewolfy or \
                                x123-3 == Werewolfx or x123+3 == Werewolfx or y123-3 == Werewolfy or \
                                y123+3 == Werewolfy:
                            Bowused = True
                            ran_num = random.randint(1, 5)
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 2 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 2
                                Werewolf_Ground = True
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the chest dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 5:
                                print("You hit the werewolf in the head dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic bow.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Bowturns) + " turn(s) until you can use your bow.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Bow.")
                    thefirstfight()
            if weapon123 == "basic sword":
                if BasicSword:
                    if not Swordused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy:
                            ran_num = random.randint(1, 4)
                            Swordused = True
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 3 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 3
                                Werewolf_Ground = True
                                Attacks = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the head dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic sword.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Swordturns) + " turn(s) until you can use your sword.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Sword.")
                    thefirstfight()
            if weapon123 == "basic axe":
                if BasicAxe:
                    if not Axeused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy:
                            ran_num = random.randint(1, 5)
                            Axeused = True
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 5 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 5
                                Werewolf_Ground = True
                                Attacks = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the head dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic axe.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Axeturns) + " turn(s) until you can use your axe.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Axe.")
                    thefirstfight()
            if weapon123 == "basic bow":
                if BasicBow:
                    if not Bowused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy or \
                            123-2 == Werewolfx or x123+2 == Werewolfx or y123-2 == Werewolfy or y123+2 == Werewolfy or \
                                x123-3 == Werewolfx or x123+3 == Werewolfx or y123-3 == Werewolfy or \
                                y123+3 == Werewolfy:
                            Bowused = True
                            ran_num = random.randint(1, 5)
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 2 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 2
                                Werewolf_Ground = True
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the chest dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 5:
                                print("You hit the werewolf in the head dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic bow.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Bowturns) + " turn(s) until you can use your bow.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Bow.")
                    thefirstfight()
        else:
            print("You already attacked this turn.")
    if move == "attack":
        if not Attacks:
            weapon123 = input("What weapon would you like to attack with?(Basic Sword, Basic Axe, Basic Bow): ")
            if weapon123 == "Basic Sword":
                if BasicSword:
                    if not Swordused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy:
                            Swordused = True
                            ran_num = random.randint(1, 4)
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 3 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 3
                                Werewolf_Ground = True
                                Attacks = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the head dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic sword.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Swordturns) + " turn(s) until you can use your sword.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Sword.")
                    thefirstfight()
            if weapon123 == "Basic Axe":
                if BasicAxe:
                    if not Axeused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy:
                            ran_num = random.randint(1, 5)
                            Axeused = True
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 5 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 5
                                Werewolf_Ground = True
                                Attacks = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the head dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic axe.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Axeturns) + " turn(s) until you can use your axe.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Axe.")
                    thefirstfight()
            if weapon123 == "Basic Bow":
                if BasicBow:
                    if not Bowused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy or \
                            123-2 == Werewolfx or x123+2 == Werewolfx or y123-2 == Werewolfy or y123+2 == Werewolfy or \
                                x123-3 == Werewolfx or x123+3 == Werewolfx or y123-3 == Werewolfy or \
                                y123+3 == Werewolfy:
                            Bowused = True
                            ran_num = random.randint(1, 5)
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 2 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 2
                                Werewolf_Ground = True
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the chest dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 5:
                                print("You hit the werewolf in the head dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic bow.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Bowturns) + " turn(s) until you can use your bow.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Bow.")
                    thefirstfight()
            if weapon123 == "basic sword":
                if BasicSword:
                    if not Swordused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy:
                            ran_num = random.randint(1, 4)
                            Swordused = True
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 3 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 3
                                Werewolf_Ground = True
                                Attacks = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the head dealing 3 damage.")
                                Werewolf_Health = Werewolf_Health - 3
                                Attacks = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic sword.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Swordturns) + " turn(s) until you can use your sword.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Sword.")
                    thefirstfight()
            if weapon123 == "basic axe":
                if BasicAxe:
                    if not Axeused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy:
                            ran_num = random.randint(1, 5)
                            Axeused = True
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 5 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 5
                                Werewolf_Ground = True
                                Attacks = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the head dealing 5 damage.")
                                Werewolf_Health = Werewolf_Health - 5
                                Attacks = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic axe.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Axeturns) + " turn(s) until you can use your axe.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Axe.")
                    thefirstfight()
            if weapon123 == "basic bow":
                if BasicBow:
                    if not Bowused:
                        if x123-1 == Werewolfx or x123+1 == Werewolfx or y123-1 == Werewolfy or y123+1 == Werewolfy or \
                            123-2 == Werewolfx or x123+2 == Werewolfx or y123-2 == Werewolfy or y123+2 == Werewolfy or \
                                x123-3 == Werewolfx or x123+3 == Werewolfx or y123-3 == Werewolfy or \
                                y123+3 == Werewolfy:
                            Bowused = True
                            ran_num = random.randint(1, 5)
                            if ran_num == 1:
                                print("You hit the werewolf in the chest dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 2:
                                print("You hit the werewolf in the head dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 3:
                                print("You hit the werewolf in the leg dealing 2 damage and making him fall to the "
                                      "ground.")
                                Werewolf_Health = Werewolf_Health - 2
                                Werewolf_Ground = True
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 4:
                                print("You hit the werewolf in the chest dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                            if ran_num == 5:
                                print("You hit the werewolf in the head dealing 2 damage.")
                                Werewolf_Health = Werewolf_Health - 2
                                Attacks = True
                                Shot = True
                                thefirstfight()
                        else:
                            print("You aren't close enough to attack to the werewolf with a basic bow.")
                            thefirstfight()
                    else:
                        print("You have to wait " + str(Bowturns) + " turn(s) until you can use your bow.")
                        thefirstfight()
                else:
                    print("You don't have a Basic Bow.")
                    thefirstfight()
        else:
            print("You already attacked this turn.")
    if move == "skip move":
        skipmove = input("Would you like to skip your move?: ")
        if skipmove == "Yes":
            Moves = True
            thefirstfight()
        if skipmove == "yes":
            Moves = True
            thefirstfight()
        else:
            thefirstfight()
    if move == "Skip Move":
        skipmove = input("Would you like to skip your move?: ")
        if skipmove == "Yes":
            Moves = True
            thefirstfight()
        if skipmove == "yes":
            Moves = True
            thefirstfight()
        else:
            thefirstfight()
    if move == "skip attack":
        skipmove = input("Would you like to skip your attack?: ")
        if skipmove == "Yes":
            Attacks = True
            thefirstfight()
        if skipmove == "yes":
            Attacks = True
            thefirstfight()
        else:
            thefirstfight()
    if move == "Skip Attack":
        skipmove = input("Would you like to skip your attack?: ")
        if skipmove == "Yes":
            Moves = True
            thefirstfight()
        if skipmove == "yes":
            Moves = True
            thefirstfight()
        else:
            thefirstfight()
    if move == "health":
        print("You have " + str(health) + " hearts.")
        thefirstfight()
    if move == "Health":
        print("You have " + str(health) + " hearts.")
        thefirstfight()
    if move == "help":
        print("If you type health then you can see how many hearts you have left.\n"
              "If you type move then you can move in one direction once, if you are not on the ground.\n"
              "If you type map you can see where you are and where the werewolf is.\n"
              "If you type attack you can attack the werewolf anytime before or after moving.\n"
              "If you type skip move you can skip your move.\n"
              "If you type skip attack you can skip your attack\n"
              "This all not case sensitive.")
        thefirstfight()
    if move == "Help":
        print("If you type health then you can see how many hearts you have left.\n"
              "If you type move then you can move in one direction once, if you are not on the ground.\n"
              "If you type map you can see where you are and where the werewolf is.\n"
              "If you type attack you can attack the werewolf anytime before or after moving.\n"
              "If you type skip move you can skip your move.\n"
              "If you type skip attack you can skip your attack\n"
              "This all not case sensitive.")
        thefirstfight()
    else:
        print("That didn't work try again.")
        thefirstfight()


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
    global Chainmailboots
    global Chainmailchestplate
    global Chainmailhelmet
    global Chainmailleggings
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
    sleep(5)
    if BasicAxe and not BasicSword and not BasicBow:
        print("When you're fighting you can either attack or move first. When you're "
              "fighting with your axe you have to be right in front of the enemy. And with your axe you have to wait"
              " 3 turns in between each time you use your axe. In these turns you can either move or attack with"
              " another weapon.\nOh, it appears you don't have any other weapons. Well it might take a while, but"
              "you'll be able to defeat your enemies. Once you're done with your turn your enemy will go. ")
    if BasicSword and not BasicAxe and not BasicBow:
        print("When you're fighting you can either attack or move first. When you're "
              "fighting with your sword you have to be right in front of the enemy. And with your sword you have to "
              "wait 2 turns in between each time you use your sword.\nIn these turns you can either move or attack "
              "with another weapon. Oh, it appears you don't have any other weapons. Well it might take a while, but"
              "you'll be able to defeat your enemies. Once you're done with your turn your enemy will go. ")
    if BasicBow and not BasicAxe and not BasicBow:
        print("When you're fighting you can either attack or move first. When you're "
              "fighting with your bow you can be up to 3 places away. And with your bow you only have to "
              "wait 1 turn in between each time you use your bow.\nIn this turn you can either move or attack with"
              " another weapon. Oh, it appears you don't have any other weapons. Well it might take a while, but"
              "you'll be able to defeat your enemies. Once you're done with your turn your enemy will go. ")
    if BasicAxe and BasicBow and not BasicSword:
        print("When you're fighting you can either attack or move first. When you're "
              "fighting with your axe you have to be right in front of the enemy. And with your axe you have to "
              "wait 3 turns in between each time you use your axe.\nIn these turns you can either move or attack "
              "with another weapon. Once you're done with your turn your enemy will go.")
        sleep(5)
        print("When you're fighting with your bow you can be up to 3 places away. And with your bow you only have "
              "to wait 1 turn in between each time you use your bow. These two will make a very good duo and it "
              "shouldn't take long to defeat your enemy.")
    if BasicSword and BasicBow and not BasicAxe:
        print("When you're fighting you can either attack or move first. When you're "
              "fighting with your bow you can be up to 3 spaces away. And with your bow you only have to "
              "wait 1 turn in between each time you use your bow.\nIn these turns you can either move or attack "
              "with another weapon. Once you're done with your turn your enemy will go.")
        sleep(5)
        print("When you're fighting with your axe you have to be right in front of your enemy. And with your axe you "
              "have to wait 3 turns in between each time you use your axe. These two will make a very good duo and "
              "it shouldn't take long to defeat your enemy.")
    if BasicAxe and BasicSword and not BasicBow:
        print("When you're fighting you can either attack or move first. When you're "
              "fighting with your axe you have to be right in front of the enemy. And with your axe you have to "
              "wait 3 turns in between each time you use your axe.\nIn these turns you can either move or attack "
              "with another weapon. Once you're done with your turn your enemy will go.")
        sleep(5)
        print("When you're fighting with your sword you have to be right in front of your enemy. And with your sword "
              "you have to wait 2 turns in between each time you use your sword. These two don't make the best duo, but"
              "as long as you have good armor you should do fine.")
    if BasicAxe and BasicBow and BasicSword:
        print("When you're fighting you can either attack or move first. When you're "
              "fighting with your axe you have to be right in front of the enemy. And with your axe you have to "
              "wait 3 turns in between each time you use your axe.\n In these turns you can either move or attack "
              "with another weapon. Once you're done with your turn your enemy will go.")
        sleep(5)
        print("When you're fighting with your sword you have to be right in front of your enemy. And with your sword "
              "you have to wait 2 turns in between each time you use your sword.")
        sleep(5)
        print("When you're fighting with your bow you can be up to 3 places away. And with your bow you only have "
              "to wait 1 turn in between each time you use your bow. These three will make a very good trio and as "
              "long as you do it right you will get an easy victory.")

    sleep(10)
    print("To use any of these weapons just type attack.")
    print("When an enemy attacks you it randomly hits you in your head, legs, chest, or feet. If you have armor"
          " on the area that it hits then you will take one heart less damage from the hit. They also move before"
          " they hit and try to move closer to you because they have to be in front of you to hit you.\nBut, when "
          "you are fighting enemies with a bow there is a chance your enemy could take an arrow out of themself"
          " and throw it at you. You can skip your attack by typing skip attack.")
    sleep(5)
    print("Narrator: To view your health type health and with that I think you are ready to fight you can do this "
          "I believe in you. If you need this information again just type help.")
    sleep(3)
    thefirstfight()


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
    global Completefirstfight
    global DayMessage
    if y2 == 11 and x1 == 10:
        print("You reached the final boss to see that it is inside of a cave. You walk inside to see a group of "
              "Minotaurs(half man, half bull). One of them looks at you and says, 'What are you doing, here?' "
              "You reply 'I want you to stop torturing the village down the mountain.'\nThey look at each other for"
              " a second and then they start laughing. Another one looks at you and says, 'You should probably just "
              "leave before we have to hurt you.' You yell back 'I'm not going to leave.'\nThe first one turns to you"
              " and says, 'Fine, if you defeat me we'll stop taking from that city, but if you lose well nothing "
              "happens.' You say, 'Sounds good. Luckily I'm not going to lose' The first one whispers to himself 'Yeah"
              ", right.")
        sleep(10)
        the_final_boss()
    if Amtmoved == 3:
        Amtmoved = 0
        Day = Day+1
        DayMessage = False
    if Day == 2 and not DayMessage:
        print("Welcome to Day 2, nothing seems to have happened and you watch the sun rise behind the trees. You can't"
              " see anything, but you feel like something is watching you.")
        DayMessage = True
    if Day == 3 and not Completefirstfight and not DayMessage:
        print("Before you able to go to sleep on the night of day 2 you look at the moon and see it is a full moon that"
              " night, then you hear a low growling sound and from seemingly out of nowhere a werewolf jumps out at "
              "you, but before it can reach you it stops in mid-air.")
        DayMessage = True
        sleep(5)
        training()
    if Day == 3 and Completefirstfight and not DayMessage:
        print("Welcome back to your adventure before you can sleep you see the sun rising. You are tired, but need to "
              "keep moving to defeat the final boss.")
    if Day > 4 and not DayMessage:
        print("You wake up on Day " + Day + "to see the sun rise. You have to keep moving. ")
        DayMessage = True
    main = input("type an action or help > ")
    if main == "dev":
        dev_mode()
    if main == "Move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move(1, 2 or 3): ")
            if float(amtmv) + Amtmoved > 3:
                print("You can't move that many spaces.")
                the_realadventure()
            x1 = x1 - float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "east":
            amtmv = input("How much do you want to move(1, 2 or 3): ")
            if float(amtmv) + Amtmoved > 3:
                print("You can't move that many spaces.")
                the_realadventure()
            x1 = x1 + float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "south":
            amtmv = input("How much do you want to move(1, 2 or 3): ")
            if float(amtmv) + Amtmoved > 3:
                print("You can't move that many spaces.")
                the_realadventure()
            y2 = y2 - float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "north":
            amtmv = input("How much do you want to move(1, 2 or 3): ")
            if float(amtmv) + Amtmoved > 3:
                print("You can't move that many spaces.")
                the_realadventure()
            y2 = y2 + float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
    if main == "move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move(1, 2 or 3): ")
            if float(amtmv) + Amtmoved > 3:
                print("You can't move that many spaces.")
                the_realadventure()
            x1 = x1 - float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "east":
            amtmv = input("How much do you want to move(1, 2 or 3): ")
            if float(amtmv) + Amtmoved > 3:
                print("You can't move that many spaces.")
                the_realadventure()
            x1 = x1 + float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "south":
            amtmv = input("How much do you want to move(1, 2 or 3): ")
            if float(amtmv) + Amtmoved > 3:
                print("You can't move that many spaces.")
                the_realadventure()
            y2 = y2 - float(amtmv)
            Amtmoved = Amtmoved + int(amtmv)
            the_realadventure()
        if direction == "north":
            amtmv = input("How much do you want to move(1, 2 or 3): ")
            if float(amtmv) + Amtmoved > 3:
                print("You can't move that many spaces.")
                the_realadventure()
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
        print(bal)
        the_realadventure()
    if main == "Balance":
        print(bal)
        the_realadventure()
    else:
        print("Didn't work try again")
        the_realadventure()


def the_adventure():
    print("The Chief: Hello traveler, for the past few years our village has been surrounded by formidable monsters,"
          " which prevent access in and out of the village. They have let us live in peace and in return we don't try"
          " and disrupt their business.\nIt has stopped the village from expanding and in a few years there will be no"
          " village. If you defeat their boss at the top of the mountain then you will be in control of the monsters"
          " and free our village. \nWhile fighting type health to see how much health you have left if this drops to or"
          " below zero then you have to restart. It is automatically at 10 hearts. This challenge is not for the weak "
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
              "blacksmith to buy weapons and an armorsmith to buy armor. You can buy from them using points, "
              "but since you don't seem to have any I will give you 350 points to start with. \nYou can come back "
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
            y2 = y2 - 1
            the_village()


def the_armorsmith():
    global x1
    global y2
    if x1 != 4 or y2 != 6:
        the_village()
    global armorsmithtimes
    armorsmithtimes = armorsmithtimes + 1
    if armorsmithtimes == 1:
        print("Welcome to the armorsmith where you can buy armor to defend yourself from your enemies type armorsmith "
              "to talk to the armorsmith.")
    else:
        print("Welcome back to the armorsmith where you can buy your armor to defend yourself remember you can type"
              " armorsmith to talk to the armorsmith.")
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
        # plotting points as a scatter plot
        plt.scatter(4, 6, label="You", color="green",
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
        # plotting points as a scatter plot
        plt.scatter(4, 6, label="You", color="green",
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
              "to see this menu \nType balance to see how many points you have\nType shop to see the shop and purchase "
              "items\nType armorsmith to talk to the armorsmith\nThis is all not case sensitive")
        the_armorsmith()
    if main == "help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nType balance to see how many points you have\nType shop to see the shop and purchase "
              "items\nType armorsmith to talk to the armorsmith\nThis is all not case sensitive")
        the_armorsmith()
    if main == "balance":
        print("You have " + str(bal) + "points.")
        the_armorsmith()
    if main == "Balance":
        print("You have " + str(bal) + "points.")
        the_armorsmith()
    if main == "Shop":
        print("Armor:               Stats:          Cost:\n"
              "Chainmail Helmet     2 Protection    40 points\n"
              "Chainmail Chestplate 2 Protection    40 points\n"
              "Chainmail Leggings   2 Protection    40 points\n"
              "Chainmail Boots      2 Protection    40 points")
        item = input("What would you like to buy or type anything to not buy anything or all to buy a full set: ")
        if item == "Chainmail Helmet":
            if not Chainmailhelmet:
                if bal >= 40:
                    bal = bal-40
                    Chainmailhelmet = True
                    print("You now have a chainmail helmet.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail helmet.")
                the_armorsmith()
        if item == "chainmail helmet":
            if not Chainmailhelmet:
                if bal >= 40:
                    bal = bal-40
                    Chainmailhelmet = True
                    print("You now have a chainmail helmet.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail helmets.")
                the_armorsmith()
        if item == "Chainmail Chestplate":
            if not Chainmailchestplate:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailchestplate = True
                    print("You now have a chainmail chestplate.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail chestplate.")
                the_armorsmith()
        if item == "chainmail chestplate":
            if not Chainmailchestplate:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailchestplate = True
                    print("You now have a chainmail chestplate.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail chestplate.")
                the_armorsmith()
        if item == "Chainmail Leggings":
            if Chainmailleggings:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailleggings = True
                    print("You now have a chainmail leggings.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail leggings.")
                the_armorsmith()
        if item == "chainmail leggings":
            if Chainmailleggings:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailleggings = True
                    print("You now have a chainmail leggings.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail leggings.")
                the_armorsmith()
        if item == "Chainmail Boots":
            if not Chainmailboots:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailboots = True
                    print("You now have a chainmail boots.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail boots.")
                the_armorsmith()
        if item == "chainmail boots":
            if not Chainmailboots:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailboots = True
                    print("You now have a chainmail boots.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail boots.")
                the_armorsmith()
        if item == "all":
            if bal >= 160:
                bal = bal - 160
                Chainmailleggings = True
                Chainmailchestplate = True
                Chainmailboots = True
                Chainmailhelmet = True
                print("You bought a full set of armor!")
                the_blacksmith()
            else:
                print("You don't have enough points to buy all of the armor.")
                the_blacksmith()
        if item == "All":
            if bal >= 160:
                bal = bal - 160
                Chainmailleggings = True
                Chainmailchestplate = True
                Chainmailboots = True
                Chainmailhelmet = True
                print("You bought a full set of armor!")
                the_blacksmith()
            else:
                print("You don't have enough points to buy all of the armor.")
                the_blacksmith()
        else:
            print("Ok, have a nice day!")
            the_armorsmith()
    if main == "shop":
        print("Armor:               Stats:          Cost:\n"
              "Chainmail Helmet     2 Protection    40 points\n"
              "Chainmail Chestplate 2 Protection    40 points\n"
              "Chainmail Leggings   2 Protection    40 points\n"
              "Chainmail Boots      2 Protection    40 points")
        item = input("What would you like to buy or type anything to not buy anything or all to buy a full set: ")
        if item == "Chainmail Helmet":
            if not Chainmailhelmet:
                if bal >= 40:
                    bal = bal-40
                    Chainmailhelmet = True
                    print("You now have a chainmail helmet.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail helmet.")
                the_armorsmith()
        if item == "chainmail helmet":
            if not Chainmailhelmet:
                if bal >= 40:
                    bal = bal-40
                    Chainmailhelmet = True
                    print("You now have a chainmail helmet.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail helmets.")
                the_armorsmith()
        if item == "Chainmail Chestplate":
            if not Chainmailchestplate:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailchestplate = True
                    print("You now have a chainmail chestplate.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail chestplate.")
                the_armorsmith()
        if item == "chainmail chestplate":
            if not Chainmailchestplate:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailchestplate = True
                    print("You now have a chainmail chestplate.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail chestplate.")
                the_armorsmith()
        if item == "Chainmail Leggings":
            if Chainmailleggings:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailleggings = True
                    print("You now have a chainmail leggings.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail leggings.")
                the_armorsmith()
        if item == "chainmail leggings":
            if Chainmailleggings:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailleggings = True
                    print("You now have a chainmail leggings.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail leggings.")
                the_armorsmith()
        if item == "Chainmail Boots":
            if not Chainmailboots:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailboots = True
                    print("You now have a chainmail boots.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail boots.")
                the_armorsmith()
        if item == "chainmail boots":
            if not Chainmailboots:
                if bal >= 40:
                    bal = bal - 40
                    Chainmailboots = True
                    print("You now have a chainmail boots.")
                    the_armorsmith()
                else:
                    print("You don't have enough points")
                    the_armorsmith()
            else:
                print("You already have chainmail boots.")
                the_armorsmith()
        if item == "all":
            if bal >= 160:
                bal = bal - 160
                Chainmailleggings = True
                Chainmailchestplate = True
                Chainmailboots = True
                Chainmailhelmet = True
                print("You bought a full set of armor!")
                the_blacksmith()
            else:
                print("You don't have enough points to buy all of the armor.")
                the_blacksmith()
        if item == "All":
            if bal >= 160:
                bal = bal - 160
                Chainmailleggings = True
                Chainmailchestplate = True
                Chainmailboots = True
                Chainmailhelmet = True
                print("You bought a full set of armor!")
                the_blacksmith()
            else:
                print("You don't have enough points to buy all of the armor.")
                the_blacksmith()
        else:
            print("Ok, have a nice day!")
            the_armorsmith()
    if main == "Armorsmith":
        if armorsmithtimes == 1:
            firsttime = "Armorsmith: Welcome to my shop where you can buy armor to protect you against your enemies " \
                        "if you type shop you can see a listing of what armor you can buy and purchase it if you'd " \
                        "like. If you'd like to leave move any direction."
            for char2 in firsttime:
                sys.stdout.write(char2)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      " the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "piece of armor.")
            if meaning == "weapon name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            if meaning == "Stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      " the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "piece of armor.")
            if meaning == "Weapon Name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            sleep(5)
            the_armorsmith()
        else:
            secondtime = "Armorsmith: Hello traveler welcome back to the armor shop and remember if you type " \
                         "shop you will see a list of what armor is available to you and purchase them. " \
                         "If you'd like to leave move any direction."
            for char1 in secondtime:
                sys.stdout.write(char1)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      " the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "piece of armor.")
            if meaning == "weapon name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            if meaning == "Stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      " the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "piece of armor.")
            if meaning == "Weapon Name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            sleep(5)
            the_armorsmith()
    if main == "armorsmith":
        if armorsmithtimes == 1:
            firsttime = "Armorsmith: Welcome to my shop where you can buy armor to protect you against your enemies " \
                        "if you type shop you can see a listing of what armor you can buy and purchase it if you'd " \
                        "like. If you'd like to leave move any direction."
            for char2 in firsttime:
                sys.stdout.write(char2)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      " the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "piece of armor.")
            if meaning == "weapon name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            if meaning == "Stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      " the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "piece of armor.")
            if meaning == "Weapon Name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            sleep(5)
            the_armorsmith()
        else:
            secondtime = "Armorsmith: Hello traveler welcome back to the armor shop and remember if you type " \
                         "shop you will see a list of what armor is available to you and purchase them. " \
                         "If you'd like to leave move any direction."
            for char1 in secondtime:
                sys.stdout.write(char1)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "piece of armor.")
            if meaning == "weapon name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            if meaning == "Stats":
                print("Armorsmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Armorsmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "piece of armor.")
            if meaning == "Weapon Name":
                print("Armorsmith: The name of armor determines what material the armor is made out of it is and how "
                      "high its stats are so basically the cooler the name the better the armor.")
            sleep(5)
            the_armorsmith()

    else:
        print("Didn't work try again")
        the_armorsmith()


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
    global x1
    global y2
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
        if dest == "firstfight":
            thefirstfight()
        if dest == "chief":
            the_chief()
        if dest == "final battle":
            the_final_boss()
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
    if x1 != 3 or y2 != 6:
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
            the_blacksmith()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_blacksmith()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_blacksmith()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_blacksmith()
    if main == "move":
        direction = input("Which direction would you like to move(north, south, east, west): ")
        if direction == "west":
            amtmv = input("How much do you want to move: ")
            x1 = x1 - float(amtmv)
            the_blacksmith()
        if direction == "east":
            amtmv = input("How much do you want to move: ")
            x1 = x1 + float(amtmv)
            the_blacksmith()
        if direction == "south":
            amtmv = input("How much do you want to move: ")
            y2 = y2 - float(amtmv)
            the_blacksmith()
        if direction == "north":
            amtmv = input("How much do you want to move: ")
            y2 = y2 + float(amtmv)
            the_blacksmith()
    if main == "Drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_blacksmith()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_blacksmith()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_blacksmith()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_blacksmith()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_blacksmith()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_blacksmith()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_blacksmith()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_blacksmith()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_blacksmith()
    if main == "drop":
        dropslot = input("Slot:")
        if dropslot == "1":
            print("You dropped " + slot1)
            slot1 = "Nothing"
            the_blacksmith()
        if dropslot == "2":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_blacksmith()
        if dropslot == "3":
            print("You dropped " + slot3)
            slot3 = "Nothing"
            the_blacksmith()
        if dropslot == "4":
            print("You dropped " + slot4)
            slot4 = "Nothing"
            the_blacksmith()
        if dropslot == "5":
            print("You dropped " + slot5)
            slot5 = "Nothing"
            the_blacksmith()
        if dropslot == "6":
            print("You dropped " + slot6)
            slot6 = "Nothing"
            the_blacksmith()
        if dropslot == "7":
            print("You dropped " + slot2)
            slot2 = "Nothing"
            the_blacksmith()
        if dropslot == "8":
            print("You dropped " + slot8)
            slot8 = "Nothing"
            the_blacksmith()
        if dropslot == "9":
            print("You dropped " + slot9)
            slot9 = "Nothing"
            the_blacksmith()
    if main == "Inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_blacksmith()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_blacksmith()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_blacksmith()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_blacksmith()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_blacksmith()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_blacksmith()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_blacksmith()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_blacksmith()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_blacksmith()
    if main == "inventory":
        slot = input("Slot:")
        if slot == "1":
            print("Slot 1: " + str(slot1))
            the_blacksmith()
        if slot == "2":
            print("Slot 2: " + str(slot2))
            the_blacksmith()
        if slot == "3":
            print("Slot 3: " + str(slot3))
            the_blacksmith()
        if slot == "4":
            print("Slot 4: " + str(slot4))
            the_blacksmith()
        if slot == "5":
            print("Slot 1: " + str(slot5))
            the_blacksmith()
        if slot == "6":
            print("Slot 6: " + str(slot6))
            the_blacksmith()
        if slot == "7":
            print("Slot 7: " + str(slot7))
            the_blacksmith()
        if slot == "8":
            print("Slot 8: " + str(slot8))
            the_blacksmith()
        if slot == "9":
            print("Slot 9: " + str(slot9))
            the_blacksmith()
    if main == "Map":

        # plotting points as a scatter plot
        plt.scatter(3, 6, label="You", color="green",
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
        # plotting points as a scatter plot
        plt.scatter(3, 6, label="You", color="green",
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
              "to see this menu \nType balance to see how many points you have\nType shop to see the shop and purchase "
              "items\nType blacksmith to talk to the blacksmith\nThis is all not case sensitive")
        the_blacksmith()
    if main == "help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu \nType balance to see how many points you have\nType shop to see the shop and purchase "
              "items\nType blacksmith to talk to the blacksmith\nThis is all not case sensitive")
        the_blacksmith()
    if main == "balance":
        print("You have " + str(bal) + "points.")
        the_blacksmith()
    if main == "Balance":
        print("You have " + str(bal) + "points.")
        the_blacksmith()
    if main == "Shop":
        print("Weapon:         Stats:                       Cost:\n"
              "Basic Sword     3 Damage, 2 turns            60 points\n"
              "Basic Axe       5 Damage, 3 turns            80 points\n"
              "Basic Bow       2 Damage, 1 turn, 3 distance 100 points\n")
        item = input("What would you like to buy or type anything to not buy anything: ")
        if item == "Basic Sword":
            if bal >= 60:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    if slot1 == "Nothing":
                        print("Ok, your basic sword is now in slot 1 and you have 60 less points!")
                        bal = bal-60
                        slot1 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "2":
                    if slot2 == "Nothing":
                        print("Ok, your basic sword is now in slot 2 and you have 60 less points!")
                        bal = bal-60
                        slot2 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "3":
                    if slot3 == "Nothing":
                        print("Ok, your basic sword is now in slot 3 and you have 60 less points!")
                        bal = bal - 60
                        slot3 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "4":
                    if slot4 == "Nothing":
                        print("Ok, your basic sword is now in slot 4 and you have 60 less points!")
                        bal = bal-60
                        slot4 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "5":
                    if slot5 == "Nothing":
                        print("Ok, your basic sword is now in slot 5 and you have 60 less points!")
                        bal = bal-60
                        slot5 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "6":
                    if slot6 == "Nothing":
                        print("Ok, your basic sword is now in slot 6 and you have 60 less points!")
                        bal = bal - 60
                        slot6 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "7":
                    if slot7 == "Nothing":
                        print("Ok, your basic sword is now in slot 7 and you have 60 less points!")
                        bal = bal-60
                        slot7 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "8":
                    if slot8 == "Nothing":
                        print("Ok, your basic sword is now in slot 8 and you have 60 less points!")
                        bal = bal-60
                        slot8 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "9":
                    if slot9 == "Nothing":
                        print("Ok, your basic sword is now in slot 9 and you have 60 less points!")
                        bal = bal-60
                        slot9 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
            else:
                print("You don't have enough points.")
                the_blacksmith()
        if item == "basic sword":
            if bal >= 60:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    if slot1 == "Nothing":
                        print("Ok, your basic sword is now in slot 1 and you have 60 less points!")
                        bal = bal-60
                        slot1 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "2":
                    if slot2 == "Nothing":
                        print("Ok, your basic sword is now in slot 2 and you have 60 less points!")
                        bal = bal-60
                        slot2 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "3":
                    if slot3 == "Nothing":
                        print("Ok, your basic sword is now in slot 3 and you have 60 less points!")
                        bal = bal - 60
                        slot3 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "4":
                    if slot4 == "Nothing":
                        print("Ok, your basic sword is now in slot 4 and you have 60 less points!")
                        bal = bal-60
                        slot4 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "5":
                    if slot5 == "Nothing":
                        print("Ok, your basic sword is now in slot 5 and you have 60 less points!")
                        bal = bal-60
                        slot5 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "6":
                    if slot6 == "Nothing":
                        print("Ok, your basic sword is now in slot 6 and you have 60 less points!")
                        bal = bal - 60
                        slot6 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "7":
                    if slot7 == "Nothing":
                        print("Ok, your basic sword is now in slot 7 and you have 60 less points!")
                        bal = bal-60
                        slot7 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "8":
                    if slot8 == "Nothing":
                        print("Ok, your basic sword is now in slot 8 and you have 60 less points!")
                        bal = bal-60
                        slot8 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "9":
                    if slot9 == "Nothing":
                        print("Ok, your basic sword is now in slot 9 and you have 60 less points!")
                        bal = bal-60
                        slot9 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
            else:
                print("You don't have enough points.")
                the_blacksmith()
        if item == "Basic Axe":
            if bal >= 80:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    if slot1 == "Nothing":
                        print("Ok, your basic axe is now in slot 1 and you have 80 less points!")
                        bal = bal-80
                        slot1 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "2":
                    if slot2 == "Nothing":
                        print("Ok, your basic axe is now in slot 2 and you have 80 less points!")
                        bal = bal-80
                        slot2 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "3":
                    if slot3 == "Nothing":
                        print("Ok, your basic axe is now in slot 3 and you have 80 less points!")
                        bal = bal - 80
                        slot3 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "4":
                    if slot4 == "Nothing":
                        print("Ok, your basic axe is now in slot 4 and you have 80 less points!")
                        bal = bal-80
                        slot4 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "5":
                    if slot5 == "Nothing":
                        print("Ok, your basic axe is now in slot 5 and you have 80 less points!")
                        bal = bal-80
                        slot5 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "6":
                    if slot6 == "Nothing":
                        print("Ok, your basic axe is now in slot 6 and you have 80 less points!")
                        bal = bal - 80
                        slot6 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "7":
                    if slot7 == "Nothing":
                        print("Ok, your basic axe is now in slot 7 and you have 80 less points!")
                        bal = bal-80
                        slot7 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "8":
                    if slot8 == "Nothing":
                        print("Ok, your basic axe is now in slot 8 and you have 80 less points!")
                        bal = bal-80
                        slot8 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "9":
                    if slot9 == "Nothing":
                        print("Ok, your basic axe is now in slot 9 and you have 80 less points!")
                        bal = bal-80
                        slot9 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
            else:
                print("You don't have enough points.")
                the_blacksmith()
        if item == "basic axe":
            if item == "Basic Axe":
                if bal >= 80:
                    slotweapon = input("Which slot would you like that in: ")
                    if slotweapon == "1":
                        if slot1 == "Nothing":
                            print("Ok, your basic axe is now in slot 1 and you have 80 less points!")
                            bal = bal-80
                            slot1 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "2":
                        if slot2 == "Nothing":
                            print("Ok, your basic axe is now in slot 2 and you have 80 less points!")
                            bal = bal-80
                            slot2 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "3":
                        if slot3 == "Nothing":
                            print("Ok, your basic axe is now in slot 3 and you have 80 less points!")
                            bal = bal - 80
                            slot3 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "4":
                        if slot4 == "Nothing":
                            print("Ok, your basic axe is now in slot 4 and you have 80 less points!")
                            bal = bal-80
                            slot4 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "5":
                        if slot5 == "Nothing":
                            print("Ok, your basic axe is now in slot 5 and you have 80 less points!")
                            bal = bal-80
                            slot5 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "6":
                        if slot6 == "Nothing":
                            print("Ok, your basic axe is now in slot 6 and you have 80 less points!")
                            bal = bal - 80
                            slot6 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "7":
                        if slot7 == "Nothing":
                            print("Ok, your basic axe is now in slot 7 and you have 80 less points!")
                            bal = bal-80
                            slot7 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "8":
                        if slot8 == "Nothing":
                            print("Ok, your basic axe is now in slot 8 and you have 80 less points!")
                            bal = bal-80
                            slot8 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "9":
                        if slot9 == "Nothing":
                            print("Ok, your basic axe is now in slot 9 and you have 80 less points!")
                            bal = bal-80
                            slot9 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                else:
                    print("You don't have enough points.")
                    the_blacksmith()
        if item == "Basic Bow":
            if bal >= 100:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    if slot1 == "Nothing":
                        print("Ok, your basic bow is now in slot 1 and you have 100 less points!")
                        bal = bal-100
                        slot1 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "2":
                    if slot2 == "Nothing":
                        print("Ok, your basic bow is now in slot 2 and you have 100 less points!")
                        bal = bal-100
                        slot2 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "3":
                    if slot3 == "Nothing":
                        print("Ok, your basic bow is now in slot 3 and you have 100 less points!")
                        bal = bal - 100
                        slot3 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "4":
                    if slot4 == "Nothing":
                        print("Ok, your basic bow is now in slot 4 and you have 100 less points!")
                        bal = bal-100
                        slot4 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "5":
                    if slot5 == "Nothing":
                        print("Ok, your basic bow is now in slot 5 and you have 100 less points!")
                        bal = bal-100
                        slot5 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "6":
                    if slot6 == "Nothing":
                        print("Ok, your basic bow is now in slot 6 and you have 100 less points!")
                        bal = bal - 100
                        slot6 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "7":
                    if slot7 == "Nothing":
                        print("Ok, your basic bow is now in slot 7 and you have 100 less points!")
                        bal = bal-100
                        slot7 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "8":
                    if slot8 == "Nothing":
                        print("Ok, your basic bow is now in slot 8 and you have 100 less points!")
                        bal = bal-100
                        slot8 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "9":
                    if slot9 == "Nothing":
                        print("Ok, your basic bow is now in slot 9 and you have 100 less points!")
                        bal = bal-100
                        slot9 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
            else:
                print("You don't have enough points.")
                the_blacksmith()
        if item == "basic bow":
            if bal >= 100:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    if slot1 == "Nothing":
                        print("Ok, your basic bow is now in slot 1 and you have 100 less points!")
                        bal = bal-100
                        slot1 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "2":
                    if slot2 == "Nothing":
                        print("Ok, your basic bow is now in slot 2 and you have 100 less points!")
                        bal = bal-100
                        slot2 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "3":
                    if slot3 == "Nothing":
                        print("Ok, your basic bow is now in slot 3 and you have 100 less points!")
                        bal = bal - 100
                        slot3 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "4":
                    if slot4 == "Nothing":
                        print("Ok, your basic bow is now in slot 4 and you have 100 less points!")
                        bal = bal-100
                        slot4 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "5":
                    if slot5 == "Nothing":
                        print("Ok, your basic bow is now in slot 5 and you have 100 less points!")
                        bal = bal-100
                        slot5 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "6":
                    if slot6 == "Nothing":
                        print("Ok, your basic bow is now in slot 6 and you have 100 less points!")
                        bal = bal - 100
                        slot6 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "7":
                    if slot7 == "Nothing":
                        print("Ok, your basic bow is now in slot 7 and you have 100 less points!")
                        bal = bal-100
                        slot7 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "8":
                    if slot8 == "Nothing":
                        print("Ok, your basic bow is now in slot 8 and you have 100 less points!")
                        bal = bal-100
                        slot8 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "9":
                    if slot9 == "Nothing":
                        print("Ok, your basic bow is now in slot 9 and you have 100 less points!")
                        bal = bal-100
                        slot9 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()

                else:
                    print("You don't have enough points.")
                    the_blacksmith()
        else:
            print("Ok, have a nice day!")
            the_blacksmith()
    if main == "shop":
        print("Weapon:         Stats:                       Cost:\n"
              "Basic Sword     3 Damage, 2 turns            60 points\n"
              "Basic Axe       5 Damage, 3 turns            80 points\n"
              "Basic Bow       2 Damage, 1 turn, 3 distance 100 points\n")
        item = input("What would you like to buy or type anything to not buy anything: ")
        if item == "Basic Sword":
            if bal >= 60:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    if slot1 == "Nothing":
                        print("Ok, your basic sword is now in slot 1 and you have 60 less points!")
                        bal = bal-60
                        slot1 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "2":
                    if slot2 == "Nothing":
                        print("Ok, your basic sword is now in slot 2 and you have 60 less points!")
                        bal = bal-60
                        slot2 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "3":
                    if slot3 == "Nothing":
                        print("Ok, your basic sword is now in slot 3 and you have 60 less points!")
                        bal = bal - 60
                        slot3 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "4":
                    if slot4 == "Nothing":
                        print("Ok, your basic sword is now in slot 4 and you have 60 less points!")
                        bal = bal-60
                        slot4 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "5":
                    if slot5 == "Nothing":
                        print("Ok, your basic sword is now in slot 5 and you have 60 less points!")
                        bal = bal-60
                        slot5 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "6":
                    if slot6 == "Nothing":
                        print("Ok, your basic sword is now in slot 6 and you have 60 less points!")
                        bal = bal - 60
                        slot6 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "7":
                    if slot7 == "Nothing":
                        print("Ok, your basic sword is now in slot 7 and you have 60 less points!")
                        bal = bal-60
                        slot7 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "8":
                    if slot8 == "Nothing":
                        print("Ok, your basic sword is now in slot 8 and you have 60 less points!")
                        bal = bal-60
                        slot8 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "9":
                    if slot9 == "Nothing":
                        print("Ok, your basic sword is now in slot 9 and you have 60 less points!")
                        bal = bal-60
                        slot9 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
            else:
                print("You don't have enough points.")
                the_blacksmith()
        if item == "basic sword":
            if bal >= 60:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    if slot1 == "Nothing":
                        print("Ok, your basic sword is now in slot 1 and you have 60 less points!")
                        bal = bal-60
                        slot1 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "2":
                    if slot2 == "Nothing":
                        print("Ok, your basic sword is now in slot 2 and you have 60 less points!")
                        bal = bal-60
                        slot2 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "3":
                    if slot3 == "Nothing":
                        print("Ok, your basic sword is now in slot 3 and you have 60 less points!")
                        bal = bal - 60
                        slot3 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "4":
                    if slot4 == "Nothing":
                        print("Ok, your basic sword is now in slot 4 and you have 60 less points!")
                        bal = bal-60
                        slot4 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "5":
                    if slot5 == "Nothing":
                        print("Ok, your basic sword is now in slot 5 and you have 60 less points!")
                        bal = bal-60
                        slot5 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "6":
                    if slot6 == "Nothing":
                        print("Ok, your basic sword is now in slot 6 and you have 60 less points!")
                        bal = bal - 60
                        slot6 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "7":
                    if slot7 == "Nothing":
                        print("Ok, your basic sword is now in slot 7 and you have 60 less points!")
                        bal = bal-60
                        slot7 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "8":
                    if slot8 == "Nothing":
                        print("Ok, your basic sword is now in slot 8 and you have 60 less points!")
                        bal = bal-60
                        slot8 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "9":
                    if slot9 == "Nothing":
                        print("Ok, your basic sword is now in slot 9 and you have 60 less points!")
                        bal = bal-60
                        slot9 = "Basic Sword"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
            else:
                print("You don't have enough points.")
                the_blacksmith()
        if item == "Basic Axe":
            if bal >= 80:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    if slot1 == "Nothing":
                        print("Ok, your basic axe is now in slot 1 and you have 80 less points!")
                        bal = bal-80
                        slot1 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "2":
                    if slot2 == "Nothing":
                        print("Ok, your basic axe is now in slot 2 and you have 80 less points!")
                        bal = bal-80
                        slot2 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "3":
                    if slot3 == "Nothing":
                        print("Ok, your basic axe is now in slot 3 and you have 80 less points!")
                        bal = bal - 80
                        slot3 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "4":
                    if slot4 == "Nothing":
                        print("Ok, your basic axe is now in slot 4 and you have 80 less points!")
                        bal = bal-80
                        slot4 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "5":
                    if slot5 == "Nothing":
                        print("Ok, your basic axe is now in slot 5 and you have 80 less points!")
                        bal = bal-80
                        slot5 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "6":
                    if slot6 == "Nothing":
                        print("Ok, your basic axe is now in slot 6 and you have 80 less points!")
                        bal = bal - 80
                        slot6 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "7":
                    if slot7 == "Nothing":
                        print("Ok, your basic axe is now in slot 7 and you have 80 less points!")
                        bal = bal-80
                        slot7 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "8":
                    if slot8 == "Nothing":
                        print("Ok, your basic axe is now in slot 8 and you have 80 less points!")
                        bal = bal-80
                        slot8 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "9":
                    if slot9 == "Nothing":
                        print("Ok, your basic axe is now in slot 9 and you have 80 less points!")
                        bal = bal-80
                        slot9 = "Basic Axe"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
            else:
                print("You don't have enough points.")
                the_blacksmith()
        if item == "basic axe":
            if item == "Basic Axe":
                if bal >= 80:
                    slotweapon = input("Which slot would you like that in: ")
                    if slotweapon == "1":
                        if slot1 == "Nothing":
                            print("Ok, your basic axe is now in slot 1 and you have 80 less points!")
                            bal = bal-80
                            slot1 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "2":
                        if slot2 == "Nothing":
                            print("Ok, your basic axe is now in slot 2 and you have 80 less points!")
                            bal = bal-80
                            slot2 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "3":
                        if slot3 == "Nothing":
                            print("Ok, your basic axe is now in slot 3 and you have 80 less points!")
                            bal = bal - 80
                            slot3 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "4":
                        if slot4 == "Nothing":
                            print("Ok, your basic axe is now in slot 4 and you have 80 less points!")
                            bal = bal-80
                            slot4 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "5":
                        if slot5 == "Nothing":
                            print("Ok, your basic axe is now in slot 5 and you have 80 less points!")
                            bal = bal-80
                            slot5 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "6":
                        if slot6 == "Nothing":
                            print("Ok, your basic axe is now in slot 6 and you have 80 less points!")
                            bal = bal - 80
                            slot6 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "7":
                        if slot7 == "Nothing":
                            print("Ok, your basic axe is now in slot 7 and you have 80 less points!")
                            bal = bal-80
                            slot7 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "8":
                        if slot8 == "Nothing":
                            print("Ok, your basic axe is now in slot 8 and you have 80 less points!")
                            bal = bal-80
                            slot8 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                    if slotweapon == "9":
                        if slot9 == "Nothing":
                            print("Ok, your basic axe is now in slot 9 and you have 80 less points!")
                            bal = bal-80
                            slot9 = "Basic Axe"
                            the_blacksmith()
                        else:
                            print("You already have something in that slot.")
                            the_blacksmith()
                else:
                    print("You don't have enough points.")
                    the_blacksmith()
        if item == "Basic Bow":
            if bal >= 100:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    if slot1 == "Nothing":
                        print("Ok, your basic bow is now in slot 1 and you have 100 less points!")
                        bal = bal-100
                        slot1 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "2":
                    if slot2 == "Nothing":
                        print("Ok, your basic bow is now in slot 2 and you have 100 less points!")
                        bal = bal-100
                        slot2 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "3":
                    if slot3 == "Nothing":
                        print("Ok, your basic bow is now in slot 3 and you have 100 less points!")
                        bal = bal - 100
                        slot3 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "4":
                    if slot4 == "Nothing":
                        print("Ok, your basic bow is now in slot 4 and you have 100 less points!")
                        bal = bal-100
                        slot4 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "5":
                    if slot5 == "Nothing":
                        print("Ok, your basic bow is now in slot 5 and you have 100 less points!")
                        bal = bal-100
                        slot5 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "6":
                    if slot6 == "Nothing":
                        print("Ok, your basic bow is now in slot 6 and you have 100 less points!")
                        bal = bal - 100
                        slot6 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "7":
                    if slot7 == "Nothing":
                        print("Ok, your basic bow is now in slot 7 and you have 100 less points!")
                        bal = bal-100
                        slot7 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "8":
                    if slot8 == "Nothing":
                        print("Ok, your basic bow is now in slot 8 and you have 100 less points!")
                        bal = bal-100
                        slot8 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "9":
                    if slot9 == "Nothing":
                        print("Ok, your basic bow is now in slot 9 and you have 100 less points!")
                        bal = bal-100
                        slot9 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
            else:
                print("You don't have enough points.")
                the_blacksmith()
        if item == "basic bow":
            if bal >= 100:
                slotweapon = input("Which slot would you like that in: ")
                if slotweapon == "1":
                    if slot1 == "Nothing":
                        print("Ok, your basic bow is now in slot 1 and you have 100 less points!")
                        bal = bal-100
                        slot1 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "2":
                    if slot2 == "Nothing":
                        print("Ok, your basic bow is now in slot 2 and you have 100 less points!")
                        bal = bal-100
                        slot2 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "3":
                    if slot3 == "Nothing":
                        print("Ok, your basic bow is now in slot 3 and you have 100 less points!")
                        bal = bal - 100
                        slot3 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "4":
                    if slot4 == "Nothing":
                        print("Ok, your basic bow is now in slot 4 and you have 100 less points!")
                        bal = bal-100
                        slot4 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "5":
                    if slot5 == "Nothing":
                        print("Ok, your basic bow is now in slot 5 and you have 100 less points!")
                        bal = bal-100
                        slot5 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "6":
                    if slot6 == "Nothing":
                        print("Ok, your basic bow is now in slot 6 and you have 100 less points!")
                        bal = bal - 100
                        slot6 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "7":
                    if slot7 == "Nothing":
                        print("Ok, your basic bow is now in slot 7 and you have 100 less points!")
                        bal = bal-100
                        slot7 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "8":
                    if slot8 == "Nothing":
                        print("Ok, your basic bow is now in slot 8 and you have 100 less points!")
                        bal = bal-100
                        slot8 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()
                if slotweapon == "9":
                    if slot9 == "Nothing":
                        print("Ok, your basic bow is now in slot 9 and you have 100 less points!")
                        bal = bal-100
                        slot9 = "Basic Bow"
                        the_blacksmith()
                    else:
                        print("You already have something in that slot.")
                        the_blacksmith()

                else:
                    print("You don't have enough points.")
                    the_blacksmith()
        else:
            print("Ok, have a nice day!")
            the_blacksmith()
    if main == "Blacksmith":
        if blacksmithtimes == 1:
            firsttime = "Blacksmith: Hello traveler welcome to shop if you type shop you will see a list of what is " \
                        "available to you and purchase them with your points. If you'd like to leave move any " \
                        "direction."
            for char2 in firsttime:
                sys.stdout.write(char2)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "weapon.")
            if meaning == "weapon name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            if meaning == "Stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "weapon.")
            if meaning == "Weapon Name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            sleep(5)
            the_blacksmith()
        else:
            secondtime = "Blacksmith: Hello traveler welcome back to the blacksmith shop and remember if you type " \
                         "shop you will see a list of what is available to you and purchase them with your points. " \
                         "If you'd like to leave move any direction."
            for char1 in secondtime:
                sys.stdout.write(char1)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "weapon.")
            if meaning == "weapon name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            if meaning == "Stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "weapon.")
            if meaning == "Weapon Name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            sleep(5)
            the_blacksmith()
    if main == "blacksmith":
        if blacksmithtimes == 1:
            firsttime = "Blacksmith: Hello traveler welcome to shop if you type shop you will see a list of what is " \
                        "available to you and purchase them with your points. If you'd like to leave move any " \
                        "direction."
            for char2 in firsttime:
                sys.stdout.write(char2)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "weapon.")
            if meaning == "weapon name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            if meaning == "Stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "weapon.")
            if meaning == "Weapon Name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            sleep(5)
            the_blacksmith()
        else:
            secondtime = "Blacksmith: Hello traveler welcome back to the blacksmith shop and remember if you type " \
                         "shop you will see a list of what is available to you and purchase them with your points. " \
                         "If you'd like to leave move any direction."
            for char1 in secondtime:
                sys.stdout.write(char1)
            meaning = input("\nWhat else would you like to learn about?(stats, cost, weapon name): ")
            if meaning == "stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "weapon.")
            if meaning == "weapon name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            if meaning == "Stats":
                print("Blacksmith: The stats of a weapon determine it's effectiveness against an enemy so the higher"
                      "the damage the more health it takes from your enemy, the higher the turns the more turns it "
                      "takes to use your weapon, and the distance is how far you can use the weapon on an enemy. ")
            if meaning == "Cost":
                print("Blacksmith: The cost of a weapon quite simply determines how many points it takes to buy a "
                      "weapon.")
            if meaning == "Weapon Name":
                print("Blacksmith: The name of a weapon determines what kind of weapon it is and how high its stats are"
                      " so basically the cooler the name the better the weapon.")
            sleep(5)
            the_blacksmith()

    else:
        print("Didn't work try again")
        the_blacksmith()


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
        Atvillage = True
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
              "to see this menu\nType balance to see how many points you have \nThis is all not case sensitive")
        the_game()
    if main == "help":
        print("Type inventory and the slot you want to access slots in your inventory \nType drop and the slot you want"
              " to drop to get rid of an item you will not be able to get this back\nType move, the direction you"
              " want to go, and how far you want to go in that direction to move \nType map to see the map \nType help "
              "to see this menu\nType balance to see how many points you have \nThis is all not case sensitive")
        the_game()
    if main == "balance":
        print("You have " + str(bal) + "points.")
        the_game()
    if main == "Balance":
        print("You have " + str(bal) + "points.")
        the_game()
    else:
        print("Didn't work try again")
        the_game()


the_game()
