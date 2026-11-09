marks = list(map(int, input().split(",")))

print(f"Marks: {marks}")
print(f"Fist 3 subjects: {marks[:3]}")
print(f"Last 2 subjects: {marks[-2:]}")

marks.sort()

print(f"Highest mark: {marks[4]}")
print(f"Lowest mark: {marks[0]}")

'''
print(f"Highest mark: {max(marks)}")
print(f"Lowest mark: {min(marks)}")
'''

count = 0
for mark in marks:
    if mark > 80: count += 1

print(f"Count greater than 80: {count}")