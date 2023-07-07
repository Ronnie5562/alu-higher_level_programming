#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            if str(i) + str(j) == str(89):
                print("{}".format(str(i) + str(j)))
            else:
                print("{}".format(str(i) + str(j)), end=", ")
