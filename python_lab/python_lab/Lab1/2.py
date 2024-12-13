#Q2: Area, Perimeter, and Angles of a Triangle
import math

a, b, c = map(float, input("Enter three sides of the triangle separated by space: ").split())
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
perimeter = a + b + c
print(f"Area: {area}, Perimeter: {perimeter}")


A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
C = 180 - A - B
print(f"Angles: {A}, {B}, {C}")