from discord.ext import commands
from discord import Member
from os.path import curdir, abspath
from pathlib import Path
from discord import Member
from src.api.user_manager import UserManager
from os import getcwd

from discord.ext.commands.context import Context


class ChatCog(commands.Cog, name="Chat"):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx, *, member: Member = None):
        """- Returns pong"""
        member = member or ctx.author
        await ctx.send(f"Hello {member.mention}!")

    @commands.command(name="whoami")
    async def ping(self, ctx, *, member: Member = None):
        member = member or ctx.author
        await ctx.send(
            f"I am the ChevyVanDealer discord bot; you can find my source code here: https://github.com/tjallo/DiscordPyBot/"
        )

    @commands.command(name="shrek")
    async def shrek(self, ctx):
        """Please... Just don't."""
        member = ctx.author
        await ctx.send(f"@everyone you have {member.mention} to thank for this...")

        path = Path(abspath(curdir)) / "resources" / "other" / "shrek.txt"

        with open(path, "r") as file:
            words = "".join(file.readlines())

        n = 1900
        words = [words[i : i + n] for i in range(0, len(words), n)]

        for word in words:
            await ctx.send(word)

    @commands.command(name="ghostping")
    async def deepfry(self, ctx, member: Member = None):
        """ most annonying function in this bot"""
        member = member or ctx.author

        await ctx.message.delete()
        
        if ctx.author.__str__() == "Tjalle#0810":
            msg = await ctx.send("@everyone")
            await msg.delete()
        else:
            await ctx.send("Uh oh, you are not allowed to use this comment!")
