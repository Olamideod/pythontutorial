# Problem: Receive miles and convert it to Kilometers
# Kilometer = miles * 1.60934
# Enter miles 5
# 5 miles equals 8.04 kilometer

# Ask the user to receive miles and assign it to miles variable
miles = input('Enter Miles: ')

# Convert from string to integer
miles = int(miles)

# Perform calculation by multiplying 1.60934 times miles
kilometer = miles * 1.60934

# Print results using format()
print("{} miles equals {} kilometers".format(miles, kilometer))
