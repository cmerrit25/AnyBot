from discord.ext import commands
import discord

class MusicCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="music")
    async def spotify(self, ctx, user: discord.Member = None):

        if user == None:
            user = ctx.author
            pass

        if user.activities:
            for activity in user.activities:
                if isinstance(activity, discord.Spotify):
                    embed = discord.Embed(
                        title = f"{user.name}'s Spotify",
                        description = "Listening to {}".format(activity.title),
                        color = 0xC902ff
                    )
                    embed.set_thumbnail(url=activity.album_cover_url)
                    embed.add_field(name="Artist", value=activity.artist)
                    embed.add_field(name="Album", value=activity.album)
                    embed.set_footer(text="Song started at {}".format(activity.created_at.strftime("%H:%M")))
                    await ctx.send(embed=embed)

        else:
            await ctx.author.send(f"{user.name} is not participating in any activities right now...")

            online_status = user.client_status.status if user.client_status.status is not None else "offline"
            desktop_status = user.client_status.desktop_status if user.client_status.desktop_status is not None else "offline"
            mobile_status = user.client_status.mobile_status if user.client_status.mobile_status is not None else "offline"
            web_status = user.client_status.web_status if user.client_status.web_status is not None else "offline"
            
            await ctx.author.send(f"{user.name} is currently {online_status} on discord, {desktop_status} on their desktop\
            {mobile_status} on their mobile device, and {web_status} on discord web browser.")

def setup(bot):
    bot.add_cog(MusicCog(bot))