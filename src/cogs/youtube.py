from discord.ext import commands
from discord.utils import get
from src.api.youtube import YoutubeAPI


class YoutubeCog(commands.Cog, name="YouTube"):
    def __init__(self, bot):
        self.bot = bot
        self.yt_api = YoutubeAPI()

    @commands.command(name="playVideo")
    async def play_video(self, ctx, *args):
        search_term = " ".join(args)

        results = await self.yt_api.search(search_term)

        titles = [video["result"][0]["title"] for video in results]
        # Prepend numbers to titles
        titles = [f"{i + 1}: {title}" for i, title in enumerate(titles)]

        ids = [video["result"][0]["id"] for video in results]

        response = "\n".join(titles)

        message = await ctx.send(response)

        check = (
            lambda m, c, a: m.content in [1, 2, 3, 4, 5]
            and m.channel == c
            and m.author == a
        )

        msg = await self.wait_for(
            "message",
            check=check(ctx.message, ctx.channel, ctx.author),
        )
        # msg variable stores the new user input(rock/paper/scissors) [your code down]
        await ctx.send(f"User chose {msg.content}")
