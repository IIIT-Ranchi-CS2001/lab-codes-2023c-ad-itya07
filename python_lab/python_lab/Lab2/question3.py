
def is_palindrome(string):
    
    clean_string = string.replace(" ", "").lower()
    return clean_string == clean_string[::-1]
def main():

    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print(f"'{input_string}' is a palindrome.")
    else:
        print(f"'{input_string}' is not a palindrome.")


if __name__ == "__main__":
    main()
