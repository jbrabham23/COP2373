# Jadyn Brabham
# Chapter 1, Assignment 1
# This program will prompt the user to purchase cinema tickets, with each
# user allowed to purchase a maximum of 4 tickets. Only 20 tickets will be
# available for sale in total. The program will ask the user for the total
# number of tickets they wish to purchase. After each customer's purchase,
# the program will show how many tickets remain. The process will repeat
# until all 20 tickets are sold, and then the program will display the
# total number of buyers.

# The handle_ticket_purchase() function prompts the user to input the
# amount of tickets they would like to buy. It validates the input by
# using an if statement to ensure the buyer does not buy more than 4
# tickets or 0 or fewer tickets. If the input is valid, the function will
# update the ticket count.
def handle_ticket_purchase(total_tickets, max_tickets):
    # Prompt the user to input the number of tickets they wish to buy
    while True:
        try:
            # Ask the user to enter the amount of tickets they wish to buy.
            tickets_to_buy = int(input(f'How many cinema tickets would you like to '
                                       f'buy? (Max {max_tickets}) Remaining '
                                       f'tickets: {total_tickets}: '))

            # Check if the user tries to buy more than 4 tickets.
            if tickets_to_buy > max_tickets:
                print(f'Sorry, you can only buy up to {max_tickets} tickets'
                      f' at a time.')

            # Check if the user tries to buy zero or a negative number of
            # tickets.
            elif tickets_to_buy <= 0:
                print('Please enter a positive number of tickets.')

            # Check if there are enough tickets available for the purchase.
            elif tickets_to_buy <= total_tickets:

                # Reduce the remaining tickets.
                total_tickets -= tickets_to_buy

                # Return the number of tickets the user bought and
                # the amount of tickets left.
                return tickets_to_buy, total_tickets

            # If the user tries to buy more tickets than are left,
            # ask the user to purchase fewer tickets.
            else:
                print(f'Sorry, there are only {total_tickets} tickets left.'
                      f'Please purchase fewer tickets.')

       # Prints a message if the user does not enter a valid number.
        except ValueError:
            print('Invalid input. Please enter a valid number.')

# The sell_tickets() function coordinates the overall ticket-selling
# process. It initializes the variables and accumulator used in the program.
# The function uses a loop to continue to allow the user to buy tickets until
# all the tickets are sold. It will display a message that tells the user
# how many tickets they purchased and how many tickets are left. Once all
# 20 tickets are purchased, it will display the total number of buyers.
def sell_tickets():

    # Initialize the variables and accumulator.
    # Total tickets available for purchase
    total_tickets = 20

    # Maximum number of tickets per buyer
    max_tickets = 4

    # Accumulator for the number of buyers
    total_buyers = 0

    # While loop to continue the program until all the tickets are sold.
    while total_tickets > 0:
        tickets_bought, total_tickets = handle_ticket_purchase(total_tickets, max_tickets)

        total_buyers += 1

        print(f'Thank you for your purchase. {tickets_bought} ticket(s) bought.'
              f'{total_tickets} tickets left.')

    # Display the total number of buyers once all tickets are sold.
    print(f'All tickets have been sold. {total_buyers} people bought tickets.')

# Start the ticket-selling process.
sell_tickets()