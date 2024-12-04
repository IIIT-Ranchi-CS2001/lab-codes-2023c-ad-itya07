# Q1: Euclidean Distance between two points in 3D space
import math

point1 = tuple(map(float, input("Enter coordinates of Point 1 (x y z): ").split()))
point2 = tuple(map(float, input("Enter coordinates of Point 2 (x y z): ").split()))

distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
print(f"Euclidean Distance: {distance}")