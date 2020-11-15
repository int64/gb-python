revenue = int(input("Введите выручку >>> "))
costs = int(input("Введите издержки >>> "))
profit = revenue - costs

if profit > 0:
    profitability = profit / revenue * 100
    print(f"Вы работаете в прибыль. Рентабельность {profitability}%")

    employees_count = int(input("Введите число сотрудников >>> "))
    employee_revenue = profit / employees_count
    print(f"Прибыль на сотрудника: {employee_revenue}")
elif profit < 0:
    print("Вы работаете в убыток")
else:
    print("Вы работаете в ноль")
