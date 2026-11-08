nums = []

for _ in range(8):
    n = int(input())
    nums.append(n)

print(f"First 4: {nums[:4]}")
print(f"Last 4: {nums[-4:]}")
print(f"Alternate: {nums[0::2]}")
nums.reverse()
print(f"Reversed: {nums}")