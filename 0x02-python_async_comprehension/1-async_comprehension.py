#!/usr/bin/env python3
'''Async Generator Module
'''

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''Generate a list of ten numbers using a ten-number generator.
    '''
    return [rand async for rand in async_generator()]
