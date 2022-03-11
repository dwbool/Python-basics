
class Road:

    def __init__(self, awidth, alength, adepth, adensity=25):

        self._width =awidth
        self._length =alength
        self._depth =adepth
        self._density =adensity


    def calc_mass(self):

        mass = self._width * self._length * self._depth * self._density
        return mass


    def get_width(self):
        return self._width


    def get_length(self):
        return self._length


    def get_depth(self):
        return self._depth



if __name__ == "__main__":

    road = Road(10, 1000, 1)
    m = road.calc_mass()
    print("road of length=%.0f m , width=%.2f m and thickness=%.2f cm has mass of %0.0f kg" %
    (road.get_length(), road.get_width(), road.get_depth(), m))
