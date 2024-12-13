def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    # Check if all lists are of equal length when strct is True
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return list(zip(customer_names, customer_ids, shopping_points))
        else:
            raise ValueError("All lists must be of equal length when 'strct' is True")
    else:
        min_len = min(len(customer_names), len(customer_ids), len(shopping_points))
        return list(zip(customer_names[:min_len], customer_ids[:min_len], shopping_points[:min_len]))
customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [101, 102, 103]
shopping_points = [50, 40, 30]

# Strict mode (True)
print(my_zip(customer_names, customer_ids, shopping_points, strct=True))

# Non-strict mode (False)
print(my_zip(customer_names, customer_ids[:2], shopping_points, strct=False))
