# common print usage
print(abs(-6.32) + 12, 8, 3, 'string_data')

# sep parameter
a = 12
b = 5.67
c = -2.31
print(a, b, c, sep = ' | ')

# parameter end, end = '\n' by default
print('Printing everything', end=' ')
print('in one line.')

# Printing 'Координаты точки: x=4.87; y=-7.21'
x = 4.87
y = -7.21
print('Координаты точки: x =', x,'; y =', y, sep="")
print (f'Координаты точки: x = {x}; y = {y}')

# Function input()
a = int(input('Please type in the argument a:'))
print(a, type(a))

# Rectangle perimeter calculation
# a = float(input('What is the long side of rectangle in cm:'))
# b = float(input('What is the short side of rectangle in cm:'))
a, b = map(float, input('What is the size of rectangle sides:').split())
perimeter = 2 * (a + b)
print(f'Perimeter of the rectangle is {perimeter}')