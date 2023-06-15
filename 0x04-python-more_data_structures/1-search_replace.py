#!/usr/bin/pyton3

def search_replace(my_list, search, replace):
    new_kist = list(map(lambda x: replace if x == search else x, my_list))
    return(new_list)
