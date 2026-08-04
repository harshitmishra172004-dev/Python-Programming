# Built-in List Method Use Extend In list . Take User Input 
list1 = []
list2 = []
n1 = int(input("Enter the number of elements in the first list: "))
for i in range(n1):
    list1.append(int(input(f"Enter element {i+1} of the first list: ")))
n2 = int(input("Enter the number of elements in the second list: "))
for i in range(n2):
    list2.append(int(input(f"Enter element {i+1} of the second list: ")))
list1.extend(list2)
print(list1)