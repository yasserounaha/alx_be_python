number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
