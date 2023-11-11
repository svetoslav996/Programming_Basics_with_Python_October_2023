days = int(input())
total_food = float(input())
total_biscuits = 0
food_eaten_by_dog = 0
food_eaten_by_cat = 0
for current_day in range(1, days + 1):
    current_day_eaten_by_dog = int(input())
    current_day_eaten_by_cat = int(input())
    food_eaten_by_dog += current_day_eaten_by_dog
    food_eaten_by_cat += current_day_eaten_by_cat
    if current_day % 3 == 0:
        total_biscuits += \
            (current_day_eaten_by_dog + current_day_eaten_by_cat) * 0.1
total_food_eaten_by_cat_and_dog = food_eaten_by_dog + food_eaten_by_cat
total_food_eaten_as_percent = total_food_eaten_by_cat_and_dog / total_food * 100
food_eaten_by_dog_as_percent = food_eaten_by_dog / total_food_eaten_by_cat_and_dog * 100
food_eaten_by_cat_as_percent = food_eaten_by_cat / total_food_eaten_by_cat_and_dog * 100

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{total_food_eaten_as_percent:.2f}% of the food has been eaten.")
print(f"{food_eaten_by_dog_as_percent:.2f}% eaten from the dog.")
print(f"{food_eaten_by_cat_as_percent:.2f}% eaten from the cat.")
