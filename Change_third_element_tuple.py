# WAP to change the third element of a tuple by converting it into a list and then back to a tuple.
# Original tuple
t = (10, 20, 30, 40, 50)

print("Original Tuple:", t)

# Convert tuple into list
l = list(t)

# Change the third element
l[2] = 100

# Convert list back into tuple
t = tuple(l)

print("New Tuple:", t)