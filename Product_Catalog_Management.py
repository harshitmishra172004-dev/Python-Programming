#Write a Python program to manage a product catalog using tuples. Search for a product by its ID, find the costliest product, 
#and update its price by recreating the tuple using tuple indexing, max(), and tuple recreation
#Product Catalog Management

# Product Catalog Management

products = (
    (101, "Laptop", 55000),
    (102, "Mobile", 25000),
    (103, "Headphones", 3000),
    (104, "Smart Watch", 7000)
)

# Search product by ID
pid = int(input("Enter Product ID to search: "))

found = False
for product in products:
    if product[0] == pid:
        print("Product Found:")
        print("ID:", product[0])
        print("Name:", product[1])
        print("Price:", product[2])
        found = True
        break

if not found:
    print("Product not found.")

# Find the costliest product
costliest = max(products, key=lambda x: x[2])
print("\nCostliest Product:", costliest)

# Update price by recreating the tuple
update_id = int(input("\nEnter Product ID to update price: "))
new_price = float(input("Enter new price: "))

updated_products = ()

for product in products:
    if product[0] == update_id:
        updated_products += ((product[0], product[1], new_price),)
    else:
        updated_products += (product,)

print("\nUpdated Product Catalog:")
for product in updated_products:
    print(product)