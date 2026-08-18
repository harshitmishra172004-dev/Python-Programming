# Write a Python program to maintain a software project's assignment list. Add, insert, remove, and reverse project names using 
# append(), insert(). remove(), and reverse(), then display the updated list.
# Software Project Assignment List

projects = ["Website Development", "Database Design", "Testing"]

print("Original List:", projects)

projects.append("Documentation")

projects.insert(1, "UI Design")

projects.remove("Testing")

projects.reverse()

# Display updated list
print("Updated List:", projects)