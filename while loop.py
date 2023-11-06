# We can use random numbers to generate random numbers
import random

# Generate a random integer between 1 and 50
rand_num = random.randrange(1,51)

# The value we increment in the while loop is defined before the loop
i = 1

# Define the condition that while true we will continue looping
while (i != rand_num):
    i += 1

print("the random value is : ", rand_num)
