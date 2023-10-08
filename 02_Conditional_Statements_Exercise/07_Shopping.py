Petar_budget = float(input())
videocards = int(input())
processors = int(input())
ram_memory = int(input())

videocard_price = videocards * 250
processor_price = processors * (videocard_price * 0.35)
ram_memory_price = ram_memory * (videocard_price * 0.10)

total_price = videocard_price + processor_price + ram_memory_price
discount = 0

if videocards > processors:
    discount = total_price * 0.15

final_price = total_price - discount  # Изчисляваме крайната цена

if Petar_budget >= final_price:
    print(f"You have {Petar_budget - final_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_price - Petar_budget:.2f} leva more!")
