# Generate coin change in the least amount of coins for any given amount of pennies provided.

import math

def coin_change(pennies):
    change =  round((((pennies / 25) - math.floor(pennies / 25)) * 25))
    if pennies % 25 == 0:
        return "Your change for " + str(pennies) + " pennies is: "  + str(pennies / 25) + " quarters."
    elif change % 25 == 20:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters and 2 dimes."
    elif change % 25 == 19:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 dime, 1 nickel, and 4 pennies."
    elif change % 25 == 18:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 dime, 1 nickel, and 3 pennies."
    elif change % 25 == 17:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 dime, 1 nickel, and 2 pennies."
    elif change % 25 == 16:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 dime, 1 nickel, and 1 penny."
    elif change % 25 == 15:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 dime, and 1 nickel."
    elif change % 25 == 14:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 dime, 1 nickel, and 4 pennies."
    elif change % 25 == 13:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 dime, 1 nickel, and 3 pennies."
    elif change % 25 == 12:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 dime, 1 nickel, and 2 pennies."
    elif change % 25 == 11:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 dime, 1 nickel, and 1 penny."
    elif change % 25 == 10: 
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters and 1 dime."
    elif change % 25 == 9:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 nickel, and 4 pennies."
    elif change % 25 == 8:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 nickel, and 3 pennies."
    elif change % 25 == 7:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 nickel, and 2 pennies."
    elif change % 25 == 6:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters, 1 nickel, and 1 pennies."
    elif change % 25 == 5:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters and 1 nickel."
    elif change % 25 == 4:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters and 4 pennies."
    elif change % 25 == 3:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters and 3 pennies."
    elif change % 25 == 2:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters and 2 pennies."
    elif change % 25 == 1:
        return "Your change for " + str(pennies) + " pennies is: "  + str(math.floor(pennies / 25)) + " quarters and 1 penny."


# Change the number of pennies below to get the exact change.
print(coin_change(1017))