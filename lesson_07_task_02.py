from abc import ABC, abstractmethod

class Garment(ABC):

    def __init__(self, aVolumeSize, aHeight):
        self._H = aHeight
        self._V = aVolumeSize

    @property
    def v(self):
        return self._V

    @property
    def h(self):
        return self._H

    @property
    @abstractmethod    
    def fabric_amount(self) -> object:
        pass


class Coat(Garment):
    @property
    def fabric_amount(self):
        return self._V / 6.5 + 0.5


class Suit(Garment):
    @property
    def fabric_amount(self):
        return 2 * self._H + 0.3


def get_total(garments):
    total = sum([g.fabric_amount for g in garments])
    return total


if __name__ == "__main__":
    coat1 = Coat(44, 1.70)
    suit1 = Suit(40, 1.60)
    garments = []
    garments.append(coat1)
    garments.append(suit1)

    total = get_total(garments)
    print("Coat: size %.0f , height %.2f " % (coat1.v, coat1.h))
    print("Suit: size %.0f , height %.2f " % (suit1.v, suit1.h))

    print("Fabric amount to sew a coat is %.2f m^2, a suit requires %.2f m^2" % (coat1.fabric_amount, suit1.fabric_amount))

    print("Total Fabric amount to sew the garments is %.2f m^2" % total)
