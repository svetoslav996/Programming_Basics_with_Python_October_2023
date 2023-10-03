CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50

chicken_menus = int(input()) * CHICKEN_MENU_PRICE
fish_menus = int(input()) * FISH_MENU_PRICE
vegetarian_menus = int(input()) * VEGETARIAN_MENU_PRICE
total_price_menus = chicken_menus + fish_menus + vegetarian_menus
dessert_price = total_price_menus * 0.20

total_price = total_price_menus + dessert_price + DELIVERY_PRICE
print(total_price)