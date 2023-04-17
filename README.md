![GitHub Workflow Status](https://img.shields.io/github/workflow/status/tjallo/DiscordPyBot/Run%20tests,%20build%20and%20publish%20docker%20image)
![GitHub Repo stars](https://img.shields.io/github/stars/tjallo/DiscordPyBot?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/tjallo/DiscordPyBot?style=social)
![Docker Pulls](https://img.shields.io/docker/pulls/tjallew/discord-py-bot)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/tjallo/DiscordPyBot)

## DiscordPyBot by tjallew
### See the v1 and v2 bracnhes for (deprecated) earlier iterations of this bot.


****
## Github link
[https://github.com/tjallo/DiscordPyBot](https://github.com/tjallo/DiscordPyBot)
# How to use
## Run this command to run the most recent docker image, with your relevant details

    docker pull tjallew/discord-py-bot:latest
    docker run \
    -e BOT_TOKEN="bot_token" \
    -e COMMAND_PREFIX="!" \
    -e DESCRIPTION="Discord.py bot version 3.0 by Tjallo, Invoke !help [command] to see the full command description" \
    -e REDDIT_CLIENT_ID="client_id" \
    -e REDDIT_CLIENT_SECRET="client_secret" \
    -e REDDIT_USER_AGENT="discord_bot" \
    -e IMGFLIP_USER="usernm" \
    -e IMGFLIP_PASSWORD="password" \
    tjallew/discord-py-bot


****

## Make sure to enable all Privileged Gateway Intents in your discord developer portal


Details you need for the enviroment variables can be found here:
* [Discord Application page](https://discord.com/developers/applications)
* [Reddit API details page](https://www.reddit.com/prefs/apps)
* [ImgFlip API](https://imgflip.com/api)

These details will persist in the container when you run docker run! So you can run the created container without the enviroment variables afterwards. Using Docker Hub application for this management is recommended.
