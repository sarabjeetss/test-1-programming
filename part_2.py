RED = "red"
BLUE = "blue"
YELLOW = "yellow"
# take inputs from the user
color1 = input("Enter the first color (red/blue/yellow):\n ")
color2 = input("Enter the second color (red/blue/yellow): \n")

#if color1 not in the option
if color1 not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color1")

# if color2 in not in the option
elif color2 not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color2")
        
# check if two colors are same
elif color1==color2:
    print("Error: The two colors you entered are same")

else:

    if color1 == RED:
        if color2 == BLUE:
            print("Purple")
        else:
            print("Orange")
    elif color1 == BLUE:
        if color2 == RED:
            print("Purple")
        else:
            print("Green")
    else:
        if color2 == RED:
            print("Orange")
        else:
            print("Green")
