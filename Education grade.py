
# Determine the grade of individuals by their age
# eval is a built-in function that converts a string to an integer

# Receive the value for age
age = eval(input("Enter age: "))


# Handle if age < 5
if age < 5:
    print("Too Young For School")

# Special output just for age 5
elif age == 5:
    print("Go To KG")

# Since a number is the result for ages 6 - 17 we can check them all with 1 condition
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to Grade {} ".format(grade))

# Handle everything else
else:
    print("Go To College")
