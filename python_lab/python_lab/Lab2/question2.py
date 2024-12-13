
S = "Ba Ba Black Sheep"


length_of_S = len(S)
print(f"Length of the string S: {length_of_S}")


first_occurrence_e = S.find('e')
if first_occurrence_e != -1:
    print(f"The first occurrence of 'e': {first_occurrence_e}")
else:
    print("The letter 'e' is not found in the string.")


total_occurrences_a = S.count('a')
print(f"The total number of occurrences of 'a': {total_occurrences_a}")


new_string = S.replace("Ba", "Ta", 2)  
print(f"Generated string: {new_string}")
