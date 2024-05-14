# Create a function to count
# Get Input from user 
# If entered number is 0 then print "blast off"
# if number is positive then count downwards
# If number is negative then count upwards 

x = int(input("Enter Number: "))  # Getting input from the user as integer
def count(n):   # function declaration for count with parameter n
    if n > 0:       # Condition if the number is greater than 0
        print(n)    # printing the value of n which entered by user
        count(n-1)  # Self Calling of function  OR Recursion 
    elif n < 0:         # Second Part of condition  if number entered by user is less than zero
        print(n)        # printing value of n
        count(n+1)      # Self Calling of function or recursion 
    else:               # if none of the above condition is true then else will be executed
        print("Blast Off")  # printing value "Blast Off"

count(x)        # Function Call with argument x 