num = int(input("Enter a number to check: "))
if num <= 1:
    print(f"{num} is not a valid number.")
elif num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")  