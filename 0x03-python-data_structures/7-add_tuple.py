#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples."""
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    # If both tuples are empty assign (0,0) to each.
    if len_a == 0:
        tuple_a = 0, 0
    if len_b == 0:
        tuple_b = 0, 0

    # If either tuples have 1 arg, assign 0 as the second arg.
    if len_a == 1:
        tuple_a = tuple_a[0], 0
    if len_b == 1:
        tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
