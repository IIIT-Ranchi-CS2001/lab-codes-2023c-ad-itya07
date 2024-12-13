def count_characters(input_string):
    char_count = {} 

    for char in input_string:
        if char in char_count:
            char_count[char] += 1  
        else:
            char_count[char] = 1  
    return char_count

p = input("Enter Your String")
result = count_characters(p)
print(result)
