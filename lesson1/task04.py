user_number = int(input("Введите число >>> "))
number = str(user_number)
max_digit = 0
counter = len(number) - 1
while counter >= 0:
    current_digit = int(number[counter])
    if current_digit > max_digit:
        max_digit = current_digit
    counter -= 1

print(f"Максимальная цифра: {max_digit}")
