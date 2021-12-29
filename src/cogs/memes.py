from discord.ext import commands
from discord import Member
from requests import request
from json import loads
from os import environ
from os.path import isfile
from dotenv import dotenv_values


class MemeCog(commands.Cog, name="Memes"):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot
        self._get_memes()

        if not isfile(".env"):
            print(
                f"\n\nThere was no (valid) '.env' file found. Please make sure it is there.\n\n Attempting to get env variables"
            )

            self.username = environ["IMGFLIP_USER"]
            self.password = environ["IMGFLIP_PASSWORD"]

        else:
            self.username = dotenv_values(".env").get("IMGFLIP_USER") or None
            self.password = dotenv_values(".env").get("IMGFLIP_PASSWORD") or None

    def _get_memes(self):
        req = request("get", "https://api.imgflip.com/get_memes")

        self.data = loads(req.text)["data"]["memes"]
        msgs = [f"{x['id']}: {x['name']}" for x in self.data]
        self.msg1 = "\n".join(msgs[:50])
        self.msg2 = "\n".join(msgs[50:])

    @commands.command(name="getMemeTemplates")
    async def get_templates(self, ctx):
        """
        Get ID's for !getMemes
        """

        await ctx.send(self.msg1)
        await ctx.send(self.msg2)

    @commands.command(name="getMeme")
    async def get_memes(self, ctx, *args, member: Member = None):
        """
        [memeID]:[topText]:[bottomText] - genereate meme
        """
        member = member or ctx.author


        try:
            args = ' '.join(args)
            splitted = args.split(':')
            template_id = splitted[0]
            topText = splitted[1]
            bottomText = splitted[2]

            params = {
                "template_id": template_id,
                "text0": topText,
                "text1": bottomText,
                "username": self.username,
                "password": self.password,
            }
            req = request("get", "https://api.imgflip.com/caption_image", params=params)

            await ctx.send(loads(req.text)['data']['url'])
        except Exception as e:
            await ctx.send(e)
