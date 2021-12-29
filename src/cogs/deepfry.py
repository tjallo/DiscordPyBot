from discord.ext import commands
from discord import Member
from src.api.deepfry import DeepfryAPI
from discord.file import File

class DeepfryCog(commands.Cog, name="Deepfry"):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot
        self.deepfrier = DeepfryAPI()

    @commands.command(name="deepfry")
    async def deepfry(self, ctx, arg, member: Member = None):
        """ [image_url] - deepfries image"""
        member = member or ctx.author

        await ctx.message.delete()
        
        try:
            img_path = await self.deepfrier.deepfry(arg.strip())

            with open(img_path, 'rb') as f:
                msg = File(f)
                picture = True
        except Exception as e:
            await ctx.send(e)
            picture = False
            msg = "Invalid url. Make sure you supply an image url."

        if picture:
            await ctx.send(file=msg)
        else:
            await ctx.send(msg)