account_balance = 25000.0
daily_limit_remaining = 10000.0

print(f"--- Welcome to the ATM ---")
print(f"Available Balance: ₹{account_balance}")
print(f"Remaining Daily Limit: ₹{daily_limit_remaining}\n")


amount = float(input("Enter the amount to withdraw: "))


if amount <= 0:
    print("Error: Invalid amount entered.")

elif amount % 100 != 0:
    print("Error: Amount must be a multiple of 100.")

elif amount > account_balance:
    print("Error: Insufficient balance available.")

elif amount > daily_limit_remaining:
    print("Error: This transaction exceeds your remaining daily limit.")

else:    
    account_balance -= amount
    daily_limit_remaining -= amount
    print("\nTransaction Successful!")
    print(f"Please collect your cash: ₹{amount}")
    print(f"Updated Balance: ₹{account_balance}")