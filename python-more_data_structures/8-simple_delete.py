#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Açarı lüğətdə axtarırıq, varsa silirik
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
