from discord.ext import commands
from sources.api import reddit_api as RedditAPI

class Reddit(commands.Cog, name="Reddit"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userkarma")
    async def userkarma(self, ctx, arg):
        """
        Get an user's karma
        user : !userkarma snoop
        """
        karma = RedditAPI.get_karma(arg)
        await ctx.send(karma)

def setup(bot):
    bot.add_cog(Reddit(bot))
