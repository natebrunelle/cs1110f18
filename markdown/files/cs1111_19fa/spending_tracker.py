# scoping: global and local variables
# use global variable to keep track of expense today
# use local variable to keep track of expense each shop

# imaging you are buying breakfast, lunch, snack, coffee, soda, dinner

# write a summary of how many shops you visit and
# how much you have spent in total today

# write a function that accumulates how much you pay in each shop


def money_spend(cost):
    global total_expense
    total_expense += cost


number_shops = 0
total_expense = 0

money_spend(5)     # shop1
money_spend(4)     # shop2
money_spend(2)     # shop3
money_spend(7)     # shop4
money_spend(5)     # shop5
money_spend(12)    # shop6

print(total_expense)
