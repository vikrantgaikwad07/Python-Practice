import random as rd

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(rd.choice(l1))  # Randomly selects an element from the list
print(rd.sample(l1, 3))  # Randomly selects 3 unique elements from the list
print(rd.randint(1, 100))  # Randomly generates an integer between 1 and 100
print(rd.random())  # Randomly generates a float between 0.0 and 1.0    
