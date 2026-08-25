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
choice_list = [rock, paper, scissors]

#set input for player1
player_choice = int(input("What do you choose? '0' for Rock, '1' for Paper, or '2' for Scissors\n"))
if player_choice >= 0 and player_choice <= 2: #chain for index error
    print(choice_list[player_choice])
computer_choice = random.randint(0,2) # Computer's random choice
print(choice_list[computer_choice])

if player_choice >= 3 or player_choice < 0: #Todo: Explain
    print("You type an invalid number")
elif player_choice == 0 and computer_choice == 2:   #Todo: Explain
    print("You Win!")
elif computer_choice > player_choice:   #Todo: Explain
    print("You Lose!")
elif player_choice > computer_choice:   #Todo: Explain
    print("You Win!")
elif computer_choice == player_choice:  #Todo: Explain
    print("It's a draw!")
elif computer_choice == 0 and player_choice == 2:   #Todo: Explain
    print("You Lose!")