# Import module
import random

variable1 = input("What is the first choice you are trying to decide between?")
variable2 = input("What is the second choice you are trying to decide between?")

# Define coin, two sides to coin
coin = [1,2]

# Define coin flip process
coin_flip = input("Please press 'Enter' to flip the coin. ")
coin_outcome = random.choice(coin)
    # Assign heads
if coin_outcome == 1:
    print("The decision is: ", variable1)

    # Assign tails
elif coin_outcome == 2:
    print("The decision is: ", variable2)

    # Allow for troubleshooting
else:
    print("error")
