print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

# Select your desired size of pizza? S, M or L
if size == "L":
    bill += 25
elif size == "M":
    bill += 20
elif size == "S":
    bill += 15
else:
    print("You've chosen input size for your pizza")

# Pepperoni on your pizza? Y or N
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Extra cheese? Y or N
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}!!")
