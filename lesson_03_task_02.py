def person_data(name, surname, birth_y, city, email, phone):
    print("%s %s born in %s lives in %s has email %s, phone %s" % (name, surname, str(birth_y), city, email, str(phone)))


print("Input personal details:")
name = input("name ")
surname = input("surname ")
birth_y = input("birth year ")
city = input("city ")
email = input("email ")
phone = input("phone ")
person_data(name, surname, birth_y, city, email, phone)
