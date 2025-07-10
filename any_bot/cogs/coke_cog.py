from discord.ext import commands
import discord

coke_log: dict[str, int] = {}

class CokeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="coke")
    async def coke(self, ctx, *nickname):

        nickname = " ".join(nickname)
        guild = ctx.guild
        member = discord.utils.get(guild.members, display_name=nickname)

        if member is None:
            await ctx.author.send(f"{nickname} is not in the server.")
            return

        try:
            coke_log[nickname] += 1
        except KeyError:
            coke_log[nickname] = 1

        cokes_drank = coke_log[nickname]
        if cokes_drank == 0:
            await ctx.author.send(f"{nickname} needs some coke!")
        elif cokes_drank == 1:
            await ctx.author.send(f"{nickname} has drank his first coke! Pop another!")
        else:
            await ctx.author.send(f"{nickname} has drank {cokes_drank} cokes! Keep going!")

def setup(bot):
    bot.add_cog(CokeCog(bot))
        