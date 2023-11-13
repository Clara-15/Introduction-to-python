# Accept user input to create two sets of integers
set1 = set(map(int, input("Enter integers for set 1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter integers for set 2 separated by spaces: ").split()))

# Find elements that are common in both sets
common_elements = set1.intersection(set2)
print("Common elements in the sets:", common_elements)
