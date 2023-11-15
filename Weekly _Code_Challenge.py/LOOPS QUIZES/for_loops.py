for apples in [10,20,30,40,50]:
    print (apples)
    print ("I love Apples!")

#Write a for loop that displays Hello, plus each name in the list. 
cities= ["Nairobi", "Nakuru", "Nanyuki", "Naivasha", "Nyeri"]
for city in cities:
    print(city +  ",the best city") 

# Write a program that prints the numbers from 1 to 100, noting the multiples of 3 and 5.
for num in range(1, 101):
    # Check if the number is a multiple of both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num}: Multiple of 3 and 5")
    # Check if the number is a multiple of 3
    elif num % 3 == 0:
        print(f"{num}: Multiple of 3")
    # Check if the number is a multiple of 5
    elif num % 5 == 0:
        print(f"{num}: Multiple of 5")
    # If the number is neither a multiple of 3 nor 5, just print the number
    else:
        print(num)


