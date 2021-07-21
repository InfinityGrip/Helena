import random
import time

minval = 1
maxval = 6

roll = input("Roll the dices again?\n")

while roll[0] == "y" or roll[0] == "Y":
    print("Rolling the Dices...")
    time.sleep(5)
    print("The values are:\n"
          f"{random.randint(minval, maxval)}\n"#dice one will generate a value between 1 and 6
          f"{random.randint(minval, maxval)}")#dice two will generate a value between 1 and 6

    roll = input("Roll the dices again?\n")
else:
    print("Thanks for playing!")