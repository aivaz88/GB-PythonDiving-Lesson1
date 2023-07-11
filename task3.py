# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

num = randint(0, 1000)
print('Программа загадала число от 0 до 1000. Угадай!')
count = 1

while count <= 10:
    answer = int(input(f'Попытка №{count}: '))
    if answer < num:
        print('больше')
    elif answer > num:
        print('меньше')
    else:
        print('Угадал')
        break
    count += 1
else:
    print('Ты проиграл!')
