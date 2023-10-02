# Title:CPD_ex10_solid
# Purpose : Refactor to meet SRP
# Instructions : Review the calculator code below, currently it is in a simple script
#               Form and does many things. Consider that this can be refactored to
#               extract elements where single functionality can be expressed. Once done
#               reflect on if your activities have made it more extensible.

from logos import calculator_logo

print(calculator_logo)
while True:
    number_of_numbers = int(input("How many numbers are to be worked on :"))
    operation = input("What operation is to be applied to the numbers:\na) Add"
                      "\ns) Subtract (first number is the start)\nd) Divide (first number is the start)\n"
                      "m) Multiply(first number is the start)\nav) Average\nq)quit\n>> ")
    numbers = []
    for seq in range(number_of_numbers):
        numbers.append(float(input("Enter number : ")))

    result = 0

    if operation.lower() not in ['s','a','d','m','av']:
        print('unknown operation')
    elif operation.lower() == 'a':
        for num in numbers:
            result += num
    elif operation.lower() == 's':
        result = numbers[0]
        for num in numbers[1:]:
            result-=num
    elif operation.lower() == 'd':
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
    elif operation.lower() == 'm':
        result = numbers[0]
        for num in numbers[1:]:
            result *= num
    elif operation.lower() == 'av':
        result = numbers[0]
        for num in numbers[1:]:
            result *= num
            result = result / len(numbers)
    elif operation.lower() == 'q':
        break

    print(f'The result of the operation is {result}')

