import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# First option
print(random.choice(friends))

# Second option
rand_friend = random.randint(0,4 )
print(friends[rand_friend])
