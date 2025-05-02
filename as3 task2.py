import math

num = float(input("Enter a number: "))

if num > 0:
    square_root = math.sqrt(num)
    log = math.log(num)

else:
    square_root = "Undefined (cannot take square root of negative number)"
    log = "Undefined (logarithm only defined for positive numbers)"

sine = math.sin(num)

print(f"Square root: {square_root}")
print(f"Logarithm: {log}")
print(f"Sine: {sine}")