import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input("Pick '1' for ROCK, '2' for PAPER, and '3' for SCISSORS!!\n"))

# Computer Choose either of the three at random
var1 = random.randint(1, 3)

if var1 == 1:
    outcome = rock
elif var1 == 2:
    outcome = paper
else:
    outcome = scissors

print("Computer Chose:\n", outcome)

# Player's picked choice:
images = [rock, paper, scissors]
if player == 1 or 2 or 3:
    print(f"You choose: ", images[player])

# Game's Rules
if var1 == player:
    print("It's a DRAW!!")
elif (player == 1 and var1 == 3) or (player == 2 and var1 == 1) or (player == 3 and var1 == 2):
    print("YOU WON!! 🎉🎉")
else:
    print("YOU LOST!! 😢")