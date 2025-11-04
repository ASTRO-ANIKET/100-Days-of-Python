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

player = int(input("Pick '1' for ROCK,'2' for PAPER, and '3' for SCISSORS!!"))

import random
var1 = random.randint(1,3)

if var1 == 1:
    outcome = rock
elif var1 == 2:
    outcome = paper
else:
    outcome = scissors

print("Computer Chose: ", outcome)

game_images = [rock, paper, scissors]

if player == 1:
   print("You Choose: ", game_images[player])
elif player == 2:
   print("You Choose: ", game_images[player])
else:
    print("You Choose: ", game_images[player])


if var1 == 1 and player == 2:
    print("PAPER beats ROCK!! YOU WON")
elif var1 == 2 and player == 3:
    print ("SCISSORS beats PAPER!! YOU WON")
elif var1 == 3 and player == 1:
    print("ROCK beats SCISSORS!! YOU WON")
elif var1 == 1 and player == 3:
    print("YOU LOST!!")
elif var1 == 1 and player == 1:
    print("You both pick ROCK, it's a DRAW!!")
elif var1 == 2 and player == 1:
    print("YOU LOST!!")
elif var1 == 3 and player == 2:
    print("YOU LOST!!")
elif var1 == 2 and player == 2:
    print("You both pick PAPER, it's a DRAW!!")
elif var1 == 3 and player == 3:
    print("You both pick SCISSORS, it's a DRAW!!")
else:
    print("You entered the wrong input!!")