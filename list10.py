# Import random module
import random

# Generate a random list of 10 numbers between 0 and 100
my_list = random.sample(range(100), 10)


# Print the list
print(f"The list is:\n{my_list}")

# Create an empty list to store numbers less than 10
less_than_10 = []

# Loop through the list and check if each number is less than 10
for num in my_list:
    if num < 10:
        # Append the number to the new list
        less_than_10.append(num)


#new list for numbers greater than 10
more_than_10 = []

for num in my_list:
    if num > 10:
        more_than_10.append(num)

# Print the new list
print("The numbers less than 10 are:", less_than_10)
print("The numbers greater than 10 are:", more_than_10)