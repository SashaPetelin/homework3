# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import randint
import random
import math

list = []
list2 = []
for i in range(randint(10,15)):
    list.append(random.uniform(-100,100))
print()
print(list)
print()
for i in range(len(list)):
    fract = list[i]-int(list[i])
    list2.append(abs(fract))
print(list2)
print()

def dif (list):
    i = 0
    max = list[i]
    min = list[i]
    while i<len(list):
        if list[i]>max:
            max = list[i]
        elif list[i]<min:
            min = list[i]
        i+=1
    print("Максимальное значение дробной части = ", round(max,3))
    print("Минимальное значение дробной части = ", round(min,3))
    print()
    return (round((max-min),3))

print("Разница между максимальным и минимальным значением дробной части равна ", dif(list2))
