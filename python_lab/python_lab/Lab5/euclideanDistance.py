import math

t = input("Enter the elements of tuple 1 separated by commas: ")
t1 = tuple(map(float, t.split(',')))  # Convert string to tuple of floats

p = input("Enter the elements of tuple 2 separated by commas: ")
p1 = tuple(map(float, p.split(',')))  # Convert string to tuple of floats
45
distance = math.sqrt((p1[0] - t1[0])**2 + (p1[1] - t1[1])**2 + (p1[2] - t1[2])**2)
print(f"The Euclidean distance between the points is: {distance}")
