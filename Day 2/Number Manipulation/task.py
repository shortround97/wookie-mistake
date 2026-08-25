bmi = 84 / 1.65 ** 2

print(int(bmi)) #flooring (below)

# Rounding the number to a place after decimal placement.
print(round(bmi, 1))
print(round(bmi, 2))
print(round(bmi, 3))

print(round) #rounds up

# Using f string
print(f'You have a bmi of: {round(bmi, 2)}, "Nice!" ')