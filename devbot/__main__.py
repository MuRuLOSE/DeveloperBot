import asyncio
from .main import main
import logging
import sys

# Возможно когда-нибудь я здесь что-нибудь сделаю

async def run() -> None:
    
    await main()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        pass #ok