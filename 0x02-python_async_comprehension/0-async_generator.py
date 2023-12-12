#!/usr/bin/env python3
'''Async Generator Module
'''
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    '''yield a random number between 0 and 10 after 10 loops
    '''
    count = 0
    while count < 10:
        await asyncio.sleep(1)
        yield random.random() * 10
        count += 1
