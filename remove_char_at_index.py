#WAP to remove a character at a index i from a string.Without using inbuilt functions,Without Functions
#Input: "Hello Harshit", 5
string = "Hello Harshit"
index = int(input("Enter the index of the character to remove: "))
new_string = ""
for i in range(len(string)):
    if i != index:
        new_string += string[i]
print(new_string)