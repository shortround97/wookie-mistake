import random
# List for letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get user's input for password gen requirement of char and length
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level (Random list items sequentially)

# pwd = "" # start empty variable
# for letter in range(0, nr_letters): # sets the range (0 - user's choice)
#     # Adds letter to password based on range set by input
#     pwd += random.choice(letters)
# for symbol in range(0, nr_symbols):
#     # adds symbols to password based on range set by input
#     pwd += random.choice(symbols)
# for number in range(0, nr_numbers):
#     # add numbers to password based on range set by input
#     pwd += random.choice(numbers)
# print(pwd) #print outside inner loop


# Hard level (Randomize and shuffle list items for password)

pwd_list = [] # use new list (instead of a variable)
for letter in range(0, nr_letters): # sets the range (0 - user's choice)
    # Append letters to password list based on range set by input
    pwd_list.append(random.choice(letters))
for symbol in range(0, nr_symbols):
    # Append symbols to password list based on range set by input
    pwd_list.append(random.choice(symbols))
for number in range(0, nr_numbers):
    # Append numbers to password list based on range set by input
    pwd_list.append(random.choice(numbers))

print(pwd_list) #print random choice chars (outside the inner loop)
random.shuffle(pwd_list) # shuffle the list
print(pwd_list) # print the shuffled list

# Use for loop to print list items to string variable.
gen_pwd = ""
for char in pwd_list:
    gen_pwd += char
print(f'Your password is: {gen_pwd}')

