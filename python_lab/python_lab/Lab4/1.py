# Q1: Count the number of palindrome words in a sentence
sentence = input("Enter a sentence: ")
palindrome_count = sum(1 for word in sentence.split() if word.lower() == word[::-1].lower())
print(f"Number of palindrome words: {palindrome_count}")