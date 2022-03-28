from asyncio import sleep
from os import getcwd
from pathlib import Path
from src.api.youtube_downloader import YoutubeDownloader

import discord

from discord.ext import commands


class AudioCog(commands.Cog, name="Audio"):
    def __init__(self, bot):
        self.bot = bot

    async def _play_file(self, ctx, file_path):
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(file_path))
        ctx.voice_client.play(
            source, after=lambda e: print("Player error: %s" % e) if e else None
        )

        while ctx.voice_client.is_playing():  # Checks if voice is playing
            await sleep(1)  # While it's playing it sleeps for 1 second
        else:
            await sleep(2)  # If it's not playing it waits 2 seconds
            while (
                ctx.voice_client.is_playing()
            ):  # and checks once again if the bot is not playing
                break  # if it's playing it breaks
            else:
                await ctx.voice_client.disconnect()  # if not it disconnects

    @commands.command()
    async def chevyVan(self, ctx: commands.Context):
        """Plays a file from the local filesystem"""

        file_path = Path(f"{getcwd()}/audio/chevyvan.mp3")

        await self._play_file(ctx, file_path)

    @commands.command(name="disconnect")
    async def disconnect(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @commands.command(name="yt")
    async def yt(self, ctx, *, link):
        """
        use: !yt [yt_url]
        """

        yt_dl = YoutubeDownloader()

        path = yt_dl.get_video_audio(link)

        if path is not None:
            await self._play_file(ctx, path)
        else:
            await ctx.send("Please enter a valid youtube link.")

    @commands.command(name="ytSearch")
    async def yt_search(self, ctx, *, query):
        """
        use: !yt-search [query]
        """

        yt_dl = YoutubeDownloader()

        results = yt_dl.search(query)

        titles = "\n".join([f"{i + 1}: {x.title}" for i, x in enumerate(results)])

        msg = await ctx.send(titles)

        # Unicode codepoints for 1 through 4 with cap enclosing codepoint (To Make 1 through 4 keycap emojis)
        emojis = [
            "\u0031\u20E3",
            "\u0032\u20E3",
            "\u0033\u20E3",
            "\u0034\u20E3",
            "\u0035\u20E3",
        ]

        for emoji in emojis:
            await msg.add_reaction(emoji)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in emojis

        try:
            reaction, user = await self.bot.wait_for(
                "reaction_add", timeout=30.0, check=check
            )

            user: discord.Member = user

            reaction = str(reaction)

            if reaction in emojis:

                index = emojis.index(reaction)

            url = results[index].watch_url

            path = yt_dl.get_video_audio(url)

            await ctx.message.delete()
            await msg.delete()

            await ctx.send(f"Now playing: {results[index].title}")

            await self._play_file(ctx, path)

        except Exception as e:
            await msg.reply(f"There was no reaction given in time.")

    @chevyVan.before_invoke
    @yt.before_invoke
    @yt_search.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
