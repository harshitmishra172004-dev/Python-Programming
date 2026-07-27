import sys

sum = 0
count = 0

for arg in sys.argv[1:]:
    sum += int(arg)
    count += 1

if count > 0:
    percentage = (sum / (count * 100)) * 100
    print(f"The percentage is: {percentage:.2f}%")
else:
    print("No marks entered.")