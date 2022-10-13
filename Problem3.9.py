# Define the number
number = 7898726

# Calculate the number of digits
noofdigits = len(str(number))

# Create a list of digits
digit = list(range(0,noofdigits))

# While Loop Statement
for i in range(0,noofdigits):
   digit[i] = number // (10 ** (noofdigits - i - 1)) % 10
   # Print the digit
   print(digit[i])






