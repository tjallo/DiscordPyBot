from pathlib import Path
from xmlrpc.client import Boolean
from discord import Guild, User
from json import dump, load


class UserManager:
    def __init__(self, save_path) -> None:
        try:
            path = Path(save_path)
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)

            self.save_path = path
        except Exception as e:
            print("Invalid path given")

    def _check_guild(self, guild: Guild):
        guild_path = self.save_path / str(guild.id)
        guild_path.mkdir(parents=True, exist_ok=True)

        guild_info = f""""guild_id": {guild.id}
"guild_name": {guild.name}
"guild_members": {guild.members}
"guild_owner": {guild.owner}
"voice_channels": {guild.voice_channels}
"text_channels": {guild.text_channels}
        """

        guild_info_path = guild_path / "info.txt"

        with open(guild_info_path, "w+") as file:
            file.write(str(guild_info))

    def _check_user(self, guild: Guild, user: User):
        guild_path = self.save_path / str(guild.id)
        user_file = guild_path / f"{user.id}.json"

        if not user_file.exists():
            user_info = {
                "user_name": user.name,
                "user_id": user.id,
                "user_score": 0,
                "user_tries": 0,
            }

            with open(user_file, "w+") as file:
                dump(user_info, file)

    def _write_user_data(self, user_data, guild: Guild, user: User):
        guild_path = self.save_path / str(guild.id)
        user_file = guild_path / f"{user.id}.json"

        with open(user_file, "w+") as file:
            dump(user_data, file)

    def get_user_data(self, guild: Guild, user: User) -> dict:
        guild_path = self.save_path / str(guild.id)
        user_file = guild_path / f"{user.id}.json"

        with open(user_file, "r") as file:
            user_data = load(file)

        return user_data

    def increment_user(self, guild: Guild, user: User, correct_answer: Boolean = True):
        self._check_guild(guild)
        self._check_user(guild, user)

        user_data = self.get_user_data(guild, user)

        if correct_answer:
            user_data["user_score"] += 1
        user_data["user_tries"] += 1

        self._write_user_data(user_data, guild, user)
