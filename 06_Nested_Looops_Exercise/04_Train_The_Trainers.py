judges_count = int(input())

presentation_count = 0
total_score = 0

command = input()
while command != "Finish":
    presentation = command

    current_score = 0
    for _ in range(judges_count):
        judge_score = float(input())
        current_score += judge_score

    avg_score = current_score / judges_count
    print(f"{presentation} - {avg_score:.2f}.")
    total_score += current_score

    presentation_count += 1
    command = input()

total_avg_score = total_score / (presentation_count * judges_count)
print(f"Student's final assessment is {total_avg_score:.2f}.")
