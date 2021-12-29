from discord.ext import commands
from discord import Member

class ChatCog(commands.Cog, name="Chat"):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx, *, member: Member = None):
        """- Returns pong"""
        member = member or ctx.author
        await ctx.send(f"Hello {member.mention}!")

