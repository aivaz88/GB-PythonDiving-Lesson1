import time

print('Загадай число от 0 до 1000. Я угадаю за 10 попыток!')
time.sleep(3)
count = 1
max_num = 1000
min_num = 0
search_num = 500
while count <= 10:
    print(f'Попытка №{count}: {search_num}')
    time.sleep(1)
    print('1 - больше \n2 - меньше\n3 - Угадал!')
    answer = int(input())
    if answer == 1:
        min_num = search_num
        search_num = min_num + (max_num - min_num) // 2
    elif answer == 2:
        max_num = search_num
        search_num = min_num + (max_num - min_num) // 2
    elif answer == 3:
        print('ИИ - сила!')
        break
    else:
        print('Эх, всю игру сломал!')
        break
    count += 1
else:
    print('Похоже где-то схитрили!')
