#Write a program that creates a list with the names of your squad mates and prints them out

# Create a list of your squad members

# Use a loop to print each name
# Add an item to the end of your squad members list
# Change an item of your squad members list
# Remove an item on the squad members list
# Specify the item your'e removing



names =["Virgina", "Josphine", "Ann", "Mercy", "Kaycee", "Sharon", "Mary", "Cate"]
names.append("Esther")
names[1] = "Sarah"
names.pop()
names.pop(2)
for name in names:
    print(name)
