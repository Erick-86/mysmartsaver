print("WELCOME TO mySMARTSAVER")

# Variables
frequency = input("How would you like to save:\n 1. Daily\n 2. Weekly\n 3. Monthly").capitalize()
amount_to_save = int(input(f"How much would you like to save {frequency.lower()}: "))
period_goal = str(input("Do you have a period, or a goal to reach:\n 1. Period\n 2. Goal").lower())

amount_saved = 0
goal_reached = 0