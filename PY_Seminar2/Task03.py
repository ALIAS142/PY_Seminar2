# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50
count, countMax = 0, 0
day = int(input("Enter day: "))
for i in range(1, day + 1):
    temp = int(input())
    if temp > 0:
        count += 1
else:
    if countMax < count:
        countMax = count
count = 0
if countMax < count:
    countMax = count
print(countMax)
