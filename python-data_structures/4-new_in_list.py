#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Orijinal siyahının kopyasını yaradırıq
    new_list = my_list.copy()
    
    # İndeks düzgündürsə, kopyanın daxilində dəyişiklik edirik
    if 0 <= idx < len(my_list):
        new_list[idx] = element
        
    return new_list
