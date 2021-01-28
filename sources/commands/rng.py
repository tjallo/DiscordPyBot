from discord.ext import commands

import random

class RnG(commands.Cog, name="RnG"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="flipcoin")
    async def coin_flip(self, ctx):
        """Flip a coin
         use: !flipcoin"""
        rand = random.randint(0, 1)
        msg = ""

        if (rand):
            msg = "Heads!"
        else:
            msg = "Tails!"

        await ctx.send(msg)


def setup(bot):
    bot.add_cog(RnG(bot))
