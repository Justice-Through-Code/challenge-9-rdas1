
# 1.1 TODO: Create a function called validate_user_input that will
# - ask the user for a number: 'Please enter a number'
# - try to return the user's input as an integer
# - if the user did not input a number, tell them 'You did not enter a valid number, please try again'
# - continue to ask them for a valid number until they input one
# - once a valid number is received, return that number

# NOTE: What type of error does python throw if you try to turn a non-number string into an integer?
# Test it out (or google it!) to see which one. Specifically catch that exception in your code.
def validate_user_input():
    entered = input("Please enter a number: ")
    try:
        return(int(entered))
    except ValueError:
        print("You did not enter a valid number, please try again")
        return validate_user_input()

'''
def validate_user_input():
    # TAs NOTE: there are a few different ways to do this! We don't need to worry about perfect efficiency,
    # if it works, it works
    is_num = False

    while not is_num:
        num = input('Please enter a number: ')
        try:
            # `return` breaks out of the while loop (and the function)
            return int(num)
        except ValueError:
            print('You did not enter a valid number, please try again')
'''

# 1.2 TODO: Once you are done, uncomment the two lines below to ensure that your code works as expected

user_number = validate_user_input()
print(f'The number the user entered is {user_number}.')


# 2.1 TODO: Create a function called print_tenth_item that will
# - take in a list of items as a parameter called `top_ten`
# - try to print out an f-string stating the 10th item in the list (NOTE: what index is the 10th item in the list?)
# - if there are not ten items in the list, tell the user that it is not applicable: 'N/A'

# NOTE: What type of error does python throw if you try to index into a list past the number of items in it?
# Test it out (or google it!) to see which one. Specifically catch that exception in your code.
def print_tenth_item(top_ten : list):
    try:
        print(top_ten[9])
    except IndexError:
        print("N/A")
# 2.2 TODO: Once you are done, uncomment the two lines below to ensure that your code works as expected

print_tenth_item(['a', 'b', 'c'])  # Should print out that there are not ten items in the list
print_tenth_item([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Should print out the 10th item in the list
