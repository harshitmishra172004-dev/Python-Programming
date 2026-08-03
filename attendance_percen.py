#To calculate attendence percentage of present employees , using a loop with 'continue'to skip absent-marked records.
total_employees = int(input("Enter total number of employees: "))
present = 0

for i in range(1, total_employees + 1):
    status = input(f"Employee {i} attendance (P/A): ").upper()

    if status == "A":
        continue   # Skip absent employees

    present += 1

attendance_percentage = (present / total_employees) * 100

print("\nTotal Employees :", total_employees)
print("Present Employees :", present)
print("Attendance Percentage : {:.2f}%".format(attendance_percentage))