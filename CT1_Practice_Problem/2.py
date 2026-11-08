n = int(input("Enter a number: "))

if n <= 0:
    print("invalid input")

e_sum = o_sum = even = odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        e_sum += i
        even += 1
    else:
        o_sum += i
        odd += 1

print(f"Even Sum: {e_sum}\nOdd Sum: {o_sum}\nEven Count: {even}\nOdd Count: {odd}")
