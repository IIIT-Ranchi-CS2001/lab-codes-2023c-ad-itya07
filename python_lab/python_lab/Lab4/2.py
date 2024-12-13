# Q2: Mean, Median, and Mode without specific modules
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Mean
mean = sum(numbers) / len(numbers)

# Median
numbers.sort()
mid = len(numbers) // 2
median = (numbers[mid] + numbers[~mid]) / 2  # Handles both even and odd cases

# Mode
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
mode = max(frequency, key=frequency.get)

print(f"Mean: {mean}, Median: {median}, Mode: {mode}")