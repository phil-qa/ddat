# Title: cmc_ex01_small_units
# Purpose : Exercise 1 write small units
# Instructions : do a  code review of the code below. What can be altered
#               Having done an initial refactor, show how your approach can extend the functionality by
#               extending this to take into account doors and windows (should not paint them
#               EXTENSION - can you extend this further to build out a quote for a house (multiple rooms)

# decorators calculator
import math


def get_wall_quote(wall_number):
    '''
    Accepts the wall number that is needs to have its dimensions gathered
    :param wall_number: number of wall used for display purposes to the user
    :return: the area or the wall
    '''
    area_of_window = 0
    area_of_door = 0

    area_of_wall = "{0}{1}".format(int(input("How high is the wall number " + str(wall_number) + "?")),
                                   int(input("How long is the wall number " + str(wall_number) + "?")))

    if input("Do you have any windows or doors for wall number " + str(wall_number) + "? (Y/N)?").upper() == 'Y':
        if input('Do you have a window? (Y/N)').upper() == 'Y':
            area_of_window = int(input("How high is the window ")) * int(input("How long is the window "))
        if input('Do you have a door? (Y/N)').upper()== 'Y':
            area_of_door = int(input("How high is the door ")) * int(input("How long is the window "))

    area_of_wall = area_of_wall - (area_of_window + area_of_door)

    return area_of_wall


def number_rooms_and_walls():
    '''
    Determines the number of the rooms and walls inputted for the users
    :return: the total cost of the job
    '''
    house_quote = str(input("Do you require a house quote(H) or just a room quote(R)?")).upper()

    room_count = 0
    room_loop_counter = 0
    room_num = 1

    total_size = 0

    if house_quote == 'H':
        room_count = int(input("How many rooms do you have?"))

        while room_loop_counter < room_count and room_count > 1:

            wall_count = int(input("How many walls do you have for room number " + str(room_num) + "?"))

            room_loop_counter = room_loop_counter + 1

            room_num = room_num + 1

            while wall_count > 0:

                total_size = get_wall_quote(wall_count)

                wall_count = wall_count - 1

    else:

        total_size = get_wall_quote(int(1))

        room_loop_counter = room_loop_counter + 1

    total_cost = paint_coverage(total_size)

    return total_cost


def paint_coverage(total_size):
    '''
    Accepts the total wall size of all the rooms entered in and works out the cost
    :param total_size: total size of the area of th job
    :return: the cost of the job
    '''
    coverage_of_tin_of_paint = int(input("how much in square meters will a single tin cover "))

    cost_of_tin = float(input("How much is a tin of paint £"))

    total_number_of_tins = math.ceil(total_size/coverage_of_tin_of_paint)

    total_cost = total_number_of_tins * cost_of_tin

    return total_cost


total_cost_of_job = number_rooms_and_walls()


print(f"The total cost of the paint is £{total_cost_of_job:.2f}")
