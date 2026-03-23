cnumallowed = 0
a = float(input('Input the multilier of the quadratic term (a): '))
b = float(input('Input the multilier of the first-degree term (b): '))
c = float(input('Input the multilier of the constant term (c): '))
cnumallowed = str(input('Would you like to turn on complex numbers? (Y/N) '))
if cnumallowed in ['Y', 'yes', 'Yes', 'y']:
    cnumallowed = 1
    import cmath
else:
    import math
if cnumallowed == 0:
    solution1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    solution2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
else:
    solution1 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
    solution2 = (-b-cmath.sqrt(b**2-4*a*c))/(2*a)
print('The solutions are: ' + str(solution1) + ' and ' + str(solution2) + '.')