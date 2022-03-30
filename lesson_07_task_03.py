import copy
import random


class Alveole:

    @property
    def id(self):
        return self._id

    def __init__(self):
        self._id = int(random.random() * 10000)


class Cell:

    def __init__(self, a_alveole_amnt=1, a_row_len=3):
        self.row_len = a_row_len
        self._alveoles = []
        for i in range(0, a_alveole_amnt):
            alv = Alveole()
            self._alveoles.append(alv)

    def make_order(self, new_row_len):
        self.row_len = new_row_len

    @property
    def alveole_count(self):
        return len(self._alveoles)

    def get_alveole(self, index):
        return self._alveoles[index]

    def get_str(self):
        s = ""
        for i in range(0, len(self._alveoles)):
            s += "*" + ("\t" if (i + 1) % self.row_len > 0 or i == len(self._alveoles) - 1 else "\n")
        return s + "\n"

    def __str__(self):
        return self.get_str()

    def __add__(self, comp):
        res = Cell(0, self.row_len)
        for x in self._alveoles:
            x2 = copy.copy(x)
            res._alveoles.append(x2)
        for a in comp._alveoles:
            a2 = copy.copy(a)
            res._alveoles.append(a2)
        return res

    def __sub__(self, comp):
        res = Cell(0, self.row_len)
        amnt_new = len(self._alveoles) - len(comp._alveoles)
        if amnt_new <= 0:
            raise Exception("result cell is empty")
        for i in range(0, len(self._alveoles)):
            if i < amnt_new:
                res._alveoles.append(self._alveoles[i])
            else:
                break
        return res

    def __mul__(self, comp):
        res = Cell(0, self.row_len)
        amnt_new = len(self._alveoles) * len(comp._alveoles)
        for i in range(0, amnt_new):
            a = Alveole()
            res._alveoles.append(a)
        return res

    def __truediv__(self, comp):
        if len(comp._alveoles) == 0:
            raise Exception("divisor cell is empty")
        amnt_new = int(len(self._alveoles) / len(comp._alveoles))
        if amnt_new <= 0:
            raise Exception("division result cell is empty")
        res = Cell(0, self.row_len)
        for i in range(0, amnt_new):
            a = Alveole()
            res._alveoles.append(a)
        return res


if __name__ == "__main__":
    c = Cell(10, 3)
    s = c.get_str()
    print("c consists of %d alveoles\n%s" % (c.alveole_count, s))

    c.make_order(4)
    s = c.get_str()
    print("c after changing row length\n" + s)

    c2 = Cell(6, 3)
    s = c2.get_str()
    print("c2 is another cell of following structure, %d alveoles\n%s" % (c2.alveole_count, s))

    c3 = c + c2
    print("sum of c and c2\n" + c3.get_str())

    c4 = c - c2
    print("difference of c and c2\n" + c4.get_str())

    c5 = c * c2
    print("product of c and c2 has %d alveoles\n%s" % ( c5.alveole_count , c5.get_str()))

    c6 = c / c2
    print("quotient of c and c2\n" + c6.get_str())

    print("c6 alveole 0 id is %d" % c6.get_alveole(0).id)
