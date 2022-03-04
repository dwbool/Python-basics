import sys

workout = float(sys.argv[1])
rate = float(sys.argv[2])
incentive = float(sys.argv[3])

salary = workout * rate + incentive

print("salary is %f " % salary)
