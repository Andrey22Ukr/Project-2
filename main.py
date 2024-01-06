num1 = int(input("Введите значение (метр)"))
print("1.Конвертировать в мили")
print("2.Конвертировать в ярды")
print("3.Конвертировать в дюймы")
choice = int(input("Выберите опцию"))
if choice == 1:
    result = (num1*1609)
    print(result)
elif choice == 2:
    result = (num1*1,9)
    print(result)
elif choice == 3:
    result = (num1*39,37)
    print(result)
else:
    print("Ошибка ввода:" )