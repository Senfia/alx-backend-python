#!/usr/bin/env python3
'''Element length
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''This function calculates the total number of
       elements in a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
