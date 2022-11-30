# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:

#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

n = int(input("Введите число: "))
list = []
x = y = 1
for i in range(n):
    list.append(x)
    x,y = y, x+y
print(list)
print()
x=0
y=1
for i in range(n+1):
    list.insert(0,x)
    x,y = y, x-y
print(list)
