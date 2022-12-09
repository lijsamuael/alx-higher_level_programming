#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list = [(x if not x == search else replace) for x in my_list]
#    new_list = [my_list[my_list.index(search)] = replace for x in
#                my_list.count(search)]
    return new_list
