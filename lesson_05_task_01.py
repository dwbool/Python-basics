print("input text, empty line to exit the program")
with open("notes.txt", "w", encoding="utf-8") as f:
    while 1:
        s = input()
        if len(s) == 0:
            print("exiting the program")
            break
        else:
            f.write(s + "\n")
