text = input()
sum_of_points = 0
for character in text:
    if character == "a":
        sum_of_points += 1
    elif character == "e":
        sum_of_points += 2
    elif character == "i":
        sum_of_points += 3
    elif character == "o":
        sum_of_points += 4
    elif character == "u":
        sum_of_points += 5

print(sum_of_points)
