# Unit Number 6 Practice coding here 
# What is a list? What is difference between list and string
# Like a string, a list is a sequence of values. In a string, the values are characters; in a list,
# they can be any type. The values in a list are called elements or sometimes items.
# THe Best Way To Create a list is the use of square brackets (In Punjabi Wadi Brackets)
umar = ["Muhammad", "Umar", "Shakar", 38, "Years"]
# What is nested list?
# A list within another list is called nested list.
print(f"Output Of List 'Umar' : ", umar)
# To access items or elements of list we use indeces
print(umar[0:2])

#Empty List is a list which has not elemnet or item in it. It just contains two square brackets only []
cheeses = ["Cheddar", "Edam", "Gouda"]
numbers = [42, 123]
empty = []

print(cheeses, numbers, empty)



print("==================Lists Are Mutable===================")

# List are mutable while strings are not mutable
print(cheeses[0])
cheeses[0] = "Umar"

print(cheeses)
print(cheeses[0])
print(cheeses[0:2])
# in operator works in lists as in strings
print("Edam" in cheeses)    # Returns True
print("Brie" in cheeses)    # Returns False

print("=================For loop in lists====================")

for cheese in cheeses:
    print(cheese)
print("=================Traversing a list====================")

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2


# Counting list indices

a = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[2][0:2])