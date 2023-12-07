#!/usr/bin/env python3
'''Complex types - functions
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a function that multiplies given numbers.
    '''
    return lambda num: num * multiplier
