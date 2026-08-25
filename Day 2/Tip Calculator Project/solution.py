print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# My code starts here
tip_as_percent = tip / 100  # Calculate chosen tip
total_tip_amount = float(bill * tip_as_percent) # Calculate tip amount for bill
total_bill = bill + total_tip_amount # Add calculated tip to the bill for total bill
bill_per_person = float(total_bill / people)    # Divide bill per person
final_amount = bill_per_person

print(f"Each person should pay: ${final_amount:.2f}")
