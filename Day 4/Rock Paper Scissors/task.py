import random

rock = '''
    ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissors")
choice_list = [rock, paper, scissors] # List used for player and computer random choice selections.

#set input for player1
player_choice = int(input("What do you choose? '0' for Rock, '1' for Paper, or '2' for Scissors\n"))
if player_choice >= 0 and player_choice <= 2: #chain for index error
    print(choice_list[player_choice])
computer_choice = random.randint(0,2) # Computer's random choice
print(choice_list[computer_choice])

if player_choice >= 3 or player_choice < 0: # Ids invariants / captures edge cases
    print("You type an invalid number")
elif player_choice == 0 and computer_choice == 2:   # Player chose rock and beats scissors.
    print("You Win!")
elif computer_choice > player_choice:   # Results if computer choice is greater.
    print("You Lose!")
elif player_choice > computer_choice:   # Results if player choice is greater.
    print("You Win!")
elif computer_choice == player_choice:  # Draw Result condition if choices are equal.
    print("It's a draw!")
elif computer_choice == 0 and player_choice == 2:   # Computer chose rock and beats scissors
    print("You Lose!")