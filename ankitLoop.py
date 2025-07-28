fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print()

for i in range(5):
    print(i)


# java and cpp
# for(int i=0; i<n; i++){
# }
# Function to print full pyramid pattern
def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()
   
full_pyramid(2)
