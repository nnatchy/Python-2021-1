# a = re , b = im

class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        final = ''
        if self.a == 0 and self.b == 0:
            return '0'
        if self.a > 0 or self.a < 0:
            final += str(self.a)
            if self.b > 0:
                final = final + '+'
        if self.b > 0:
            if self.b == 1:
                final += 'i'
            else:
                final += str(self.b) +'i'
        elif self.b < 0:
            if self.b == -1:
                final += '-i'
            else:
                final += str(self.b) +'i'
        return final
    
    def __add__(self,rhs):
        real = self.a + rhs.a
        image = self.b + rhs.b
        return Complex(real,image)
    
    def __mul__(self,rhs):
        real = (self.a * rhs.a) - (self.b*rhs.b)
        image = (self.a*rhs.b) + (self.b*rhs.a)
        return Complex(real,image)
    
    def __truediv__(self,rhs):
        real = ((self.a*rhs.a) + (self.b*rhs.b))/(rhs.a**2+rhs.b**2)
        image = ((-self.a*rhs.b) + (self.b*rhs.a))/(rhs.a**2+rhs.b**2)
        return Complex(real,image)

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)