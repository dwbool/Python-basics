class Worker:

    def __init__(self, aname, asurname, aposition, awage=0, abonus=0):
        self.name = aname
        self.surname = asurname
        self.position = aposition
        self._income = {"wage": awage, "bonus": abonus}

    def set_wage(self, awage):
        self._income["wage"] = awage

    def set_bonus(self, abonus):
        self._income["bonus"] = abonus


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return float(self._income["wage"] + self._income["bonus"])


staff = []

if __name__ == "__main__":

    person1 = Position("Anabelle", "De La Torre", "chef", 10000, 200)
    person2 = Position("Aquilla", "Banaay", "waitress", 5000, 60)
    person3 = Position("Nellie", "Gumilid", "janitor", 3000, 30)

    person3.set_wage(4600)
    person3.set_bonus(50)

    staff.append(person1)
    staff.append(person2)
    staff.append(person3)

    for person in staff:

        print("%s works as %s and earns %.2f USD monthly" % (person.get_full_name(), person.position, person.get_total_income()))




