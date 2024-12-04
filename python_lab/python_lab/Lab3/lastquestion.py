# # Get the input string and character from the user
# string_input = input("Enter a string: ")
# char_input = input("Enter a character: ")
# count = 0
# for char in string_input:
#     if char == char_input:
#         count += 1

# print("The character '{}' appears {} times in the string.".format(char_input, count))
# s ='a'
# s.split
# print(s)
# pets = ['Dog', 'Cat', 'Monkey', 'Lion']
# for index, p in enumerate(pets):
#     print(index, p)
# num1 = [1, 2, 3]
# # num2 = num1
# # num1 is num2
# # num1.append({40})
# # print(num1.pop(1))
# # print(num1.append({40}))
# L = [3, 6, 8, 9, 0]
# #  sorted(L)
# print(sorted(L))
# print(L)
# List comprehension to create a list of squares
n=int(input())
square = [x * x for x in range(0, n+1)]
print(square)  # Output: [1, 4, 9, 16]

# Corrected for loop to use enumerate
for i, v in enumerate(square):
    print(i, v)
