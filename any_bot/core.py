import os
import logging
import discord
from dotenv import load_dotenv
from discord.ext import commands
from any_bot.logging_config import start_logger

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

start_logger(logfile='info.log', level=logging.INFO)
logger = logging.getLogger(__name__)

intents = discord.Intents().all()
intents.members = True
intents.presences = True

bot = commands.Bot(
    command_prefix="!", 
    intents=intents, 
    description="This is AnyBot.\nCommands currently include online and activity status checks."
)

bot.load_extension("cogs.coke_cog")
bot.load_extension("cogs.music_cog")
bot.load_extension("cogs.user_status_cog")

@bot.event
async def on_ready():

    logger.info(f"Connected as {bot.user} (ID: {bot.user.id})")
    logger.info(f"Target Channel ID: {CHANNEL_ID}")

    try:
        channel = bot.get_channel(CHANNEL_ID) or await bot.fetch_channel(CHANNEL_ID)
        await channel.send(
            "Hello, my friend! I'm AnyBot! What can I do for you today?"
        )
    except Exception as e:
        logger.error(f"Failed to send on_ready message: {e}")


