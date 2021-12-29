from os import environ, name
from os.path import isfile
from discord.ext import commands
from dotenv import dotenv_values
from asyncpraw import Reddit
from asyncpraw.reddit import Redditor


class RedditCog(commands.Cog, name="Reddit"):
    def __init__(self, bot):
        self.bot = bot

        if not isfile(".env"):
            print(
                f"\n\nThere was no (valid) '.env' file found. Please make sure it is there.\n\n Attempting to get env variables"
            )

            self.client_id = environ["REDDIT_CLIENT_ID"]
            self.client_secret = environ["REDDIT_CLIENT_SECRET"]
            self.client_user_agent = environ["REDDIT_USER_AGENT"]

        else:
            self.client_id = dotenv_values(".env").get("REDDIT_CLIENT_ID") or None
            self.client_secret = (
                dotenv_values(".env").get("REDDIT_CLIENT_SECRET") or None
            )
            self.client_user_agent = (
                dotenv_values(".env").get("REDDIT_USER_AGENT") or None
            )

        self.reddit = Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.client_user_agent,
        )

        self.reddit.read_only = True

    @commands.command(name="userkarma")
    async def userkarma(self, ctx, arg):
        """- Returns the amount of karma a reddit user has"""
        name = str(arg).strip()
        try:
            user = Redditor(reddit=self.reddit, name=name)
            # Since we are using async praw, we must await this coroutine
            await user.load()
            comment_karma = user.comment_karma
            link_karma = user.link_karma
            total_karma = int(comment_karma) + int(link_karma)
            message = f"The reddit user {name} has {comment_karma} comment karma and {link_karma} post karma.\n\n{total_karma} karma in total."
        except Exception as e:
            message = f"User with the username: {name} was not found."

        await ctx.send(message)
