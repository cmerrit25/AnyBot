from discord.ext import commands
import discord

class UserStatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="user_status")
    async def user_status(self, ctx, *nickname):

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

                
            else:
                await ctx.author.send(
                    f"{member.name} has no current activity..."
                )
        elif member.status == discord.Status.dnd:
            await ctx.author.send(f"{member.name} doesn\'t want to be disturbed...")
def setup(bot):
    bot.add_cog(UserStatusCog(bot))