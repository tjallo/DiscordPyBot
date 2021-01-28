from discord.ext import commands


class Chat(commands.Cog, name="Chat"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def cool_bot(self, ctx):
        """Test to see if the bot is properly online
        use: !ping"""
        await ctx.send(f'Hello, {ctx.message.author.name}!')


def setup(bot):
    bot.add_cog(Chat(bot))
