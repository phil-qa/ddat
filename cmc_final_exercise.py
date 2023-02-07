# Title: cmc_final_exercise

# Purpose : To combine the learning track in clean maintainable code

# Instructions : The following code uses an imported module paint_coster.py
# to provide an estimate for painting a house. Code Review the module to see if it
# meets a standard for clean maintainable code make corrections as required

from logos import builders_logo
from paint_coster import cost_job

print(builders_logo)

while True:
    menu_choice = input("Please select an option :\n1) paint estimator \n2) exit\n>>")

    if menu_choice == "1":
        cost_of_painting = cost_job()
        print(f"The cost for painting £{cost_of_painting}")

    if menu_choice == "2":
        break
