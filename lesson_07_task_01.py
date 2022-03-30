import copy


class Matrix:

    def __init__(self, *argv):

        self._rows = []
        self._col_count = len(argv[0])
        for i in range(0, len(argv)):
            if len(argv[i]) != self._col_count:
                raise Exception("different row lengths in matrix")
            row = []
            for k in range(0, len(argv[i])):
                val = float(argv[i][k])
                row.append(val)
            self._rows.append(row)

    @property
    def col_count(self):
        return self._col_count

    @property
    def row_count(self):
        return len(self._rows)

    def cell(self, icol, irow):
        return self._rows[irow][icol]

    def __str__(self):
        s = ""
        for i in range(0, self.row_count):
            for k in range(0, self.col_count):
                s += "%.2f" % self._rows[i][k] + ("\t" if k < len(self._rows[i]) - 1 else "\n")
        return s

    def __add__(self, g):
        if g.row_count != self.row_count:
            raise Exception("different row count in matrices")
        if g.col_count != self.col_count:
            raise Exception("different column count in matrices")
        res = copy.deepcopy(self)
        for i in range(0, self.row_count):
            for k in range(0, self.col_count):
                res._rows[i][k] += g._rows[i][k]
                # g.cell(k,i)
        return res

if __name__ == "__main__":
    print("matrices summation")
    m = Matrix([1, 1, 4], [2, 3.87, 5], [73, 8, 10])
    g = Matrix([2, 3, 4], [2, 9.16, 5], [73, 8, 10])
    a = m + g
    print(str(m) + "\t\t+ ")
    print(str(g) + "\t\t= ")
    print(str(a))


