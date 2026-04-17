#!/usr/bin/python3
def best_score(a_dictionary):
    # Lüğətin boş olub-olmadığını yoxlayırıq
    if not a_dictionary:
        return None
    
    # Ən böyük dəyərə (xala) sahib açarı (key) tapırıq
    return max(a_dictionary, key=a_dictionary.get)
