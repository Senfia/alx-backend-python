#!/usr/bin/env python3
'''An asynchronous coroutine that takes in an integer
   that waits for a random delay between 0 and
   `max_delay` (included and float value) seconds and
   eventually returns it.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Returns an random number after some seconds
    '''
    wait_seconds: float = random.random() * max_delay
    await asyncio.sleep(wait_seconds)
    return wait_seconds
