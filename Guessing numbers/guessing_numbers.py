from random import *

random_num = randint(1, 100)

print(random_num)

while True:
    attempt = int(input())
    if attempt == random_num:
        print("Поздравляю вы угадали число")
        break
    elif attempt >= random_num:
        print("Слишком много, попробуйте еще раз")
        continue
    elif attempt <= random_num:
        print("Слишком мало, попробуйите еще раз")
        continue  