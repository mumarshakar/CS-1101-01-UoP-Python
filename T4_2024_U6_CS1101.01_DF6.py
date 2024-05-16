"""
Discussion Assignment Unit 6
CS1101.01 

"""

#In the assignment statement, the left-hand side is an object and the right-hand side is a value.

#For example a=5, In this assignment statement, "a" is the object and "5" is the value.

# In case of  lists, Two lists may be equivalent but not sure the reference is identical.

#For example,

list1=[15, 25, 33]

list2=[15, 25, 33]

print(list1 is list2)

# Output =>  False

# In the above statements, the output is false because the list1 and list2 object references were different(identical) but the value was the same(equivalent).

list1=[15, 25, 33]

list2=list1

print(list1 is list2)

# Output  = > True
# In the above statements, the output is true because both the objects reference the same identity.
# The is operator is used to check the reference of the objects, not the values.
# The operator returns true if the reference is the same, otherwise returns false.
# Objects, References, and Aliases:
# The collection of data using variables is called objects.
# References are nothing but a name that specifies the memory location of a particular object.
# The relationship of aliases with the objects and reference is the reference of the object,
# that is both objects having the same reference, then those objects are an alias for each other.
# For example,

list1 = [11, 14, 16, 10, 18, 13]

list2 = list1

# In the above example, list1 and list2 have the same reference,
# so list1 is the alias for list2 as well as list2 is the alias for list1.

def lists(ls):
    list1 = ls
    list2 = list1

print('list1', list1)

print('list2', list2)

# new list

list1 = [11, 14, 16, 10, 18, 13]

print('list1', list1)

print('list2', list2)

lists([101, 102, 103, 104, 105])


