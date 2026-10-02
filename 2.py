# Number Analyzer
# Ask the user to enter an integer.
# Your program must determine:
# Whether the number is positive, negative, or zero.
# Whether it is even or odd.
# Whether it is divisible by 3.
# Whether it is divisible by 5.
# Whether it is divisible by both 3 and 5.
# Display the results clearly using f-strings.
# Hint: Use %, if-elif-else, and.


number = int(input("Enter an integer: "))

if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

if number % 2 == 0:
    parity = "even"
else:
    parity = "odd"

if number % 3 == 0:
    divisible_by_3 = True
else:
    divisible_by_3 = False

if number % 5 == 0:
    divisible_by_5 = True
else:
    divisible_by_5 = False

if divisible_by_3 and divisible_by_5:
    divisible_by_both = True
else:
    divisible_by_both = False

print(f"Number: {number}")
print(f"Sign: {sign}")
print(f"Parity: {parity}")
print(f"Divisible by 3: {divisible_by_3}")
print(f"Divisible by 5: {divisible_by_5}")
print(f"Divisible by both 3 and 5: {divisible_by_both}")
