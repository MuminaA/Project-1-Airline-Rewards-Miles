# collect input on name, is a member, how many miles, cost of ticket
customer_name = input("What is the customer's name?\n")
member_status = input("Is the customer a member (y/n)?\n")
member_miles = int(input("How many miles does the customer have?\n"))
ticket_cost = float(input("What was the cost of their ticket?\n"))


# find if customer is loyal rewards member
if member_status == "y" and member_miles >= 0 and ticket_cost >= 0:
    print(f"Dear {customer_name},")
    print('')
    #if base
    if member_miles < 25000:
        miles_earned = int(ticket_cost) * 5
        new_miles = (member_miles + miles_earned)
        print('You are a member of SpartanAir loyalty rewards and are currently at Base tier.')
        print(f'Your recent ticket purchase of ${ticket_cost:.2f} has earned you {miles_earned} miles.')
        if new_miles >= 25000 or new_miles <= 25000: #member_miles >= 0 and ticket_cost >= 0:
            print(f'Your total number of miles has increased from {member_miles} miles to {new_miles} miles.')
        if new_miles >= 25000 and new_miles < 50000:
            print("You are eligible for a status upgrade from Base to Silver.")
        if new_miles >= 50000 and new_miles < 75000:
            print("You are eligible for a status upgrade from Base to Gold.")
        if new_miles >= 75000 and new_miles < 125000:
            print("You are eligible for a status upgrade from Base to Platinum.")
        if new_miles >= 125000:
            print("You are eligible for a status upgrade from Base to Diamond.")
    #if silver
    elif member_miles < 50000:
        miles_earned = int(ticket_cost) * 7
        new_miles = (member_miles + miles_earned)
        print('You are a member of SpartanAir loyalty rewards and are currently at Silver tier.')
        print(f'Your recent ticket purchase of ${ticket_cost:.2f} has earned you {miles_earned} miles.')
        if new_miles >= 50000 or new_miles <= 50000:
            print(f'Your total number of miles has increased from {member_miles} miles to {new_miles} miles.')
        if new_miles >= 50000 and new_miles < 75000:
            print("You are eligible for a status upgrade from Silver to Gold.")
        if new_miles >= 75000 and new_miles < 125000:
            print("You are eligible for a status upgrade from Silver to Platinum.")
        if new_miles >= 125000:
            print("You are eligible for a status upgrade from Silver to Diamond.")
    #if gold
    elif member_miles < 75000:
        miles_earned = int(ticket_cost) * 8
        new_miles = (member_miles + miles_earned)
        print('You are a member of SpartanAir loyalty rewards and are currently at Gold tier.')
        print(f'Your recent ticket purchase of ${ticket_cost:.2f} has earned you {miles_earned} miles.')
        if new_miles >= 75000 or new_miles <= 75000:
            print(f'Your total number of miles has increased from {member_miles} miles to {new_miles} miles.')
        if new_miles >= 75000 and new_miles < 125000:
            print("You are eligible for a status upgrade from Gold to Platinum.")
        if new_miles >= 125000:
            print("You are eligible for a status upgrade from Gold to Diamond.")
    #if plat
    elif member_miles < 125000:
        miles_earned = int(ticket_cost) * 9
        new_miles = (member_miles + miles_earned)
        print('You are a member of SpartanAir loyalty rewards and are currently at Platinum tier.')
        print(f'Your recent ticket purchase of ${ticket_cost:.2f} has earned you {miles_earned} miles.')
        if new_miles >= 125000 or new_miles <= 125000:
            print(f'Your total number of miles has increased from {member_miles} miles to {new_miles} miles.')
        if new_miles >= 125000:
            print("You are eligible for a status upgrade from Platinum to Diamond.")
    #if diamond
    elif member_miles >= 125000:
        miles_earned = int(ticket_cost) * 11
        new_miles = (member_miles + miles_earned)
        print('You are a member of SpartanAir loyalty rewards and are currently at Diamond tier.')
        print(f'Your recent ticket purchase of ${ticket_cost:.2f} has earned you {miles_earned} miles.')
        if new_miles >= 125000 or new_miles <= 125000:
            print(f'Your total number of miles has increased from {member_miles} miles to {new_miles} miles.')
# if customer is NOT loyal rewards member, output this
elif member_status == "n" and member_miles >= 0 and ticket_cost >= 0:
    miles_earned = int(ticket_cost) * 5
    new_miles = (member_miles + miles_earned)
    print(f"Dear {customer_name},")
    print('')
    print('SpartanAir would like to invite you to become a loyalty rewards member.')
    print(F'As a Base tier member, your recent ticket purchase of ${ticket_cost:.2f} would earn you {miles_earned} miles.')
# if customer inputs negative numbers, output this
else:
    print("ERROR: Number of miles or ticket cost is less than zero.")