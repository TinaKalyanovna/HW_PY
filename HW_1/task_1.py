#  Задача 2: Найдите сумму цифр трехзначного числа.

#  123 -> 6 (1 + 2 + 3)
#  100 -> 1 (1 + 0 + 0)


num = int(input('Ведите число:'))
digitsum = 0

while num > 0:
    digitsum = digitsum + num % 10
    num = num // 10

print(digitsum)    
