count_of_numbers = int(input())
even = 0
odd = 0

for position in range(1, count_of_numbers + 1):
    element = int(input())
    if position % 2 == 0:
        even += element
    else:
        odd += element

difference = abs(even - odd)

if even == odd:
    print("Yes")
    print(f"Sum = {even}")
else:
    print("No")
    print(f"Diff = {difference}")


