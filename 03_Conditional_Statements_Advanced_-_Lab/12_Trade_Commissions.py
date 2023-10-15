# Входни данни
city = input()
sales = float(input())

# Инициализация на променлива за комисионната
commission = 0

# Проверка за валиден град
if city == "Sofia" or city == "Varna" or city == "Plovdiv":
    # Проверка на обема на продажбите и изчисление на комисионната
    if sales >= 0:
        if city == "Sofia":
            if sales <= 500:
                commission = 0.05 * sales
            elif sales <= 1000:
                commission = 0.07 * sales
            elif sales <= 10000:
                commission = 0.08 * sales
            else:
                commission = 0.12 * sales
        elif city == "Varna":
            if sales <= 500:
                commission = 0.045 * sales
            elif sales <= 1000:
                commission = 0.075 * sales
            elif sales <= 10000:
                commission = 0.10 * sales
            else:
                commission = 0.13 * sales
        elif city == "Plovdiv":
            if sales <= 500:
                commission = 0.055 * sales
            elif sales <= 1000:
                commission = 0.08 * sales
            elif sales <= 10000:
                commission = 0.12 * sales
            else:
                commission = 0.145 * sales
    else:
        print("error")
else:
    print("error")

# Извеждане на комисионната, форматирана до 2 цифри след десетичната точка
if commission > 0:
    print(f"{commission:.2f}")
