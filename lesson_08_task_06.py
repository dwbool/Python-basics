

class Warehouse(list):

    def append(self,  x):
        super(Warehouse, self).append(x)

    def add_equipment(self, manufact, model, kind, qty, dep):

        if kind.lower()=='printer':
            prn = Printer(manufact, model    )
            wi = WarehouseItem(prn, qty, dep)
            self.append(wi)

        elif kind.lower()=='scanner':
            prn = Scanner(manufact, model    )
            wi = WarehouseItem(prn, qty, dep)
            self.append(wi)

        elif kind.lower().strip() > '':
            oth = OfficeEquipment( )
            oth.manufact = manufact
            oth.model = model
            oth.kind = kind
            wi = WarehouseItem(oth, qty, dep)
            self.append(wi)




class WarehouseItem:

    def __init__(self, aequipment, aqty, adep ):
        super().__init__()
        self.equipment = aequipment
        self.qty=aqty
        self.dep=adep



class OfficeEquipment:

    def __init__(self):
        self.model=""
        self.kind= "unknown"
        self.manufact = ""

    def __str__(self):
        s = "%s %s %s" % (self.manufact,self.model,self.kind)
        return s


class Printer(OfficeEquipment):

    def __init__(self, amanufact, amodel):
        super().__init__()
        self.model=amodel
        self.manufact = amanufact
        self.kind="Printer"


class Scanner(OfficeEquipment):

    def __init__(self, amanufact, amodel):
        super().__init__()
        self.model=amodel
        self.manufact = amanufact
        self.kind="Scanner"




def find_model(lst, aman, amdl):
    for i in range(0,len(lst)):
        if lst[i].model==amdl and lst[i].manufact==aman :
            return i
    return -1

def find_item(lst, aman, amdl, dep):
    for i in range(0,len(lst)):
        if lst[i].equipment.model==amdl and lst[i].equipment.manufact==aman and lst[i].dep==dep:
            return i
    return -1


def lst_models(lst:list):
    print("MODELS")
    s = "%s\t%s\t\t%s\t\t%s" % ("id", "model", "manufacturer", "kind" )  # OfficeEquipment(lst[i]).manufact
    print(s)
    for i in range(0,len(lst)):
        s = "%d\t%s\t\t%s\t\t\t\t%s" % (i, lst[i].model,  lst[i].manufact, lst[i].kind )  #OfficeEquipment(lst[i]).manufact
        print(s)

def lst_warehouse(lst:list):
    print("COMPANY EQUIPMENT IN USE")
    s = "%s\t%s\t\t%s\t\t%s\t\t%s\t\t%s" % ("id", "model", "manufacturer", "kind", "department", "quantity")  # OfficeEquipment(lst[i]).manufact
    print(s)
    for i in range(0,len(lst)):
        s = "%d\t%s\t\t\t%s\t\t\t%s\t\t%s\t\t\t%d" % (i, lst[i].equipment.model,  lst[i].equipment.manufact, lst[i].equipment.kind,  lst[i].dep, lst[i].qty)  #OfficeEquipment(lst[i]).manufact
        print(s)


def input_positive_int():
    s = input()
    x = -1
    if s.isnumeric():
        try:
            x = int(s)
            if x < 0:
                x = -1
        except:
            pass
    if x == -1:
        print("value must be positive integer or zero")
    return x




scn = Scanner("Mustek", "Paragon" )
prn = Printer("Canon", "MP-160" )
lmp = OfficeEquipment( )
lmp.model="Light"
lmp.manufact="Deluxe"
lmp.kind = "Lamp"

wh = Warehouse()
models = []
models.append(scn)
models.append(prn)
models.append(lmp)


wi = WarehouseItem(prn, 3,  "Personnel" )
wh.append(wi)
wi2 = WarehouseItem(lmp, 4,  "Marketing" )
wh.append(wi2)
wi3 = WarehouseItem(scn, 5,  "Planning" )
wh.append(wi3)

print("COMPANY EQUIPMENT DATABASE")
lst_models(models)
lst_warehouse(wh)

while 1:
    print("INPUT COMMAND: ml - model list; apm - add printer model; asm - add scanner model; aom - add other model; ai - add item to department; ri - remove item; wl - warehouse list; q - quit")
    s=input().lower().strip()

    if s == 'ml':
        lst_models(models)

    elif s == 'aom':
        print("input equipment kind")
        knd = input().strip()
        if knd == "":
            print("equipment kind cannot be empty")
            continue
        print("input manufacturer")
        sman = input().strip()
        print("input model")
        mdl = input().strip()
        if find_model(models,sman,mdl)==-1:
            aom = OfficeEquipment()
            aom.model= mdl
            aom.manufact = sman
            aom.kind=knd
            models.append(aom)
        else:
            print("already exists")
        lst_models(models)

    elif s == 'apm':
        print("input manufacturer")
        sman = input().strip()
        print("input model")
        mdl = input().strip()
        if find_model(models,sman,mdl)==-1:
            prn = Printer(sman, mdl)
            models.append(prn)
        else:
            print("already exists")
        lst_models(models)

    elif s == 'asm':
        print("input manufacturer")
        sman = input().strip()
        print("input model")
        mdl = input().strip()
        if find_model(models,sman,mdl)==-1:
            prn = Scanner(sman, mdl)
            models.append(prn)
        else:
            print("already exists")
        lst_models(models)

    elif s == 'ai':
        print("input model ID (see through ml command), input empty string to cancel operation")
        id = input_positive_int()
        if id<len(models) and id>-1:
            mdl = models[id]
        if id==-1 :
            print("wrong id")
            continue
        print("chosen: "+models[id].model)
        print("input quantity")
        qty=input_positive_int()
        if qty == -1:
            print("wrong number")
            continue
        print("input department")
        dep = input().strip().upper()
        if dep == "":
            print("department cannot be empty")
            continue
        id = find_item(wh,mdl.manufact,mdl.model,dep)
        if id != -1:
            print("record already exists, adding quantity")
            wh[id].qty += qty
        else:
            wh.add_equipment(mdl.manufact,mdl.model,mdl.kind,qty,dep)
        print("new equipment added: %s %s %d" % (mdl.manufact,mdl.model,qty))
        lst_warehouse(wh)

    elif s == "wl":
        lst_warehouse(wh)

    elif s == "ri":
        print("input COMPANY EQUIPMENT IN USE item id to remove (can see through wl cmmand)")
        id = input_positive_int()
        if id!=-1 and id< len(wh):
            print("input quantity")
            qty= input_positive_int()
            if qty == -1: continue
            print("removing ID = %d ; eduipment = %s" % (id, wh[id].equipment.model))
            if qty == wh[id].qty:
                wh.pop(id)
            elif qty < wh[id].qty:
                wh[id].qty -= qty
            else:
                print("wrong number of items to remove")
                continue
        else:
            print("wrong COMPANY EQUIPMENT IN USE ID")
            continue
        lst_warehouse(wh)

    elif s == "q":
        break

    else:
        print("unknown command: " + s)









