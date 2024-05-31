# Taking input from the user
year = int(input("Enter the year:"))

# Checking if the year is divisible by 4 and not divisible by 100
if year % 4 == 0 and year % 100 != 0:
    # If the above condition is true, it's a leap year
    print(f"The year {year} is a Leap Year")
# Checking if the year is divisible by 400
elif year % 400 == 0:
    # If the above condition is true, it's a leap year
    print(f"The year {year} is a Leap Year")
else:
    # If none of the above conditions are true, it's not a leap year
    print(f"The year {year} is not a Leap Year")
