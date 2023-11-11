budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0
if season == "Winter":
    if destination == "Dubai":
        price_per_day = 45000 * 0.7
    elif destination == "Sofia":
        price_per_day = 17000 * 1.25
    elif destination == "London":
        price_per_day = 24000
elif season == "Summer":
    if destination == "Dubai":
        price_per_day = 40000 * 0.7
    elif destination == "Sofia":
        price_per_day = 12500 * 1.25
    elif destination == "London":
        price_per_day = 20250
needed_money = days * price_per_day
difference = abs(budget - needed_money)
if budget >= needed_money:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")