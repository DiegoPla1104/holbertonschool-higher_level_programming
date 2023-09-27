#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = []
    for j in range(list_length):
        k = 0
        try:
            k = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            i.append(k)
    return(i)
