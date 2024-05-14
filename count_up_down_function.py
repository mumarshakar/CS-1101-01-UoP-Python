# Create a function to count
# Get Input from user 
# If entered number is 0 then print "blast off"
# if number is positive then count downwards
# If number is negative then count upwards 

x = int(input("Enter Number: "))  # Getting input from the user as integer
def count(n):   # function declaration for count
    if n > 0:       # Condition if the number is greater than 0
        print(n)    # printing the value of n which entered by user
        count(n-1)
    elif n < 0:
        print(n)
        count(n+1)
    else:
        print("Blast Off")

count(x)