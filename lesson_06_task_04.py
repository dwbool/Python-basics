import math


class Car:

    def __init__(self, aspeed, acolor, aname, ais_police):

        self._speed = aspeed
        self.color = acolor
        self.name = aname
        self.is_police = ais_police
        self.angle = 0

    def go(self, acceleration=1.0):

        if self._speed < 120:
            self._speed += acceleration
        if self._speed > 120:
            self._speed = 120

    def stop(self, deceleration=1.0):

        if self._speed > 0:
            self._speed -= deceleration
        if self._speed < 0:
            self._speed = 0

    def turn(self, direction):

        self.angle += direction
        pref = "police " if self.is_police else ""
        print(pref + self.name + " turned to absolute angle %.2f " % math.degrees(self.angle))

    def show_speed(self):
        pref = "police " if self.is_police else ""
        print(pref + self.name + " car's speed is  %.0f km/h" % float(self._speed))
        return self._speed


class TownCar(Car):

    def show_speed(self):
        pref = "town "
        pref += "police " if self.is_police else ""
        if self._speed > 60:
            print(pref + self.name + " town car is rushing too fast at the speed of %.0f km/h" % (self._speed))
        else:

            print(pref + self.name + " car's speed is  %.0f km/h" % float(self._speed))
        return self._speed


class WorkCar(Car):

    def show_speed(self):
        pref = "work "
        pref += "police " if self.is_police else ""
        if self._speed > 60:
            print(pref + self.name + " service car is rushing too fast at the speed of %.0f km/h" % (self._speed))
        else:
            super().show_speed()

        return self._speed

class SportCar(Car):

    def show_speed(self):
        pref = "sport "
        pref += "police " if self.is_police else ""
        print(pref + self.name + " car's speed is  %.0f km/h" % float(self._speed))
        return self._speed


cars = []

cc = Car(30, "blue", "Hyundai", False)
tc = TownCar(20, "red", "Mazda", False)
wc = WorkCar(49, "turquoise", "Subaru", True)
sc = SportCar(120, "purple", "Porshe", False)

cars.append(cc)
cars.append(tc)
cars.append(wc)
cars.append(sc)

print("input 'G' to make all the cars go faster or 'S' to slow them down, 'L' - turn left, 'R' - turn right, 'D' - direction print, 'Q' to quit, any string to refresh the data")

while 1:

    for c in cars:
        c.show_speed()

    cmd = input().lower()

    if cmd == 'g':
        print("going faster >>")
        for c in cars:
            c.go(10)

    elif cmd == 's':
        print("slowing down <<")
        for c in cars:
            c.stop(10)

    elif cmd == 'l':
        print("left")
        for c in cars:
            c.turn(math.radians(1))

    elif cmd == 'r':
        print("left")
        for c in cars:
            c.turn(math.radians(-1))

    elif cmd == 'd':
        print("left")
        for c in cars:
            print("%s direction absolute angle is %.2f degrees" % (c.name, math.degrees(c.angle)) )

    elif cmd == 'q':
        print("quitting")
        break
