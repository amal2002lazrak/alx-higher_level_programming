#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_dic = list(a_dictionary.keys())
    list_dic.sort()

    for i in list_dic:
        print("{}: {}" .format(i, a_dictionary.get(i)))
