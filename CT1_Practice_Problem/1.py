def isEven(n):
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

num :int = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
    isEven(num)
    
elif num < 0:
    print("Negative Number")
    isEven(num)
else:
    print("Zero")

print(f"Square: {num**2}")