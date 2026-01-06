# Count the number of digits in a given number using a while loop
i = 0
n = int(input("Enter a number: "))
while n > 0:
    r = n % 10
    n = n // 10
    i = i + 1
print("The count of number is:", i)

# Reverse a number and check whether it is a palindrome or not
rev = 0
n = int(input("Enter a number: "))
m = n
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
    print("Reversed number is:", rev)
if rev == m:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

# Calculate the sum of first n natural numbers using a while loop
n = int(input("Enter a number: ")  )
i = 0 
sum = 0
while n > i :
    i = i + 1
    sum = sum + i
    print(sum)

# Find the maximum and minimum number from a list of n numbers using a while loop
i = 0
n = int(input("Enter the number of elements: "))
print("Enter", n, "Numbers")
max = 0
min = 1000000
while i < n:
    x = int(input())
    i = i + 1
    if x > max:
        max = x
    if x < min:
        min = x

print("The maximum number is:", max)
print("The minimum number is:", min)
