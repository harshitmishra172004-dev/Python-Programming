#To calculate the final bill for an e-commerce order by applying discount slabs using an elif ladder
total_amount = float(input("Enter the total amount of the order: "))

if total_amount >= 1000:
    discount = 0.2 * total_amount
elif total_amount >= 500:
    discount = 0.1 * total_amount
else:
    discount = 0

final_bill = total_amount - discount
print(f"The final bill amount is: {final_bill}")
