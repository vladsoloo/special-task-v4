masti = ["Пики", "Трефы", "Бубны", "Червы"]

n = int(input("Введите номер масти (1-4): "))

if n >= 1 and n <= 4:
    print(masti[n-1])
else:
    print("Ошибка: неверный номер масти.")
