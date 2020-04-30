from reddit_api import reddit_main as r
from wiki_api import wiki_api as w
from google_api import google_api as g
from deepfryer import deepfry as d
from discord.ext import commands
from credentials import token
from utils import utils as u
from meme_generator import memeGen as m
from werkzeug.urls import url_fix
from derp import mainDerp as h
from lastfm_api import last as l
from lastfm_api import LastFMTopTracksprettyJSON
from lastfm_api import getInfoPretty
from lastfm_api import getTopArtistsPretty
import asyncio
import discord
import requests
import shutil
import os
import random
import time
import requests
import json
import calendar


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
!gettoptracks (user)-(timespan) - Get LastFM top tracks, date range choices: overall | 7day | 1month | 3month | 6month | 12month
!getplaycount (user) - Get playcount of user on LastFM
!gettopartists (user)-(timespan) - Get LastFM top tracks, date range choices: overall | 7day | 1month | 3month | 6month | 12month
!getweeklycount (user) - Get LastFM current weekslot count
!drink (integer) - play a drinking game, drink the difference
"""

async def shrekFunction():
    filename = "media//shrek.txt"
    shrekLength = u.file_len(filename) -1
    shrekf = open(filename)
    shreklines= shrekf.readlines()
    for i in range(shrekLength):
        await message.channel.send(shreklines[i])

currentEpoch = round(time.time())
fromEpoch = l.parseTime()

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
            await message.channel.send("Processing...")
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
                await message.channel.send("Processing...")
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
                await message.channel.send("Processing...")
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
                await message.channel.send("Processing...")
                splitThis = message.content[9:]
                output = splitThis.split('-')
                url = url_fix((m.createMeme(output[0], output[1], output[2])).strip(os.sep))
                url = u.remove_at(7, url)
                url = u.remove_at(7, url)
                await message.channel.send(url) 
            except:
               await message.channel.send("Memegen failed!")


    if message.content.startswith("!getmemelist"):
        await message.channel.send("Processing...")
        result = m.parseMemeList()        
        sendString = ""
        for i in range(10):            
            sendString += f"Title: {result[1][i]}, ID: {result[0][i]} \n"
        await message.channel.send(sendString)
        link = "https://api.imgflip.com/popular_meme_ids"
        await message.channel.send(f"For the current top 100 memes check: {link}")
       

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
        randint = random(0,100)
        if round(randint) == 69:
            shrekFunction()
        fileN = "media//offensive.txt"
        length = u.file_len(fileN) -1
        pick = random.randint(0,length)     
        f=open(fileN)
        lines=f.readlines()
        await message.channel.send(lines[pick])   


    if message.content.startswith("!supersecretshrekmessage"):
        filename = "media//shrek.txt"
        shrekLength = u.file_len(filename) -1
        shrekf = open(filename)
        shreklines= shrekf.readlines()
        for i in range(shrekLength):
            await message.channel.send(shreklines[i])
        
            
    if message.content.startswith("!addquote"):
        inText = message.content[10:]
        u.addLineToFile(f'\n{inText} ', 'media/offensive.txt')
        await message.channel.send(f'Quote : \"{inText}\", was added to the inspirational quotes file.')

    if message.content.startswith('!gettoptracks'):
        await message.channel.send("Processing...")
        try:
            splitThis = message.content[14:]
            output = splitThis.split('-')
            artists, tracks = l.getTopTracks(output[0], output[1])
            sendString = ""
            await message.channel.send(f"{output[0]}'s Favourite tracks in last {output[1]} period where:")
            for i in range(len(artists)):
                sendString += f"{tracks[i]} - {artists[i]} \n"
            await message.channel.send(sendString)
        except:
            await message.channel.send("Error! Did you use the right syntax?")

    if message.content.startswith('!getplaycount'):
        try:
            await message.channel.send("Processing")    
            userName = message.content[14:]
            output = l.getPlaycount(userName)
            await message.channel.send(f"{userName}, has a playcount of {output}.")
        except:
            await message.channel.send("Error! Did you use the right syntax?")

    if message.content.startswith('!gettopartists'):
        try:
            result = message.content[15:]
            output = result.split('-')
            await message.channel.send("Processing...")
            artists = l.getTopArtists(output[0], output[1])
            await message.channel.send(f"{output[0]}'s Favourite artists in last {output[1]} period where:")
            sendString = ""
            for artist in artists:
                sendString += f"{artist} \n"
            await message.channel.send(sendString)    
        except:
            await message.channel.send("ERROR! Did you use the right syntax?")
        
    if message.content.startswith('!drink'):
        try:
            inputInt = int(message.content[7:])
            drinkThis, wasNumber = h.drinkGame(inputInt)
            author = str(message.author)
            await message.channel.send(f"The number was {wasNumber}, so {author[:-5]} has to drink {drinkThis} sips!")
        except:
            await message.channel.send("Enter a valid number!")
        
    if message.content.startswith('!getweeklycount'):
        try:
            user = message.content[15:]
            await message.channel.send(f"The current time is {currentEpoch}")
            await message.channel.send("Processing...")
            count = l.getWeeklyCount(currentEpoch, fromEpoch, user)            
            await message.channel.send(f"{user}\'s current weekcount is {count}")
              
        except:
            await message.channel.send("ERROR! Did you use the right syntax?")

client.run(token)
