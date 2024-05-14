"""
Write program to display your name and perform following operations on it: 
(I) Display n characters from left. (Accept n as input from the user)
(II) Count the number of vowels. 
(III) Reverse it. 
The code and its output must be explained technically.
 The explanation can be provided before or after the code, 
 or in the form of comments within the code. The descriptive part of
 your response must be at least 200 words. 
"""

def get_name():
  """Prompts the user to enter their name and returns it."""
  name = input("Enter your name: ")
  return name
# nm = get_name()
# print(nm)


def characters(nm, n):
  """Displays the first n characters of the name."""
  print(f"First {n} characters: {nm[:n]}")

# characters("UMARSHAKAR", 3)

def count_vowels(name):
  """Counts the number of vowels in the name."""
  vowels = 'aeiouAEIOU'
  count = 0
  for char in name:
    if char in vowels:
      count += 1
  print(f"Number of vowels: {count}")

# count_vowels("MUHAMMAD")

def reverse_name(name):
  """Reverses the name and displays it."""
  print(f"Reversed name: {name[::-1]}")
#reverse_name("PAKISTAN")



def main():
  """Gets the name from the user and performs the operations."""
  name = get_name()
  n = int(input("Enter the number of characters to display (from left): "))
  characters(name, n)
  count_vowels(name)
  reverse_name(name)
main()