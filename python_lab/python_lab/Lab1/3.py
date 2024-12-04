# Q3: Impedance in Parallel
import math
Z1 = complex(input("Enter first impedance (e.g., 3+4j): "))
Z2 = complex(input("Enter second impedance (e.g., 1-2j): "))
Zeq = (Z1 * Z2) / (Z1 + Z2)
print(f"Z1: {Z1}, Z2: {Z2}")
print(f"Real Part: {Zeq.real}, Imaginary Part: {Zeq.imag}")