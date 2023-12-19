
# we dont need any Python Library here..



print("***Welcome to the Tip Calculator***")

total_bill = float(input("Enter the total amount of the bill (Please don't add any sign): "))

tip = int(input("What percent would you like to give as a tip? (10, 12, 15): "))

final_bill = (tip / 100) * total_bill + total_bill

split = int(input("How many people to split the bill: "))

each = final_bill / split

# Use f-string to format the output with two decimal places
print(f"Each person has to pay: ${each:.2f}")
