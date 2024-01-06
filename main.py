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
pass
num1=int(input("Введите 1 число:"))
num2=int(input("Введите 2 число:"))
num3=int(input("Введите 3 число:"))
print("1-Показать максимум")
print("2-Показать минимум")
print("3-Показать среднее")
choice=int(input("Введите цифру: "))
if choice == 1:
    result = max(num1,num2,num3)
    print(result)
elif choice == 2:
    result = min(num1,num2,num3)
    print(result)
elif choice == 3:
    result = (num1+num2+num3)/3
    print(result)
