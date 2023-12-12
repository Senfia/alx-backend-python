#!/usr/bin/env python3
'''Async Generator Module
'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure the total runtime of an imported module and return it
    '''
    start_t = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_t
