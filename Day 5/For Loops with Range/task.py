# Using range function has to be used in conjuction with loop

# range() anatomy range(start, stop, step)
# the stop parameter will not include last int (must extend stop num
# beyond the expected end).

# Using range()
# for number in range(1, 11):
#     print(number)

# Performing Gauss' challenge by adding up numbers in a range.
total = 0
for number in range(1, 101):
    total += number
print(total)
