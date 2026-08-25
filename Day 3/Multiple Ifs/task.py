print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# if/elif/else with height, age, and want photo conditions
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("youth pay $5.")
    elif age <= 18:
        bill = 7
        print("Young adults pay $7.")
    else:
        bill = 12
        print("Adults pay $12.")

    wants_photo = input("Do you want a photo?")
    if wants_photo == "yes" or "y":
        # Adds photo price to bill
        bill += 3
    print(f"Your bill for the ride is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
