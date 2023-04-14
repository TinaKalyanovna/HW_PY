
# Задача 14: Требуется вывести все целые 
# степени двойки (т.е. числа вида 2k), не 
# превосходящие числа N.


n = int(input('Введите число n '))
stop = 0
m = 2
for i in range(n):
    if stop != 1:
        m = m ** i
        if m <= n:
            print(m, end=' ')
            m = 2
        else:
            stop = 1
    else:
        i = n
