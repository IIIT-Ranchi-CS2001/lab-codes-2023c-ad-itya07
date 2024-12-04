# Q7: List of Tuples with and without zip
customer_names = input("Enter customer names separated by commas: ").split(',')
customer_ids = input("Enter customer IDs separated by commas: ").split(',')
shopping_points = list(map(int, input("Enter shopping points separated by commas: ").split(',')))

# Using zip
customers_with_zip = list(zip(customer_names, customer_ids, shopping_points))
print("Using zip:", customers_with_zip)

# Without using zip
customers_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
print("Without zip:", customers_manual)