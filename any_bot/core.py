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
async def user_status(ctx, *nickname):

    nickname = " ".join(nickname)
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

            spotify_activity = discord.utils.find(
                lambda a: isinstance(a, discord.Spotify), 
                member.activities
            )

            if spotify_activity:
                await ctx.author.send(f"Currently listening to {spotify_activity[0].title}")
            else:
                await ctx.author.send(f"{nickname} is not listening to Spotify right now...")
            
        else:
            await ctx.author.send(
                f"{member.name} has no current activity."
            )
    elif member.status == discord.Status.dnd:
        await ctx.author.send(f"{member.name} doesn\'t want to be disturbed...")
        

    
    else:
        await ctx.author.send(f"{member.name} is offline")

    channel = bot.get_channel(CHANNEL_ID) or await bot.fetch_channel(CHANNEL_ID)
    await channel.send(f"Hey! {nickname} is a great person")

