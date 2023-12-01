#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x2_ist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            x2_list[count] = True
        else:
            x2_list[count] = False
    return(x2_list)
