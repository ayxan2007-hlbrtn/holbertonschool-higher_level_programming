#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Hər bir key-value cütü üçün value-nu 2-yə vurub yeni lüğət yaradırıq
    return {key: value * 2 for key, value in a_dictionary.items()}
