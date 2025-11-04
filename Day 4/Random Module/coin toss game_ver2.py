import random

import my_file
print(my_file.var_1)

random_integer = random.randint(1, 10)
print(random_integer)

random_number_0_to_1 = random.random() * 10 #will generate numbers with the same decimal places, the one they are multiplied
print(random_number_0_to_1)

random_float = random.uniform(1, 10) #will generate numbers with different decimal places like .0 or 0.
print(random_float)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
