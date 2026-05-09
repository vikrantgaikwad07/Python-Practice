# Check if a list is a palindrome

l1 = [5,4,3,4,5]

rev = l1[::-1]

if l1 == rev:
    print("The list is a palindrome.")  
else:
    print("The list is not a palindrome.")