first_day_result = int(input("Введите результат первого дня >>> "))
wanted_result = int(input("Введите желаемый результат >>> "))

if first_day_result >= wanted_result:
    print("Результат первого дня должен быть меньше желаемого")
    exit(1)

current_day_result = first_day_result
day = 1
while current_day_result < wanted_result:
    current_day_result = current_day_result * 1.1
    day += 1

    if day >= 365:
        print("Уже год бежим, что-то долго =)")
        break
if day < 365:
    print(f"На {day} день спортсмен достигнет результата {current_day_result} км")
