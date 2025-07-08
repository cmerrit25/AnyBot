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

intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix="!", 
    intents=intents, 
    description="This is AnyBot.\nCommands currently include online and activity status checks."
)

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


@bot.command(name="user_status")
async def user_status(ctx, nickname: str):

    guild = ctx.guild
    member = discord.utils.get(guild.members, display_name=nickname)

    if member is None:
        await ctx.author.send(f"{nickname} is not in the server.")
        return
    
    if member.voice and member.voice.channel:
        await ctx.author.send(f"{nickname} is currently in voice channel: {member.voice.channel.name}.")

    if member.status == discord.Status.online:
        await ctx.author.send(f"{member.name} is online!")
        if member.activities:
            activity = member.activities[0]
            await ctx.author.send(f"Currently playing: {activity}.")
            
        else:
            await ctx.author.send(
                f"{member.name} has no current activity."
            )
        return

    status_msg = f"{member.name} is {member.status}."
    await ctx.get_channel(CHANNEL_ID).send(f"Hey! {status_msg}")

