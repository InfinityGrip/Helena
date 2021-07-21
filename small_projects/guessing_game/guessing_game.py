import random
import math

lowerBound = int(input("Enter lower bound:- \n"))

upperBound = int(input("Enter upper bound:- \n"))

rand = random.randint(lowerBound, upperBound)
chance = round(math.log(upperBound - lowerBound + 1, 2))

print(f"I have picked a number between{lowerBound} and {upperBound}.\n"
      f"you have {chance} chances to guess the correct number.")
count = 0

while count < chance:
    count += 1

    guess = int(input("Guess a number:\n"))

    if rand == guess:
        print("Congratulations you have found the magic number!!!")
        break

    elif rand > guess:
        print("Yikes!! Maybe try a little higher ?")
    elif rand < guess:
        print("Snake eyes!! you are too high, try again.")

if count >= chance:
    print(f"Sorry, the number was {rand}.\n"
          f"Better luck next time!")