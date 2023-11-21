#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    x = 0
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            x = 1
        except ZeroDivisionError:
            print("division by 0")
            x = 1
        except IndexError:
            print("out of range")
            x = 1
        finally:
            if x:
                x = 0
                new.append(0)
            else:
                new.append(res)
    return new
