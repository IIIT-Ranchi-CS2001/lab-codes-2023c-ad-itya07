# Q1: Custom zip function with strict mode
def my_zip(*iterables, strct=True):
    min_len = min(map(len, iterables)) if strct else None
    return [tuple(iterable[i] for iterable in iterables) for i in range(min_len or max(map(len, iterables)))]

# Testing
customer_names = ["Alice", "Bob", "Charlie"]
customer_ids = ["C001", "C002", "C003"]
shopping_points = [200, 150, 300]
print("Strict Mode:", my_zip(customer_names, customer_ids, shopping_points, strct=True))
print("Non-Strict Mode:", my_zip(customer_names, customer_ids, shopping_points, strct=False))

# Q2: Custom sort function for tuples
def my_sort(data, key=0):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# Testing
data = [("Alice", "C001", 200), ("Bob", "C002", 150), ("Charlie", "C003", 300)]
print("Sorted by Name:", my_sort(data, key=0))
print("Sorted by ID:", my_sort(data, key=1))
print("Sorted by Shopping Points:", my_sort(data, key=2))

# Q3: Custom max function
def my_max(*args):
    max_val = args[0]
    for val in args:
        if val > max_val:
            max_val = val
    return max_val

# Testing
print("Max in list:", my_max(*[5, 10, 15]))
print("Max in tuple:", my_max(*tuple([2, 3, 1])))
print("Max in set:", my_max(*{9, 4, 7}))

# Q4: Using map, lambda, and filter
input_string = input("Enter a comma-separated string: ")
# Extract uppercase letters
uppercase = list(map(lambda s: s.upper(), filter(lambda x: x.isalpha(), input_string.split(','))))
print("Uppercase:", uppercase)

# Square of digits
digit_squares = list(map(lambda x: int(x)**2, filter(lambda x: x.isdigit(), input_string.split(','))))
print("Digit Squares:", digit_squares)

# Alphanumeric characters
alphanumeric = list(filter(lambda x: x.isalnum(), input_string.split(',')))
print("Alphanumeric Characters:", alphanumeric)
