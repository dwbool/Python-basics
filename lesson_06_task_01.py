import time


class TrafficLight:


    def __init__(self):

        self._st = 0
        self._t0 = 0
        self.__color = ""
        self.r_time = 7
        self.y_time = 3
        self.g_time = 5


    def running(self):

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



tl = TrafficLight()
# the traffic light sits horizontally in our picture: @ - lamp is on, O - lamp is off
print("R\tY\tG")

while 1:
    tl.running()
    print("\b\b\b\b\b\b\b\b\b" + str(tl.pic()) + "\t\t" + tl.get_color(), end='')
    time.sleep(0.1)
