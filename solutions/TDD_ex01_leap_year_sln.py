# Title: TDD_ex01_leap_year
# Purpose : To implement Test driven development principles
# Instructions : Create a feature to take a user input for a year value and respond if it is a
#                leap year or not
#                The rules for a leap year are :
#                it is a leap year if the year is divisible by 4
#                except if the year is divisible by 100 then it is not a leap year
#                unless the year is divisible by 400 then it is a leap year
#                implement the feature using tdd principles. Isolate the elements and consider the GWT construct

#               NOTE : A boilerpolate code file is provided, Baretest.py

#TODO Implement the feature
class Leaper():
    @staticmethod
    def response(year):
        message = ""
        if Leaper._validate_input(year):
            
            message = f"{year} is a valid year"
        else:
            message = f"{year} is not a valid year"
            return message
        year = int(year)
        if Leaper._divisible_by_4(year) and (not Leaper._divisible_by_100(year) or Leaper._divisible_by_400(year)):
            message += "\nThis is a leap year"
        else:
            message += "\nThis is not a leap year"
        return message


    def _validate_input(user_input):
        try:
            int(user_input)
            return True
        except:
            return False

    @staticmethod
    def _divisible_by_4(number):
        return number%4 == 0

    @staticmethod
    def _divisible_by_100(number):
        return number%100 == 0

    @staticmethod
    def _divisible_by_400(number):
        return number%400 == 0