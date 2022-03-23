from discord.ext import commands
from discord import Member
from random import choice
from random import randint


class DrinkingCog(commands.Cog, name="Games"):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="randomDrink")
    async def ping(self, ctx, *args, member: Member = None):
        """[tag] [tag] [tag] - tag as many people as you want, the game picks one random player that has to drink between 1 and 12 sips"""
        member = member or ctx.author
        people = [x for x in args]
        i = randint(1, 12)
        person = choice(people)

        await ctx.send(f"{person} has to drink {i} sips")

    from random import choice

    def _roll_dice(self, sides, times):
        p = [i + 1 for i in range(sides)]

        outcome = []

        for _ in range(times):
            outcome.append(choice(p))

        return outcome

    @commands.command(name="roll")
    async def roll(self, ctx, *args):
        """
        use: !roll [sides] [times]
        """

        try:
            args = [arg for arg in args]

            sides = int(args[0])
            times = int(args[1])

            if sides <= 100 and times <= 100:

                outcome = self._roll_dice(sides, times)

                outcome = " - ".join([str(r) for r in outcome])

                msg = f"You rolled a {sides} sided die {times} times. The outcome was:\n**{outcome}**"

            else:
                msg = "Please keep sides and times under the limit of 100"

        except Exception as e:
            msg = "Please use the correct syntax. E.g. \"!roll 6 3\""

        await ctx.send(msg)
