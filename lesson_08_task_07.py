
class ComplexNum:

    def __init__(self, are, aim):
        self.re = are
        self.im = aim

    def __add__(self, other):
        res = ComplexNum(self.re + other.re, self.im + other.im)
        return res

    def __mul__(self, other):
        res = ComplexNum(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)
        return res

    def __str__(self):
        return "%.6f%+.6f*j" % (self.re, self.im)


a = ComplexNum(1, -4)
b = ComplexNum(3, 2)
z1 = a + b
z2 = a * b
print("%s + %s = %s" % (str(a), str(b), str(z1)))
print("%s * %s = %s" % (str(a), str(b), str(z2)))

#print((1 - 4j) * (3 + 2j))

while 1:
    print("input first complex operand: RE and IM numbers separated by space")
    x1, y1 = map(float, input().split())
    print(x1,y1)

    print("input first complex operand: RE and IM numbers separated by space")
    x2, y2 = map(float, input().split())
    print(x1,y1)

    a = ComplexNum(x1, y1)
    b = ComplexNum(x2, y2)
    z1 = a + b
    z2 = a * b
    print("%s + %s = %s" % ( str(a), str(b), str(z1)))
    print("%s * %s = %s" % (str(a), str(b), str(z2)))


