print("Задача 3. Чётные числа от 1 до 50")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

print("\nЗадача 4. Валидация возраста")
while True:
    age = int(input("Введите возраст (0-120): "))
    if 0 <= age <= 120:
        print(f"Возраст принят: {age}")
        break
    else:
        print("Ошибка! Возраст должен быть от 0 до 120 лет.")
