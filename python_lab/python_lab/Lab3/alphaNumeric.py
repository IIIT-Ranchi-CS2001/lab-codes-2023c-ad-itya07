def check_alphanumeric(s):
    for char in s:
        if not char.isalnum():
            return False
    return True


string = input("Enter a string: ")
if check_alphanumeric(string):
    print(True)
else:
    print(False)