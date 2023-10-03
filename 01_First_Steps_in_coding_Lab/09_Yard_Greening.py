sqMeters = float(input())
totalPrice = sqMeters * 7.61
discount = totalPrice * 0.18
finalPrice = totalPrice - discount

print(f"The final price is: {finalPrice} lv. \nThe discount is: {discount} lv.")