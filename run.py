from any_bot.core import bot, TOKEN, load_extensions
import asyncio

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
