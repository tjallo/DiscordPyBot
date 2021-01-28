from discord.ext import commands
from discord import FFmpegOpusAudio
from discord.utils import get
from pytube.__main__ import YouTube
from sources.api import youtube_api as Youtube
import subprocess, asyncio, os

MP3_FOLDER = 'resources/mp3'


def getTimeFromFile(file):
    args=("ffprobe","-show_entries", "format=duration","-i",file)
    popen = subprocess.Popen(args, stdout = subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read().decode().split()[1]

    time = float(output.split('=')[-1])

    return time

    
def mp3_handler():   
    if not os.path.exists(MP3_FOLDER):
        os.mkdir(MP3_FOLDER)

    files = os.listdir(MP3_FOLDER)

    for file in files:
        os.remove(f'{MP3_FOLDER}/{file}')
   


async def disconnectFromChannelAfterNSeconds(voice, N):
    await asyncio.sleep(N)
    await voice.disconnect()


class Voice(commands.Cog, name="Voice"):

    def __init__(self, bot):
        self.bot = bot

    

    @commands.command(name='chevyvan')
    async def chevyvan(self, ctx):
        """Only for real men
        use: !chevyvan
        """

        file = 'resources/sounds/chevyvan.mp3'
        await ctx.send('If you wanna be a real man')

        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        source = FFmpegOpusAudio(file)
        player = voice.play(source)

        runtime = getTimeFromFile(file)

        await disconnectFromChannelAfterNSeconds(voice, runtime + 2)




    @commands.command(name='youtube')
    async def youtube(self, ctx, *arg):
        """
        Play a song from youtube
        use: !youtube Never Gonna Give you Up
        """

        def check(reaction, user):
            return user != self.bot.user

        def check2(reaction, user):
            return user != self.bot.user

        mp3_handler()

        query = " ".join(arg)

        results = Youtube.get_urls_and_titles(query)

        sendThis = ""

        for i, result in enumerate(results):
            sendThis += f"**{i+1}** - {result[0]}\n"

        message = await ctx.send(sendThis)

        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        await message.add_reaction("4️⃣")
        await message.add_reaction("5️⃣")

        emoji, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

        emoji = emoji.emoji
        number = 0
        numbers = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣']
        index = numbers.index(emoji) 

        await message.delete()
        

        current_title = results[index][0]
        url = results[index][1]

        file = Youtube.download_video(url, MP3_FOLDER)

        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        source = FFmpegOpusAudio(file)
        player = voice.play(source)

        runtime = getTimeFromFile(file)

        msg1 = await ctx.send(f"Now playing: {current_title}")
        await msg1.add_reaction("🛑")

        emoji3, user3 = await self.bot.wait_for('reaction_add', timeout=runtime + 3, check=check)

        await ctx.send(f"{user3} has stopped playback")

        await disconnectFromChannelAfterNSeconds(voice, 0)
        




def setup(bot):
    bot.add_cog(Voice(bot))
