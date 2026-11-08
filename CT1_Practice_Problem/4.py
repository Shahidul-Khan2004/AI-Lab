n = int(input("Enter a positive number: "))

f = 1

while(n > 1):
    f *= n
    n -= 1

print(f"Factorial: {f}")