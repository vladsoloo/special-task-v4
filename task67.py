k = int(input("День недели (от 1 до 7): "))

if k < 1 or k > 7:
    print("Некорректный ввод. День недели должен быть числом от 1 до 7.")
elif (k + 5) % 7 < 5:
    print("Работа")
else:
    print("Отдых")
