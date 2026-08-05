#Write a Python program to manage employee records using a list. Remove duplicate names, 
#sort the list alphabetically, and search for an employee using append(), sort(), in, and set().
# Employee Record Management

employees = []

n = int(input("Enter the number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    employees.append(name)

# Remove duplicate names
employees = list(set(employees))

# Sort the list alphabetically
employees.sort()

print("\nEmployee List:")
print(employees)

# Search for an employee
search = input("\nEnter employee name to search: ")

if search in employees:
    print(search, "is found in the employee list.")
else:
    print(search, "is not found in the employee list.")