# Get inputs from the user
month = int(input("Enter the month in numeric form: "))
day = int(input("Enter the day in numeric form: "))
year = input("Enter the year as two numerical digits (for example: 98, 20, 21): ")

# Check for valid input
if month < 1 or month > 12:
    print("Error: Invalid Month Input")
elif day < 1 or day > 31:
    print("Error: Invalid Day Input")
elif year.isdigit() == False or len(year) != 2:
    print("Error: Invalid Year Input")
else:
    print(f"{month}/{day}/{year}: Success: Congratulations! you entered the correct date.")
