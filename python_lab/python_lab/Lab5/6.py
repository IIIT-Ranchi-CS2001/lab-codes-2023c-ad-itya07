# Q6: Count Characters in a String
string = input("Enter a string: ")
char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print("Character Count:", char_count)
