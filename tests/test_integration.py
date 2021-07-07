import asyncio
import sys
import pytest


if 'win32' in sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

@pytest.mark.asyncio
async def test_sample():
    loop = asyncio.get_running_loop()
    return
    


