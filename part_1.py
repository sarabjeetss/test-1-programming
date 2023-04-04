# Take input from the user
Month = int(input("Enter the month in numeric form:\n "))
Day = int(input("Enter the day in numeric form:\n "))
Year = input("Enter the year as two numerical digits: \n ")

# check inputs
if Month < 1 or Month > 12:
    print("Error: Invalid Month Input")
elif Day < 1 or Day > 31:
    print("Error: Invalid Day Input")
elif Year.isdigit() == False or len(Year) != 2:
    print("Error: Invalid Year Input")
else:
    print(f"{Month}/{Day}/{Year}: Success: Congratulations! you entered the correct date.")
