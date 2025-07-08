import os, discord, logging
from logging_config import start_logger
from dotenv import load_dotenv
from discord.ext import commands

start_logger(logfile='info.log', level=logging.INFO)

logger = logging.getLogger(__name__)

load_dotenv()
TOKEN    = os.getenv("DISCORD_TOKEN")
CHANNEL_ID= os.getenv("CHANNEL_ID")

GUILD_ID = None

description = """This is AnyBot.

Commands currently only include sending online and activity status of given user nicknames."""

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    
    logger.info(f"Channel ID: {CHANNEL_ID}")

    try:
        channel = bot.get_channel(CHANNEL_ID) or await bot.fetch_channel(CHANNEL_ID)
        await channel.send("Hello, my friend! I'm AnyBot! What can I do for you today?")
    
    except AttributeError:
        logger.error("Couldn't find the channel...")


#checking for online and activity status of given nicknamed user
@bot.command()
async def user_status(ctx, nickname):

    guild  = ctx.guild   #retrieve guild object when bot is ready

    member = discord.utils.get(guild.members, display_name=nickname)  #search for member in server by given nickname

    if member is None:
        await ctx.author.send(f"{nickname} is not in the server...")

    elif member.status == discord.Status.online:
        
        user = ctx.author
        await user.send(f"{member.name} is online!")

        if member.activities:          #report the first activity if it's available
            await user.send(f"{member} is currently {member.activities[0]}.")
        else:
            await user.send(f"{member} is currently doing absolutely nothing...")

    else:     #hit the channel telling that the user is offline
        channel = bot.get_channel(CHANNEL_ID) or await bot.fetch_channel(CHANNEL_ID)
        await channel.send(f"Hey, {member.name} is {member.status} right now.")
        

bot.run(TOKEN)
