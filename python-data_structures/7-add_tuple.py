#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Hər tuple-ın ilk 2 elementini götürürük, yoxdursa 0 yazırıq
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Cəmi hesablayırıq
    return (a[0] + b[0], a[1] + b[1])
