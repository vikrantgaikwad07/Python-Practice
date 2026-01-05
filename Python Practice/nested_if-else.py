# Program to calculate discount based on the amount entered by the user

Amount = int(input("Enter the amount: "))

if Amount <= 1000:
    Amount = Amount - (Amount * 0.10)
    print("The final amount after 10% discount is:", Amount)
elif Amount <= 5000:
    Amount = Amount - (Amount * 0.15)
    print("The final amount after 15% discount is:", Amount)
elif Amount <= 10000:
    Amount = Amount - (Amount * 0.20)
    print("The final amount after 20% discount is:", Amount)
else:
    Amount = Amount - (Amount * 0.25)
    print("The final amount after 25% discount is:", Amount)

# Program to check whether a year is a leap year or not

Year = int(input("Enter the year: "))
if Year % 4 == 0 :
    print(Year, "is a leap year.")
else:
   print(Year, "is not a leap year.")
