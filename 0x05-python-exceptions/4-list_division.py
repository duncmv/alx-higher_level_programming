#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new = []
    while list_length > 0:
        try:
            new.append(my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            new.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new.append(0)
            print("division by zero")
        except IndexError:
            new.append(0)
            print("out of range")
        finally:
            i += 1
            list_length -= 1
    return new
