import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN    = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
USER_ID  = os.getenv("USER_ID")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def user_status(ctx, nickname):

    guild  = bot.get_guild(GUILD_ID)

    member = discord.utils.get(guild.members, display_name=nickname)
    if member is None:
        await user.send(f"{nickname} is not in the server...")

    if member.status == discord.Status.online:
        
        user = ctx.author
        await user.send(f"{member.name} is online!")
    else:
        user = ctx.author
        await user.send(f"{member.name} is {member.status}")

    await bot.close() 

bot.run(TOKEN)
