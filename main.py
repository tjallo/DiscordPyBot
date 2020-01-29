from reddit_api import reddit_main
from wiki_api import wiki_api
from google_api import google_api
from deepfryer import deepfry
from discord.ext import commands
from credentials import token
from utils import utils
from meme_generator import memeGen
from werkzeug.urls import url_fix
from derp import mainDerp
import asyncio
import discord
import requests
import shutil
import os
import random


r = reddit_main
w = wiki_api
g = google_api
d = deepfry
u = utils
m = memeGen
h = mainDerp

commandList = """
!help - See this message
!ping - Pong!
!wiki - Get a wiki article
!imgwiki - Get the first image on a Wiki Article
!rkarma - Get an user's total karma on reddit
!sourcecode - Get a GitHub link to the bot's source code
!imgsearch - Google and post an image
!deepfry - Google and deepfry an image
!getmemelist - get top 10 meme's right now on imgflip with corrosponding id
\"!memegen (id)-(text1)-(text2)\" - generates a meme using imgflip meme id
!isgay - random gay generator
!destroylibtard - send an inspirational quote
!addquote - add quote to the inspirational quotes list.
"""

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help' or '!yelp'):        
        await message.channel.send(commandList)
    
    if message.content.startswith('!ping'):
        print(message)
        await message.channel.send('Pong!')
    
    if message.content.startswith('!wiki'):
        if (len(message.content) == 5): await message.channel.send("Proper way to use is !wiki [wiki article]")
        else:
            await message.channel.send(w.get_article(message.content[6:]))

    if message.content.startswith('!imgwiki'):
        if (len(message.content) == 8): await message.channel.send("Proper way to use is !imgwiki [wiki article]")
        else:
          await message.channel.send(w.get_image(message.content[9:]))   

    if message.content.startswith('!rkarma'):
        if (len(message.content) == 7): await message.channel.send("Proper way to use is !rkarma [reddit user name]")
        else:
            await message.channel.send(r.get_karma(message.content[8:]))   
    if message.content.startswith('!sourcecode'):
        await message.channel.send("You can finde the source code here: https://github.com/tjallo/DiscordPyBot")

    if message.content.startswith('!imgsearch'):
        if (len(message.content) == 10): await message.channel.send("Proper way to use is !imgsearch [query]")
        else:
            try:
                query = message.content[11:]
                path = g.googleImgSearch(query)
                file = discord.File(path, filename=path[-5:])            
                await message.channel.send(file=file) 
                os.remove(path)
                u.removeDownloads()
            except:
                await message.channel.send("No such image was found :(")     
                            
    if message.content.startswith('!deepfry'):
        if (len(message.content) == 9): await message.channel.send("Proper way to use is !deepfry [imgSearch]")
        else:
            try:
                query = message.content[9:]
                d.fryMe(g.googleImgSearch(query))
                path = "downloads/fried.jpeg"
                file = discord.File(path, filename=path[-8:])            
                await message.channel.send(file=file)         
                #u.removeDownloads()
            except:
                await message.channel.send("Image not found")
        

    if message.content.startswith('!memegen'):
        if (len(message.content) == 8): await message.channel.send("Proper way to use is !memegen (id)-(text1)-(text2)")
        else:
            try:
                splitThis = message.content[9:]
                output = splitThis.split('-')
                url = url_fix((m.createMeme(output[0], output[1], output[2])).strip(os.sep))
                url = u.remove_at(7, url)
                url = u.remove_at(7, url)
                await message.channel.send(url) 
            except:
               await message.channel.send("Memegen failed!")


    if message.content.startswith("!getmemelist"):
        result = m.parseMemeList()
        await message.channel.send("This is the start of the meme list, please wait for the ending message:")
        for i in range(10):            
            await message.channel.send(f"Title: {result[1][i]}, ID: {result[0][i]}")
        link = "https://api.imgflip.com/popular_meme_ids"
        await message.channel.send(f"For the current top 100 memes check: {link}")
        await message.channel.send("This is the end of the meme list")

    if message.content.startswith("!isgay"):
        output = h.isGay((message.content[7:]).lower())
        await message.channel.send(f"{message.content[7:]} is {output}% gay!")

#    if "real man" in message.content.lower():
#        channel = message.author.voice.channel
#        vc = await channel.connect()        
#        vc.play(discord.PCMAudio(pipe=True))
#        
#        await vc.disconnect()

    if message.content.startswith("!destroylibtard"):
        fileN = "media//offensive.txt"
        length = u.file_len(fileN) -1
        pick = random.randint(0,length)     
        f=open(fileN)
        lines=f.readlines()
        await message.channel.send(lines[pick])
        
            
    if message.content.startswith("!addquote"):
        inText = message.content[10:]
        u.addLineToFile(f'\n{inText} ', 'media/offensive.txt')
        await message.channel.send(f'Quote : \"{inText}\", was added to the inspirational quotes file.')


client.run(token)