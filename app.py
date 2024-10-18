import asyncio
from sample.worker import (
    broker,
    test_task
)

async def main():
    await broker.startup()
    await test_task.kiq()

if __name__ == '__main__':
    asyncio.run(main())

