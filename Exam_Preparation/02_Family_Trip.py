budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_costs_percent = int(input())
if nights > 7:
    price_per_night *= 0.95
additional_costs = budget * additional_costs_percent / 100
needed_money = nights * price_per_night + additional_costs
difference = abs(budget - needed_money)
if budget >= needed_money:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")