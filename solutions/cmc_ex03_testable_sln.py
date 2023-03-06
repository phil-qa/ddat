# Title:cmc_ex03_testable.py
# Purpose : To determine processes for making things more testable
# Instructions :The following code is to check the strength of a user input
# for a password. Refactor the code making it testable also it’s not that functional so make it functional. Try
# and write tests for it (inline or using unit tests)
# The following criteria are required :
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