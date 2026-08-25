inv_a = {'apples':10, 'banana':5, 'oranges':7}
inv_b = {'apples':3, 'banana':2, 'grapes':4}
inventory = inv_a.copy()
for item, quantity in inv_b.items():
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
print(inventory)