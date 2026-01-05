
# Conditional Statements Examples


# 1. Even or Odd
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print("----------------------")

# 2. Voting Eligibility
age_vote = int(input("Enter your age: "))
if age_vote >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("----------------------")

# 3. Work Eligibility
age_work = int(input("Enter your age: "))
if 18 <= age_work <= 65:
    print("You are eligible to work.")
else:
    print("You are not eligible to work.")

print("----------------------")

# 4. Gender Check
gender = input("Enter your gender (M/F): ")

if gender.lower() == 'm':
    print("Male")
else:
    print("Female")
