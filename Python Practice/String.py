# Extracting components from a URL
url = input("Enter the URL: ")

protocol = url[:url.find(":")]

dot1 = url.find(".")
dot2 = url.find(".", dot1 + 1)
domain = url[dot1 + 1:dot2]

page = url[url.rfind("/") + 1:]

print("Protocol:", protocol)
print("Domain:", domain)        
print("Page:", page)

# Comparing two strings for equality
s1 = input("Enter first string: ")

s2 = s1[::-1]
print(s1)
print(s2)

if s1 == s2:
    print("The string is palindromic.")
else:
    print("The string is not palindromic.")

# Creating a palindromic string
s1 = input("Enter first string: ")
s2 = s1.replace(" ", "")
rev = s2[::-1]

if s2.casefold() == rev.casefold():
    print(s2)
else:
    Palindrome = s2.casefold() + rev.casefold()
    print(Palindrome)

