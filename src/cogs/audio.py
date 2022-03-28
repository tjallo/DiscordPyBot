from os import getcwd
from pathlib import Path

import discord

from discord.ext import commands


class AudioCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chevyVan(self, ctx):
        """Plays a file from the local filesystem"""

        file_path = Path(f"{getcwd()}/audio/chevyvan.mp3")

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(file_path))
        ctx.voice_client.play(
            source, after=lambda e: print("Player error: %s" % e) if e else None
        )

        await ctx.send("Now playing: {}".format(file_path))

    @commands.command(name="disconnect")
    async def disconnect(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @chevyVan.before_invoke
    async def ensure_voice(self, ctx):
        ctx.voice_client.source.volume = 1
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
