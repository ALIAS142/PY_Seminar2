# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

n1=0
n2=1
k=1
a=int(input())
while n2<a:
    n1,n2=n2,n2+n1
    k+=1
if n2!=a:
    print("-1")
else:
    print(k)