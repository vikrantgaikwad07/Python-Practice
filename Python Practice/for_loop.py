# Calculate the sum of all integers from 1 to n
sum = 0
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    sum += i
print(sum)

# Calculate the factorial of a number n
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("The factorial of", n, "is:", fact)

# Fibonacci sequence up to n terms
a = 0
b = 1
n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c


# Find all divisors of a number n
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)    
    else:
        continue

# Check if a number is prime
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
        if n % i == 0:
         count += 1
if count == 2:
    print(n, "is a prime number")
  
else:
    print(n, "is not a prime number")
   