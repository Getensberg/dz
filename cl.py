import cmath

a = int(input('введите а\n'))
b = int(input('введите b\n'))
c = int(input('введите c\n'))


def sqrtFunc(a,b,c):
    discriminant = (b**2) - (4*a*c)

    root1 = (-b-cmath.sqrt(discriminant))/(2*a)
    root2 = (-b+cmath.sqrt(discriminant))/(2*a)
    return [root1,root2]

print(sqrtFunc(a,b,c))
