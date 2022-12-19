#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            answer = my_list_1[i] / my_list_2[i]
        except TypeError:
            answer = 0
            print("{}".format("wrong type"))
        except ZeroDivisionError:
            answer = 0
            print("{}".format("division by 0"))
        except IndexError:
            answer = 0
            print("{}".format("out of range"))
        finally:
            new_list.append(answer)
    return new_list
