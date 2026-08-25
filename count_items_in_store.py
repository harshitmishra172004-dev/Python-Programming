cart =['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
count = {}
for item in cart: 
   if item in count:
      count[item] += 1
   else:
      count[item] = 1

print(count)      