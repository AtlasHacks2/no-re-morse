import random

number_list = list(range(1, 27))
# Original list
print(number_list)

# List after first shuffle
random.shuffle(number_list)
print(number_list)

# List after second shuffle
random.shuffle(number_list)
print(number_list)