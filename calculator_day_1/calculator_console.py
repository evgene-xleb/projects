import math

# Простой функционал
# Сложение, вычитание, умножение, деление


def mult(a, b):  # умножение
    return a * b


def addition(a, b):  # сложение
    return a + b


def subtraction(a, b):  # вычитание
    return a - b


def division(a, b):  # делене
    return a // b


def calculator():
    print("Приветствую вас в калькуляторе")
    print("Ваши действия:\n1) Умножение\n2) Деление\n3) Сложение\n4) Вычитание")
    choise = int(input())
    num1 = int(input("Число 1: "))
    num2 = int(input("Число 2: "))
    if choise == 1:
        print(mult(num1, num2))
    elif choise == 2:
        print(division(num1, num2))
    elif choise == 3:
        print(addition(num1, num2))
    elif choise == 4:
        print(subtraction(num1, num2))


calculator()


print("Hello World ")
