print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#Todo: Get pizza price per input of pizza size choice
bill = 0
if size == "L":
    bill += 25
elif size == "M":
    bill += 20
elif size == "S":
    bill += 15
else:
    print("Sorry, that's not a valid size.")
#Todo: work out cost for additional pepperoni with chosen size.
if pepperoni == "Y":
    if size == "L" or size == "M":
        bill += 3
    else:
        bill += 2
#Todo: Calculate final cost with or without extra cheese.
if extra_cheese  == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")


# I need to review indentation via Claude or Gemini