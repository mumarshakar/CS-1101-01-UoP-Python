def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1

    return -1


result = find("Pakistan", "a")

print(result)