from asyncio import sleep
from pathlib import Path
from discord.ext import commands
from os import getcwd
from discord import FFmpegPCMAudio, VoiceProtocol, PCMVolumeTransformer
from discord.ext.commands import Context


class AudioCog(commands.Cog, name="Audio"):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name='chevyVan')
    async def test(self, ctx: Context):

        file_path = Path(f"{getcwd()}/audio/chevyvan.mp3")
        

        if ctx.voice_client is None:
            if ctx.voice_client is None:
                if ctx.author.voice:
                    await ctx.author.voice.channel.connect()
                else:
                    await ctx.send("You are not connected to a voice channel.")
                    raise commands.CommandError("Author not connected to a voice channel.")
            elif ctx.voice_client.is_playing():
                ctx.voice_client.stop()

        vc: VoiceProtocol = ctx.voice_client

        vc.connect(reconnect=True, timeout=30)

        source = PCMVolumeTransformer(FFmpegPCMAudio(file_path))               
            


        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) and vc.disconnect() if e else None)
