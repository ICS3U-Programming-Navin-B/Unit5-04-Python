#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Jan 27 2022
# This program will  gets two numbers and an operation
# from the user, it then calculates a solution using
# the inputs.
import math


# this function calculates the solution
def calculate(sign, first_number, second_number):
    if sign == "+":
        solution = first_number + second_number
    elif sign == "-":
        solution = first_number - second_number
    elif sign == "*":
        solution = first_number * second_number
    elif sign == "/":
        solution = first_number / second_number
    elif sign == "%":
        solution = first_number % second_number
    # error checking
    else:
        solution = -1
        # send answer to main
    return solution


def main():
    number1_string = input("Enter the first number: ")
    operation = input("Enter the operation (+, -, *, /, %): ")
    number2_string = input("Enter the second number: ")
    try:
        number1 = float(number1_string)
        number2 = float(number2_string)
        solution_main = calculate(operation, number1, number2)
        if solution_main == -1:
            print("Invalid input(s).")
        else:
            print("The solution is {}.". format(solution_main))
    except Exception:
        print("Invalid input(s).")


if __name__ == "__main__":
    main()
