# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# a = input("Enter number:   ")
# a = int(a)
#
# a1 = 0
# a2 = 1
# fib = a1 + a2
# if a == 0:
#     print(0)
# elif a == fib:
#      print(fib)
# else:
#     print(-1)

a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
n = 1
while (fib_next <= a):
    if fib_next == a:

print(n)
    break
    fib_prev, fib_next = fib_next, fib_prev + fib_next
    n += 1
else:
    print(-1)