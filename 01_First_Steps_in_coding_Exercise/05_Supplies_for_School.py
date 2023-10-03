PEN_PRICE = 5.80
MARKER_PRICE = 7.20
BOARD_CLEANER_PRICE_PER_LITER = 1.20

packets_pens = int(input())
packets_markers = int(input())
board_cleaner_liters = int(input())
percent_discount = int(input()) / 100

total_price = (packets_pens * PEN_PRICE) + (packets_markers * MARKER_PRICE) + (board_cleaner_liters * BOARD_CLEANER_PRICE_PER_LITER)
discounted_price = total_price * (1 - percent_discount)

print(discounted_price)
