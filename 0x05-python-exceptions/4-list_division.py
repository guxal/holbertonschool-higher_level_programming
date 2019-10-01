#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for idx in range(list_length):
        try:
            r = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            r = 0
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        finally:
            result_list += [r]
    return result_list
