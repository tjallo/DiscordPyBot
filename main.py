from reddit_api import reddit_main
from wiki_api import wiki_api
from google_api import google_api
from deepfryer import deepfry
from discord.ext import commands
from credentials import token
import discord


r = reddit_main
w = wiki_api
g = google_api
d = deepfry

commandList = """
!help - See this message
!ping - Pong!
!wiki - Get a wiki article
!imgwiki - Get the first image on a Wiki Article
!rkarma - Get an user's total karma on reddit
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
        await message.channel.send(w.get_article(message.content[6:]))

    if message.content.startswith('!imgwiki'):
        await message.channel.send(w.get_image(message.content[9:]))   

    if message.content.startswith('!rkarma'):
        await message.channel.send(r.get_karma(message.content[8:]))           
    
client.run(token)