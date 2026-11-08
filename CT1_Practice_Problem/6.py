marks = []

for _ in range(6):
    n = int(input())
    marks.append(n)

total = sum(marks)
average = total / len(marks)

passed_count = 0
for mark in marks:
    if mark >= 50:
        passed_count += 1

print(f"First 3: {marks[:3]}")
print(f"Last 3: {marks[-3:]}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Passed Subjects: {passed_count}")