num = int(input("Enter a number: "))
sum_of_digits = 0
original_num = num
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10
print("Number:", original_num)
print("Sum of digits:", sum_of_digits)