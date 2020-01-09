from reddit_api import reddit_main
from wiki_api import wiki_api
from google_api import google_api
from deepfryer import deepfry
from discord.ext import commands
from credentials import token
from utils import utils
import discord
import os


r = reddit_main
w = wiki_api
g = google_api
d = deepfry
u = utils

commandList = """
!help - See this message
!ping - Pong!
!wiki - Get a wiki article
!imgwiki - Get the first image on a Wiki Article
!rkarma - Get an user's total karma on reddit
!sourcecode - Get a GitHub link to the bot's source code
!imgsearch - Google and post an image
!deepfry - Google and deepfry an image
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
                path = "Downloads/fried.jpeg"
                file = discord.File(path, filename=path[-8:])            
                await message.channel.send(file=file)         
                u.removeDownloads()
            except:
                await message.channel.send("Image not found")
        

client.run(token)