user_number = int(input("Введите число >>> "))
number1 = user_number
number2 = int(str(user_number) + str(user_number))
number3 = int(str(user_number) + str(user_number) + str(user_number))

result = number1 + number2 + number3
print(f"Итог: {result}")
