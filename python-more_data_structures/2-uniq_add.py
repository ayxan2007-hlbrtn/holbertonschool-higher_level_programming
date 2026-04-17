#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Siyahını çoxluğa çeviririk ki, təkrarlar silinsin, sonra toplayırıq
    return sum(set(my_list))
