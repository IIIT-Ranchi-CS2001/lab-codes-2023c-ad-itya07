def table(num, limit):
    for i in range(1, limit + 1):
        print(f"{num} x {i} = {num * i}")


num = int(input("Enter the number:"))
limit =int(input("Enter the limit:"))
table(num, limit)