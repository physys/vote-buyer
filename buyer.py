import pyautogui
import sys
import time

print("""
************************************
IMPORTANT!
Save all work and open documents! This script can accidentally close any open window if
the mouse is moved while it is clicking!

This script will click a number of times where you place the mouse based on the inputs.
It doesn't know what it's clicking on, it doesn't know what you're using it for, and it
can't tell if anything has gone wrong during the process. 

It can be hard to stop if there is an emergency.
You cannot use other programs while it is running.

You can force it to stop clicking by moving the cursor to a corner of the screen you started the script on.
************************************
""")

while True:
    try:
        vote_cost = max(int(input("Enter cost of a single vote: ")), 1)
        current_coins = int(input("Enter your current coin total: "))
        target_coins = int(input("Enter minimum amount of coins you want to have after buying votes: "))
    except ValueError:
        print("You entered something that couldn't be interpreted as a number...")
        continue

    # Check to see if the user has enough coins to cover the cost of at least 1 vote
    if current_coins < vote_cost:
        print(f"You have {current_coins} but the cost of a vote is {vote_cost}.")
        restart = input("Restart? (y/n): ")
        # If the user responds with any version of 'y' or 'yes', go back to the top of the main while loop
        if restart.lower() in ['y', 'yes']:
            continue
        else:
            sys.exit()

    # Can't end with more coins than you have
    elif target_coins > current_coins:
        print("You can't end up with more coins than you started with, you silly head!")
        continue

    # Can't buy any votes and end up with the target
    elif target_coins > (current_coins - vote_cost):
        print(f"You aren't able to buy any votes and still end up with {target_coins}.")
        continue

    else:
        # Difference of current and target is what we have to spend, floor divide by cost to get whole number of votes
        num_clicks = (current_coins - target_coins) // vote_cost
        seconds = round(num_clicks * .2)

        print(f"\nIf the site doesn't lag and nothing goes wrong, you'll have {num_clicks} more votes\n"
              f"and you'll be left with {current_coins - num_clicks * vote_cost} coins.\n"
              f"This process will take {time.strftime('%M', time.gmtime(seconds))} minute(s) and "
              f"{time.strftime('%S', time.gmtime(seconds))} second(s).\n")
        input("Without clicking, move your cursor over the buy button and press any key to start buying votes.\n"
              "Make sure you don't bump your cursor after it starts!\n")

        for num in range(num_clicks):
            print(f"Click {num + 1} of {num_clicks} | {round((num + 1) * 100 / num_clicks)}%", end='\r')
            pyautogui.click()
            time.sleep(.2)

        input("Done!\n\nPress any key to quit.")
        sys.exit()

