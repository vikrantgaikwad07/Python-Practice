# This program calculates the total working hours in a week and the total salary based on the working hours.

l = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
sum = 0
for i in l:
    n = input("Enter the working hours for " + i + ": ")
    sum = sum + int(n)
print("Total working hours in a week: " + str(sum))

if sum <= 40:
    s = sum * 12
    print("Total salary for the week: " + str(s))

else:
    sum = sum - 40
    s = 12 * 40 + sum * 1.5 * 12
    print("Total salary for the week: " + str(s))