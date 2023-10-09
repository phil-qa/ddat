# Title:cmc_ex03_testable.py
# Purpose : To determine processes for making things more testable
# Instructions :The following code is to check the strength of a user input
# for a password. Using an appropriate test framework (if necessary grab documentation for unittests at
# https://docs.python.org/3/library/unittest.html)
# Review the code below and break the elements into small units of work with acceptance criteria
# expressed in Given When Then format.
# The following criteria are required of the password :
# At least 8 chars
# At least one upper case letter
# At least one lower case letter
# At least one number
# At least one special character

# get password from the user

new_password = input("Please give a new password")
# does it pass
passing=False
for x in new_password:
    if x.isupper():
        for x in new_password:
            if x.islower():
                for x in new_password:
                    if x.isdigit():
                        passing = True
                        break



if passing:
    print("Passes")
else:
    print("nope not passing")