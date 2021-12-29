from discord.ext import commands
from discord import Member
from random import choice
from random import randint

class DrinkingCog(commands.Cog, name="Drinking"):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="randomDrink")
    async def ping(self, ctx, *args, member: Member = None):
        """[tag] [tag] [tag] - tag as many people as you want, the game picks one random player that has to drink between 1 and 10 sips"""
        member = member or ctx.author
        people = [x for x in args]
        i = randint(1,10)
        person = choice(people)

        await ctx.send(f"{person} has to drink {i} sips")

