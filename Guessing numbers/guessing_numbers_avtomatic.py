from random import *

num = randrange(int(input("До какого числа будешь ваш диапозон ?")))

n1 = 1
n2 = num

t = 0

while True:
    middle = (n1 + n2) // 2
    t += 1
    if middle == num:
        print("Победа")
        print(f"Число было {num}, Количество попыток {t}")
        break
    elif middle < num:
        n1 = middle + 1
        continue
    elif middle > num:
        n2 = middle - 1
        continue
