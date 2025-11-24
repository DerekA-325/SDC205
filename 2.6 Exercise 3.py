print("derave1577")

price = 0
subTotal = 0
taxRate = 0.07

for counter in range(5):
    price = float(input("Enter the price of the item: "))
    subTotal = subTotal + price

salesTax = subTotal * taxRate
total = subTotal + salesTax

print(f'Subtotal: {subTotal:,.2f}')
print(f'Sales Tax: {salesTax:,.2f}')
print(f'Total: {total:,.2f}')
