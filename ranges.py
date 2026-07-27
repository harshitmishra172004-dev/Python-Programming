import sys

sum = 0
for arg in sys.argv[1:]:
    sum+= int(arg)
    
print(f"The sum of the numbers is: {sum}")