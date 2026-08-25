import random

# rand_num = random.randint(1, 10)


# print(rand_num)
# print(my_favorite_module.my_fav_number)

# Create random floating point numbers via 'random.random()'.
random_floatnum = random.random() * 10
print(random_floatnum)

# Create a uniform random number (inclusive of a and b).
# random_uniform_num = random.uniform(1, 10)
# print(random_uniform_num)

# Create heads or tails random number.
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
