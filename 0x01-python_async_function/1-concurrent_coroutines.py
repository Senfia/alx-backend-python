#!/usr/bin/env python3

'''run n asynchronous tasks concurrently, each with a
   random delay, and return the sorted list of completion times.
'''

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''returns a sorted list of all the delays
    '''
    waits = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(waits)
