import time

ST_ERROR = 100

class TrafficLight:


    def __init__(self):

        self._st = 0 # state, bits are lamps on
        self._t0 = 0 # time initial value
        self.__color = "" # color
        self.r_time = 7 # red time
        self.y_time = 3 # yellow time
        self.g_time = 5 # green time



    def running(self):
        st_prev=self._st
        if self._st == 0:
            self._t0 = time.perf_counter()
            self._st = 1
        elif self._st == 1:
            self.__color = "R"
            if time.perf_counter() - self._t0 > self.r_time:
                self._st = 2
                self._t0 = time.perf_counter()
        elif self._st == 2:
            self.__color = "Y"
            if time.perf_counter() - self._t0 > self.y_time:
                self._st = 4
                self._t0 = time.perf_counter()
        elif self._st == 4:
            self.__color = "G"
            if time.perf_counter() - self._t0 > self.g_time:
                self._st = 1
                self._t0 = time.perf_counter()
        if not self.switch_allowed(st_prev, self._st):
            print("Error: traffic light switched from state %d to wrong state %d " % (int(st_prev), int(self._st)))
            self._st = ST_ERROR


    def pic(self):

        pc = ""
        for i in range(0, 3):
            x = 1 << i
            if (self._st & x) > 0:
                pc += "@\t"
            else:
                pc += "O\t"
        return pc


    def get_color(self):

        return self.__color


    def switch_allowed(self, st_from, st_to ):
        if st_from==st_to:
            return 1
        elif st_from==0 and st_to==1:
            return 1
        elif st_from==1 and st_to==2:
            return 1
        elif st_from==2 and st_to==4:
            return 1
        elif st_from==4 and st_to==1:
            return 1
        elif st_to==0:
            return 1
        else:
            return 0




tl = TrafficLight()
# the traffic light sits horizontally in our picture: @ - lamp is on, O - lamp is off
print("R\tY\tG")

while 1:
    tl.running()
    print("\b\b\b\b\b\b\b\b\b" + str(tl.pic()) + "\t\t" + tl.get_color(), end='')
    time.sleep(0.1)
    if tl._st==ST_ERROR:
        break
