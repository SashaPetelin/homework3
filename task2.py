# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint

list = []
list2 = []
for i in range(randint(7,13)):
    list.append(randint(-100,100))
print()
print(list)

size = (len(list))
mid = len(list)/2
for i in range(size):
    while i<mid and size>mid:
        size=size-1
        x = list[i]*list[size]
        list2.append(x)
        i+=1
print(list2)


