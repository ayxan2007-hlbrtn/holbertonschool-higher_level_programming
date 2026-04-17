#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Açarı və dəyəri lüğətə mənimsədirik (mövcuddursa yenilənir, yoxdursa yaranır)
    a_dictionary[key] = value
    return a_dictionary
