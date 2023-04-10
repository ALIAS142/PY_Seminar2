# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print("Enter 3-digit's number: ")
n = input()
n2 = str(n)

a = int(n2[0])
b = int(n2[1])
c = int(n2[2])
d = a+b+c

print(d)
