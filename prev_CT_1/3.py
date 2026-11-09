n = int(input())

cost = 0
for _ in range(2):
    if n == 0: break
    cost += 50
    n -= 1
for _ in range(2, 5):
    if n == 0: break
    cost += 30
    n -= 1
for _ in range(n):
    cost += 20
    n -= 1

print(f"Total cost = {cost}")

'''
hours = int(input())

if hours <= 2:
    cost = hours * 50
elif hours <= 5:
    cost = 2 * 50 + (hours - 2) * 30
else:
    cost = 2 * 50 + 3 * 30 + (hours - 5) * 20

print(f"Total cost = {cost}")
'''