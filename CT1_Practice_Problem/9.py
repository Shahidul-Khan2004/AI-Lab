nums = []

for _ in range(5):
    n = int(input())
    nums.append(n)

largest = float('-inf')
smallest = float('inf')

for i in nums:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print(f"Largest: {largest}\nSmallest: {smallest}\nDifference: {largest - smallest}")