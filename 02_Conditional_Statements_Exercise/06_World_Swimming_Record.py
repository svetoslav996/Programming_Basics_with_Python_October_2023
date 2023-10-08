# Входни данни
record_seconds = float(input())
distance_meters = float(input())
time_per_meter_seconds = float(input())

# Изчисление на времето в секунди, за което Иван ще преплува разстоянието
total_time_seconds = distance_meters * time_per_meter_seconds

# Изчисление на броя забавяния в резултат на съпротивлението на водата
delay_count = int(distance_meters / 15)

# Изчисление на общото време със забавянията
total_time_seconds += delay_count * 12.5

# Проверка дали Иван е подобрил рекорда
if total_time_seconds < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time_seconds:.2f} seconds.")
else:
    difference_seconds = total_time_seconds - record_seconds
    print(f"No, he failed! He was {difference_seconds:.2f} seconds slower.")