def my_sort(data_list, key=0):
    # Sort based on the provided key
    if key == 0:
        return sorted(data_list, key=lambda x: x[0])
    elif key == 1:
        return sorted(data_list, key=lambda x: x[1])
    elif key == 2:
        return sorted(data_list, key=lambda x: x[2])
    else:
        raise ValueError("Invalid key. Key must be 0 (name), 1 (ID), or 2 (shopping points).")

customer_data = [('Alice', 101, 50), ('Bob', 102, 40), ('Charlie', 103, 30)]


print(my_sort(customer_data, key=0))
print(my_sort(customer_data, key=1))
print(my_sort(customer_data, key=2))
