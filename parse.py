# Parses workout notes and converts to .json 

# Expects input notes to be in the following format
# \n
# Date (day/month)
# Workout category (chest, back, legs etc)
# Exercise 1: (weight)[kg] x (number rep), (number rep) [(weight)[kg] x (number rep), .. ]
# Exercise 2 ... 
# \n

with open('the-zen-of-python.txt') as f:
    for line in f:
        print(line.strip())



