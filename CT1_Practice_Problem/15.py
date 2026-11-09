n = int(input("Enter the number of products: "))
prices = []
prices = list(map(int, input("Enter prices: ").split(",")))

def main():
    total = count = 0
    for price in prices:
        total += price
        if price > 500:
            count += 1

    discount = 0
    if 1000 <= total < 3000:
        discount = total * 0.05
    elif total >= 3000:
        discount = total * 0.1

    print(f"Total Bill: {total}\nProducts Above 500: {count}\nDiscount: {discount}\nFinal Bill: {total - discount}")

if len(prices) != n:
    print("Invalid number of prices!")
else:
    main()