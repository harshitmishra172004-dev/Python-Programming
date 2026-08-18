# Create a dictionary of multiple employees containing name, date of joining ,and salary. Take User Input for the same and 
# print the dictionary.
employees = {}
while True:
    employee_id = input("Enter employee ID : ")
    if employee_id == 'none':
        break
    employees[employee_id] = {}
    employees[employee_id]["name"] = input("Enter employee name: ")
    employees[employee_id]["date_of_joining"] = input("Enter date of joining: ")
    employees[employee_id]["salary"] = float(input("Enter salary: "))
print("Employee Dictionary:", employees)
