# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their interest * interest rate is
# Print the earning after a 10 year period

# Ask the user for the money invested + the interest rate
money = input("How much to invest : ")
interest_rate = input("Interest Rate : ")

# Convert the value to a float
money = float(money)

# Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01

# Cycle through 10 years using a for loop and range from 0 - 9
for i in range(10):
    money = money + (money * interest_rate)
# Output results
print("investment after 10 years : {:.2f}".format(money))