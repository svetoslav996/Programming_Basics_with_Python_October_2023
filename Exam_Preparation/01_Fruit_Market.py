strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())
raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

needed_money = strawberries_quantity * strawberries_price \
               + bananas_quantity * bananas_price \
               + oranges_quantity * oranges_price \
               + raspberries_quantity * raspberries_price
print(f"{needed_money:.2f}")
