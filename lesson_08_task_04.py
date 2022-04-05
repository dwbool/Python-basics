

class Warehouse(list):

    def append(self,  x):
        super(Warehouse, self).append(x)

class OfficeEquipment:


    def __init__(self):
        self.model=""
        self.sort= "unknown"
        self.manufact = ""

    def __str__(self):
        s = "%s %s %s" % (self.manufact,self.model,self.sort)
        return s


class Printer(OfficeEquipment):

    def __init__(self, amanufact, amodel):
        super().__init__()
        self.model=amodel
        self.manufact = amanufact
        self.sort="Printer"


class Scanner(OfficeEquipment):

    def __init__(self, amanufact, amodel):
        super().__init__()
        self.model=amodel
        self.manufact = amanufact
        self.sort="Scanner"


scn = Scanner("Mustek", "Paragon" )
prn = Printer("Canon", "MP-160" )

wh = Warehouse()
wh.append(scn)
wh.append(prn)

print(wh)

for x in wh:
    print(x)

