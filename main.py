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
