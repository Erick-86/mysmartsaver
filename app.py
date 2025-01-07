print("WELCOME TO mySMARTSAVER")

# Variables
frequency = input("How would you like to save:\n 1. Daily\n 2. Weekly\n 3. Monthly").capitalize()
amount_to_save = int(input(f"How much would you like to save {frequency.lower()}: "))
period_goal = str(input("Do you have a period, or a goal to reach:\n 1. Period\n 2. Goal").lower())

# goal
# period
period = 0
goal = 0

if period_goal == "period" or period_goal == "1":
    if frequency == "Daily" or frequency == "1":
        period = int(input("How many days would you like to save: "))
    elif frequency == "Weekly" or frequency == "2":
        period = int(input("How many weeks would you like to save: "))
    elif frequency == "Monthly" or frequency == "3":
        period = int(input("How many months would you like to save: "))
    else: 
        print("Invalid input")
elif period_goal == "goal" or period_goal == "2":
    goal = int(input("How much is your saving goal: "))
else: 
    print("Invalid input")

amount_saved = 0
period_time = 0

frequencies = ["Day", "Week", "Month"]

currnt_save = amount_to_save

# Saving logic
while (period_time < period and period > 0) or (amount_saved < goal and goal > 0):
    period_time += 1
    amount_saved += currnt_save

    print(f" {frequencies[0]} {period_time}: Save ${currnt_save} (Total = {amount_saved})")
    currnt_save += 1