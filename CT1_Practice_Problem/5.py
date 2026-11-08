n = int(input("Enter a positive number: "))

tmp = n
total = sum = 0
last = tmp % 10

while(tmp != 0):
    sum += tmp % 10
    tmp //= 10
    total += 1

print(f"Total Digits: {total}\nSum of Digits: {sum}\nLast Digit: {last}")