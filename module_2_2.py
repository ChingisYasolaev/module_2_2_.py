first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and first == third:
    print('совпадений ', 3)
elif first == second or first == third or second == third:
    print('совпадений ', 2)
else:
    print('совпадений ', 0)
