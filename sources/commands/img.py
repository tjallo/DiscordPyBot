from sources.api.imgflip_api import generateMemeURL
from discord.ext import commands
import discord

from sources.api import image_api as Img
from sources.api import imgflip_api as Flip


class Images(commands.Cog, name="Images"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="imgSearch")
    async def imgSearch(self, ctx, arg):
        """
        Search DuckDuckGo for images (takes a little while to load)
        use: !imgSearch "The Spanish Inquisition"
        """
        await ctx.send("Processing...")

        link = Img.getImageLink(arg)

        await ctx.send(link)

    @commands.command(name="deepfry")
    async def fileDownload(self, ctx, *arg):
        """
        deepfry images from the internet
        use: !deepfry "Jan Pieterszoon Coen"
        """

        arg = " ".join(arg)

        await ctx.send(f"Working on deepfrying {arg}....")

        path = await Img.deepfrySearch(arg)
        try:
            await ctx.send(file=discord.File(path))
        except:
            await ctx.send("Image not found...")

    @commands.command(name="memeIDs")
    async def memeIDs(self, ctx):
        """
        Get list of popular imglfip meme IDs, to be used with memegenerator
        use: !memeIDs
        """

        ids = Flip.getPopularMemeIDs()
        output = ""

        for entry in ids:
            output += f"{entry[0]}, {entry[1]}\n"
        output =output[:1999]
        await ctx.send(output[:output.rfind("\n")])

    @commands.command(name="memeGenerator")
    async def memeGenerator(self,ctx,*arg):
        """
        Generate a meme using imgflip's api
        use: !memeGenerator "memeID" "top text" "bottom text"
        """
        memeID = arg[0]
        topText = arg[1]
        bottomText = arg[2]

        await ctx.send(Flip.generateMemeURL(memeID, topText, bottomText))

def setup(bot):
    bot.add_cog(Images(bot))
