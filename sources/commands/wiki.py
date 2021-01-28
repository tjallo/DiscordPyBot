from discord.ext import commands
from sources.api import wikipedia_api as Wiki

class Wikipedia(commands.Cog, name='Wikipedia'):
    """
    The Wikipedia API is kinda broken
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wikiArticle")
    async def getArticle(self, ctx, arg):
        """Get an Wikipedia article
        use: !wikiArticle \"Dutch East India Company\""""

        result = Wiki.get_summary(arg)

        await ctx.send(result)

    @commands.command(name="wikiImage")
    async def wikiImage(self, ctx, arg):
        """Get the first image of a Wikipedia article
        use: !wikiImage \"Dutch East India Company\""""

        result = Wiki.get_image(arg)

        await ctx.send(result)

def setup(bot):
    bot.add_cog(Wikipedia(bot))
