
class MyList(list):

    def append(self, val):

        if type(val) is int or type(val) is float:
            super().append(float(val))
        else:
            num_value = None
            try:
                num_value = float(val)
            except Exception as e:
                pass
            if num_value is not None:
                super().append(num_value)
            else:
                raise Exception("value is not number: "+val)


if __name__ == "__main__":

    lst = MyList()

    while 1:
        print("input number or stop to exit:")
        s = input()
        if s.lower() == "stop":
            print("quitting the program")
            break
        try:
            lst.append(s)
        except Exception as e:
            print("error: %s" % str(e))

        print("list is: %s" % str(lst))







