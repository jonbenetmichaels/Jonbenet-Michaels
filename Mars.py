print("Welcome to Mars Mission Control!")
# Prompts the user to continue
wants_to_continue = input("Plan a mission? yes/no ")

# Runs if user decides to continue
if wants_to_continue == "yes":
    # Astronaut Information
    name = input("What is your name?")
    training = int(input("How many years of experience do you have?"))
    fuel_capacity = int(input("What is your fuel capacity (in litres)?"))
    # Mission Calculations
    # Training Experience
    training_hours = training * 2000
    print("You have ", training_hours, " hours of training")
    # Journey Math
    weeks_of_fuel = fuel_capacity // 50
    fuel_left = fuel_capacity % 50
    exact_efficiency = fuel_capacity / 50
    # Mission Resource Update
    supplies = 1000
    supplies -=150
    supplies *= 2
    print("Supply Count: ", supplies)
    # Mission Report
    print(name.upper())
    call_sign = name.upper()*3
    print("Commander ", name.upper(), ", you have ", training_hours, "training hours.\n Your fuel will last ", weeks_of_fuel, " weeks, with ", fuel_left,  "litres remaining,\n and you have ", supplies, " food packets for the journey.\n Mission Call Sign: ", call_sign)
# Runs if user decides not to continue
elif wants_to_continue == "no":
    print("No worries! Let's try again some other time.")
# Runs if no valid input is made
else:
    print("Invalid input. Program shutting down. . .")