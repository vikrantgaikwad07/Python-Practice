# Print all prime numbers between 1 and 100
for n in range(1, 101):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n,end=' ')

# program for printing different patterns using nested loops
# Square pattern
for i in range(1,6):
    for j in range(1,6):
        print('*', end=' ')
    print()

# Right-angled triangle pattern
for i in range(1,6):
    for j in range(1,6):
        print('*', end=' ')
    print()

