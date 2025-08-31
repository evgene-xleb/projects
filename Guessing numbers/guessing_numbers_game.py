from random import *

num = randint(1, 100)

print("Добро пожаловать в игру. Ваша задача угадать число от 1 до 100")

t = 0

def is_valid(num):
    if num.isalpha():
        return False
    if 1 <= int(num) <= 100:
        return True
    
while True:
    try_num = input("Ваше число ?")
    if is_valid(try_num):
        t += 1
        if int(try_num) == num:
            print()
            print("Победа, ты угадал!")
            print()
            print(f"Число: {num} Попыток: {t}")
            print()
            print("Спасибо что сыграли в числовую угадайку. Еще увидимся...")
            break
        elif int(try_num) < num:
            print("Загаданое число больше !")
            continue
        elif int(try_num) > num:
            print("Загаданое число меньше !")
            continue
    else:
        print("А может быть все-таки введем целое число от 1 до 100?")

