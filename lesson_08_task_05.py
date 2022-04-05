

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

        elif kind.lower()=='other':
            oth = OfficeEquipment(manufact, model    )
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
        s = "%d\t%s\t\t%s\t\t\t\t%s\t\t%s\t\t\t\t%d" % (i, lst[i].equipment.model,  lst[i].equipment.manufact, lst[i].equipment.kind,  lst[i].dep, lst[i].qty)  #OfficeEquipment(lst[i]).manufact
        print(s)




scn = Scanner("Mustek", "Paragon" )
prn = Printer("Canon", "MP-160" )

wh = Warehouse()
models = []
models.append(scn)
models.append(prn)


wi = WarehouseItem(prn, 3,  "Personnel" )
wh.append(wi)

lst_models(models)
lst_warehouse(wh)

while 1:
    print("ml - model list; apm - add printer model; asm - add scanner model; ai - add item; ri - remove item; wl - warehouse list; q - quit")
    s=input().lower().strip()

    if s=='ml':
        lst_models(models)

    elif s=='apm':
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

    elif s=='asm':
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

    elif s=='ai':
        print("input model ID (see through ml command), input empty string to cancel operation")
        sid = input().strip()
        if sid=="": continue
        id = -1
        mdl = None
        try:
            id = int(sid)
            mdl = models[id]
        except:
            id=-1
            mdl=None
        if id==-1 :
            print("wrong id")
            continue
        print("chosen: "+models[id].model)
        print("input quantity")
        qty=0
        try:
            qty = int(input())
        except:
            print("wrong number")
            continue
        print("input department")
        dep = input().strip().upper()
        id = find_item(wh,mdl.manufact,mdl.model,dep)
        if id!=-1:
            print("record already exists, adding quantity")
            wh[id].qty += qty
        else:
            wi = WarehouseItem(mdl,qty,dep)
            wh.append(wi)
        print("new equipment added: %s %s %d" % (mdl.manufact,mdl.model,qty))
        lst_warehouse(wh)

    elif s=="wl":
        lst_warehouse(wh)

    elif s=="ri":
        print("input COMPANY EQUIPMENT IN USE item id to remove (can see through wl cmmand)")
        sid = input().strip()
        if sid == "": continue
        id = -1
        mdl = None
        try:
            id = int(sid)
        except:
            id = -1
        if id!=-1 and id< len(wh):
            print("input quantity")
            qty=0
            try:
                qty = int(input())
            except:
                print("wrong number")
                continue

            print("removing ID = %d ; eduipment = %s" % (id, wh[id].equipment.model))
            if qty== wh[id].qty:
                wh.pop(id)
            elif qty<wh[id].qty:
                wh[id].qty-=qty
            else:
                print("wrong number of items to remove")
                continue
        else:
            print("wrong ID")
        lst_warehouse(wh)

    elif s == "q":
        break









