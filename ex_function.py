# Mathematics functions

# Modulus
x = abs(-5)
print(x)

# Minimum value
y = min(4, 7, -8, 11)
print(y)

# Max value
z = max(45, 56, 12, 6, 9)
print(z)

# Exponential
f = pow(6, 2)
m = pow(8, 1/3)
print(f, m)

# Rounding
l = round(89.0785437)
k = round(0.5)
t = round(1.5)
p = round(10.5)
i = round(39.5)
print(l, k, t, p, i)

# Rounding to a number of digits

d = round(6.784302, 3)
a = round(8.98892, -1)
c = round(45600988.34, -3)
print(f'{d} - rounded to 3 digit after dot, {a} - rounded to ten, {c}-rounded to thousands')

# Functions abs() min() max() pow() could be nested

nested = max(5, 2, abs(-12), 11)
print(f'max value is - {nested}')

# Importing math module and using functions

import math

# looking through the all module functions: math. in console
# rounding to the closest bigger value
import math

big = math.ceil(7.12)
print(f'rounded to the bigger value: {big}')

# rounding to the closest smaller value
small = math.floor(11.59)
print(f'rounded to the smaller value - {small}')

# Factorial calculation
fac = math.factorial(4)
print(f'The Factorial is - {fac}')

# Get rid of numbers after the dot
tr = math.trunc(568.24335)
print(f'Truncated value: {tr}')