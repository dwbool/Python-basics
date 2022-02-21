isec = int(input("please input an integer number of seconds "))
imin = int(isec // 60)
ihours = int(imin // 60)
print("the time interval you entered is %02d:%02d:%02d" % (ihours, int(imin % 60), int(isec % 60)))
