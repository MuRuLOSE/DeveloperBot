import asyncio
from .main import main
import logging
import sys
import contextlib

# Возможно когда-нибудь я здесь что-нибудь сделаю

async def run():
    await main()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(run())