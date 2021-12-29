# Dependencies
from os.path import isfile
from os import environ
from dotenv import dotenv_values
from discord.ext.commands import Bot, DefaultHelpCommand

# Local imports
from src.cogs.chat import ChatCog
from src.cogs.reddit import RedditCog
from src.cogs.trivia import TriviaCog


class BotClient(Bot):
    async def on_ready(self):
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


def main():
    if not isfile(".env"):
        print(
            f"\n\nThere was no (valid) '.env' file found. Please make sure it is there.\n\n Attempting to get env variables"
        )

        COMMAND_PREFIX = environ['COMMAND_PREFIX'] or "!"
        BOT_TOKEN = environ['BOT_TOKEN']
        DESCRIPTION = environ['DESCRIPTION'] or "Discord.py bot Ver 3.0 by Tjallo"

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
    )
    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
