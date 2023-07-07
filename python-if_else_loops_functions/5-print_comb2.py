#!/usr/bin/python3
for num in range(100):
    if num == 99:
        print("{}".format(str(num).zfill(2)))
        continue
    print("{}".format(str(num).zfill(2)), end=", ")
