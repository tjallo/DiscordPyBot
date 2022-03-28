# Dependencies
from os.path import isfile
from os import environ, makedirs, getcwd
from dotenv import dotenv_values
from discord.ext.commands import Bot, DefaultHelpCommand
from discord import Game
from asyncio import run
from pathlib import Path
import logging

from numpy import True_


# Local imports
from src.cogs.chat import ChatCog
from src.cogs.reddit import RedditCog
from src.cogs.trivia import TriviaCog
from src.cogs.deepfry import DeepfryCog
from src.cogs.memes import MemeCog
from src.cogs.drinking import DrinkingCog
from src.cogs.audio import AudioCog

from src.util.start_up import cleanup


class BotClient(Bot):
    async def on_ready(self):
        activity = Game(name="my ass as a drum.", type=1)
        await self.change_presence(activity=activity)
        print(f"Logged in as {self.user}")

    def __init__(self, command_prefix, help_command=..., description=None, **options):
        super().__init__(
            command_prefix,
            help_command=help_command,
            description=description,
            **options,
        )

        self.add_cog(ChatCog(self))
        self.add_cog(RedditCog(self))
        self.add_cog(TriviaCog(self))
        self.add_cog(DeepfryCog(self))
        self.add_cog(MemeCog(self))
        self.add_cog(DrinkingCog(self))
        self.add_cog(AudioCog(self))

def setup_logger():
    folder_location = Path(f"{getcwd()}/db/logging")
    makedirs(folder_location, exist_ok=True)

    file_path = folder_location / "discord.log"

    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename=file_path, encoding='utf-8', mode="w+")

    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

    logger.addHandler(handler)

def main():
    cleanup()
    setup_logger()

    if not isfile(".env"):
        print(
            f"\n\nThere was no (valid) '.env' file found. Please make sure it is there.\n\n Attempting to get env variables"
        )

        COMMAND_PREFIX = environ["COMMAND_PREFIX"] or "!"
        BOT_TOKEN = environ["BOT_TOKEN"]
        DESCRIPTION = environ["DESCRIPTION"] or "Discord.py bot Ver 3.0 by Tjallo"

    else:
        config = dotenv_values(".env")

        # Default properties
        COMMAND_PREFIX = config.get("COMMAND_PREFIX") or "!"
        BOT_TOKEN = config.get("BOT_TOKEN") or None
        DESCRIPTION = config.get("DESCRIPTION") or "Discord.py bot Ver 3.0 by Tjallo"

    HELP_COMMAND = DefaultHelpCommand()

    HELP_COMMAND.sort_commands = True

    

    bot: BotClient = BotClient(
        command_prefix=COMMAND_PREFIX,
        help_command=HELP_COMMAND,
        description=DESCRIPTION,
        case_insensitive=True,
    )

    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
