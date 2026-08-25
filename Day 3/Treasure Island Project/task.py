print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#variable for answer input
choice1 = input("You've come to a crossroad, which do you choose? 'left/l' or 'right/r'?\n").lower()


if choice1 == "left" or choice1 == "l":
    choice2 = input('You\'ve come to a lake. '
                    'There\'s an island in the middle of the lake;\n'
                    'Type "wait" to wait for a boat.\n'
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input('You\'ve arrive safely. Now choose a door. Which color door? '
                        '"red", "blue", or "yellow"?\n').lower()
        #choice3 involves additional independent conditions
        # The game will continue with the choice of 'wait'
        if choice3 == "red":
            print("The room is full of fire. Game Over.\n")
        elif choice3 == "yellow":
            print("You found the treasure! Winner! Winner! Chicken Dinner!\n")
        elif choice3 == "blue":
            print("You were eaten by a dragon! Game Over.\n")
        else:
            print("You chose a door that doesn't exist. Game Over.\n")
    else:
        print("You didn\'t make. An alligator ate you. Game Over.\n")

else:
    print("Fell into a pit of snakes.\nGame Over.\n")

# This program is a game that sets up decision trees using if/elif/else statements.
# Starting at line 26, I assigned the first variables as choice1 to hold input to compare and set the next action
# and the else statement for the end of the program;
# Then within the if/elif/else statement, I assigned the second variable with choice2/input.
# Finally, the third variable is compared against 3 values, where each comparison (within if/elif/else) statement forms its own
# condition.