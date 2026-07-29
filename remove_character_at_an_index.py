name = "Harshit Mishra"
index = (int(input("Enter the index of the character you want to remove: ")))

if index < 0 or index >= len(name):
    print("Invalid index. Please enter a valid index.")

else:
    new_name = name[:index] + name[index + 1:]
    print("New string after removing character at index", index, ":", new_name)