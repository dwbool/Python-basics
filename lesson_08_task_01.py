
class DateRec:

    def __init__(self, asdate):
        if not DateRec.is_valid(asdate):
            raise Exception("")
        self._sdate =asdate

    def __str__(self):
        y, m, d = self.get_ymd()
        s = "%d-%d-%d" % (d ,m ,y)
        return s


    def get_ymd(self):
        lst =self._sdate.split('-')
        d=int(lst[ 0])
        m=int(lst [ 1])
        y=int(lst [ 2])
        return y,m,d

    @staticmethod
    def get_ymd_side( s):
        lst = s.split('-')
        d = int(lst[0])
        m = int(lst[1])
        y = int(lst[2])
        return y, m, d

    @classmethod
    def get_ymd_rec(cls, d,m,y):
        s="%d-%d- % d" % (d,m,y)
        if not DateRec.is_valid(s):
            raise Exception("invalid date")
        rec = cls(s)
        return rec


    @staticmethod
    def leap( y ):
        if y % 4 == 0 and (y % 100 > 0 or y % 1000 ==0):
            return 1
        else :
            return 0

    @staticmethod
    def is_valid( sdt):
        y,m,d= DateRec.get_ymd_side( sdt)
        if y<0:
            return 0
        if m<1 or m> 12 :
            return 0
        if d<1:
            return 0
        if m in (1,3,5,7,8, 10 ,12) :
            if d>31:
                return 0
        elif m in (4,6,9,11):
            if d>30:
                return 0
        elif m==2:
            if DateRec.leap(y) and d>29:
                return 0
            elif d>28:
                return 0
        else:
            return 0
        return 1



y=1996 # 2000  #2020  #1992
lp=DateRec.leap(y)
print("%d is leap = %d"%(y,lp))

drec = DateRec("1-2-2020")
print("constructor created record: y m d = " + str(drec.get_ymd()))

obj = DateRec.get_ymd_rec( 12,12,2023)
print("class method created object: %s" % str(obj))

try:
    d = 12
    m = 13
    y = 2023
    print("trying to make erroneous date %02d-%02d-%04d" % (d, m, y))
    obj = DateRec.get_ymd_rec( 12,13,2023)
    print("crated object: %s" % str(obj))
except Exception as e:
    print("faced error: %s" % str(e))

