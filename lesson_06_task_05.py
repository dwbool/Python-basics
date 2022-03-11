import subprocess, os, platform
import pathlib
import os.path
import time

"""
it is assumed that the files named 

Pen.jpg
Pencil.jpg
Handle.jpg
Stationery.jpg

are located in the script's directory
"""

# https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
# https://stackoverflow.com/questions/434597/open-document-with-default-os-application-in-python-both-in-windows-and-mac-os


class Stationery:

    def __init__(self):
        self.title = "Stationery"

    def draw(self):
        if type(self).__name__ == "Stationery":
            s = "piece of " + self.title + " : " + str(self)
            print(s)
        try:
            fn = self.file_name()
            if os.path.isfile(fn):
                if platform.system() == 'Darwin':  # macOS
                    subprocess.call(('open', fn))
                elif platform.system() == 'Windows':  # Windows
                    os.startfile(fn)
                else:  # linux variants
                    subprocess.call(('xdg-open', fn))
        except:
            pass

    def file_name(self):
        s: str = str(pathlib.Path().resolve())
        s += '/' + self.title + ".jpg"
        return s


class Pen(Stationery):

    def __init__(self):
        self.title = "Pen"

    def draw(self):
        print("good " + self.title)
        super().draw()


class Pencil(Stationery):

    def __init__(self):
        self.title = "Pencil"

    def draw(self):
        print("nice " + self.title)
        super().draw()


class Handle(Stationery):

    def __init__(self):
        self.title = "Handle"

    def draw(self):
        print("mediocre " + self.title)
        super().draw()


if __name__ == "__main__":

    stationery = Stationery()
    pen = Pen()
    pencil = Pencil()
    handle = Handle()

    box = []

    box.append(stationery)
    box.append(pen)
    box.append(pencil)
    box.append(handle)

    for item in box:
        item.draw()
        time.sleep(1.1)

"""
s:str = str( pathlib.Path().resolve())
s+='/'+"Pencil.jpg"
print(s)
#subprocess.run(['open',s ], check=True)
#os.startfile(s)
"""
