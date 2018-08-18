"""This program rolls a pair of dice. The player has to guess what the sum of the two values rolled is. If they guess correctly, they win, otherwise the computer wins."""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("Enter your guess: "))
  return guess
  
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum sum of the die is %d " % (max_val))
  guess = get_user_guess()
  if guess > max_val:
    print("Your guess is out of bounds")
  else:
    print("Rolling...")
    sleep(2)
    print("Die one rolled a %d!" % (first_roll))
    sleep(1)
    print("Die two rolled a %d!" % (second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    #print("The sum for the two die is: %d" % (total_roll))
    print("Result...")
    sleep(1)
    if guess == total_roll:
      print("You guessed it! You win!! Woohoo!!!!")
    else:
      print("Sorry, the total was actually %d" % (total_roll))
    

    
roll_dice(8)
