print("Задача 1. Сумма чисел от 1 до N")
N = int(input("Введите натуральное число N: "))
summa = 0
for i in range(1, N + 1):
    summa += i
print(f"Сумма чисел от 1 до {N} = {summa}")

print("\nЗадача 2. Обратный отсчёт")
N = int(input("Введите число N: "))
i = N
while i >= 1:
    print(i, end=" ")
    i -= 1
print("\nПуск!")
