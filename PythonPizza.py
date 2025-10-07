# Company Banner
print("Welcome to Python Pizza! What can I get you today?")

# User Order Input
size = input("What size would you like?: ")
has_pepperoni = input("Would you like pepperoni?: ")
has_extra_cheese = input("Would you like extra cheese?: ")

# Base Prices
small = 15
medium = 20
large = 20

# initialize customer's price variable
customer_total = 0

# Price calculations
if size == "small":
    if has_pepperoni == "yes"   :
        if has_extra_cheese == "yes":
            customer_total = small + 2 +3
        elif has_extra_cheese == "no":
            customer_total = small + 2
        else: 
            print("Invalid Input for Extra Cheese. Input must be yes or no.")
    elif has_pepperoni == "no":
        if has_extra_cheese == "yes":
            customer_total = small + 3
        elif has_extra_cheese == "no":
            customer_total = small
        else:
            print("Invalid Input for Extra Cheese. Input must be yes or no.")
    else:
        print("Invalid Input for 'Has Pepperoni?' Input must be yes or no")
elif size == "medium":
    if has_pepperoni == "yes"   :
        if has_extra_cheese == "yes":
            customer_total = medium + 3 +3
        elif has_extra_cheese == "no":
            customer_total = medium + 3
        else: 
            print("Invalid Input for Extra Cheese. Input must be yes or no.")
    elif has_pepperoni == "no":
        if has_extra_cheese == "yes":
            customer_total = medium + 3
        elif has_extra_cheese == "no":
            customer_total = medium
        else:
            print("Invalid Input for Extra Cheese. Input must be yes or no.")
    else:
        print("Invalid Input for 'Has Pepperoni?' Input must be yes or no")
elif size == "large":
    if has_pepperoni == "yes"   :
        if has_extra_cheese == "yes":
            customer_total = large + 3 +3
        elif has_extra_cheese == "no":
            customer_total = large + 3
        else: 
            print("Invalid Input for Extra Cheese. Input must be yes or no.")
    elif has_pepperoni == "no":
        if has_extra_cheese == "yes":
            customer_total = large + 3
        elif has_extra_cheese == "no":
            customer_total = large
        else:
            print("Invalid Input for Extra Cheese. Input must be yes or no.")
    else:
        print("Invalid Input for 'Has Pepperoni?' Input must be yes or no")
else: 
    print("Invalid Size Input. Please enter one of the following: small, medium, large ")

# Display Customer Ticket 

print("Your total is: ", customer_total )