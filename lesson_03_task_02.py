def person_data(**argv):
    if len(argv) != 6:
        print("not enough or too many arguments")
        return
    name = argv["name"]
    surname = argv["surname"]
    birth_y = argv["birth_y"]
    city = argv["city"]
    email = argv["email"]
    phone = argv["phone"]
    print(
        "%s %s born in %s lives in %s has email %s, phone %s" % (name, surname, str(birth_y), city, email, str(phone)))


print("Input personal details:")
name1 = input("name ")
surname = input("surname ")
birth_y = input("birth year ")
city = input("city ")
email = input("email ")
phone = input("phone ")
person_data(name=name1, surname=surname, birth_y=birth_y, city=city, email=email, phone=phone)
