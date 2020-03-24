#!/usr/bin/env python
# set max & min
max_value = 26
min_value = 0

# while true
while True:
#      calculate guess
    guess = (max_value + min_value) // 2
# create message for user
    user_prompt = "Is {} your number? ".format(guess)
#      ask user if guess if correct
    user_input = input(user_prompt)
#      if answer is y
    if user_input == 'y':
        #         print message and exit
        print("Yay!")
        break
        #      if answer is h
    elif user_input == 'h':
        #         set max to guess
        max_value = guess
#      if answer is l
    elif user_input == 'l':
#         set min to guess
        min_value = guess
#      else:
    else:
        print("Pleae enter y, h, or l")
#         print message
