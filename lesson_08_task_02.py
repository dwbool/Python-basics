
class MyZeroDivisionError(ZeroDivisionError):

    def __init__(self, message="Salary is not in (5000, 15000) range"):
        self.message = message
        super().__init__(self.message)



class MyContainer:

    def __init__(self, avalue):

        self.value = avalue


    def __truediv__(self, other):

        if other.value == 0:
            raise MyZeroDivisionError("custom class division by zero")

        return self.value / other.value

    def __str__(self):
        return str(self.value)



x1 = MyContainer(20)
x2 = MyContainer(10)

k = x1 / x2

print("normal division")
print("%s / %s = %s" % (str(x1), str(x2), str(k)))



try:
    print("\ndivision by divisor which may be zero, enter zero to check")
    val = input()
    x2 = MyContainer(float(val))
    k = x1 / x2
except Exception as e:
    print("we encountered error: %s" % str(e))
    k = None

print("%s / %s = %s" % (str(x1), str(x2), str(k)))
