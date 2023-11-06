# Enter Calculator: 5 * 4
# 5 * 4 = 20

# Store the user inputs of the 2 numbers and its operator
num1, operator, num2 = input('Enter Calculation ').split()

# Convert the string into integer
num1 = int(num1)
num2 = int(num2)

# If + then we need to provide output based on addition
# same for the rest operations
# Print the result

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))

elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))

elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))

elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))

elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))

else:
    print("Olamide said this calculator can only print with operators like: +, -, *, /, and %.")