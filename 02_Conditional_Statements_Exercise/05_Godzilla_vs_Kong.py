budget = float(input())
people_count = int(input())
clothing_for_one = float(input())

decor = budget * 0.10
if people_count > 150:
    clothing_for_one = clothing_for_one * 0.90

money_needed = decor + people_count * clothing_for_one

if money_needed > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {money_needed - budget :.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - money_needed :.2f} leva left.")