nums = []

for _ in range(8):
    n = int(input())
    nums.append(n)

pos = neg = zero = 0

for i in nums:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1

print(f"Postive: {pos}\nNegative: {neg}\nZero: {zero}")