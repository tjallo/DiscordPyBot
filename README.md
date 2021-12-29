# DiscordPyBot by tjallew
### This version is still in development, see v2 branch for working example, and v1 branch for a legacy version

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
    -e REDDIT_USER_AGENT="discord_bot" tjallew/discord-py-bot
    -e IMGFLIP_USER="usernm" \
    -e IMGFLIP_PASSWORD="password" \


****


Details you need for the enviroment variables can be found here:
* [Discord Application page](https://discord.com/developers/applications)
* [Reddit API details page](https://www.reddit.com/prefs/apps)
* [ImgFlip API](https://imgflip.com/api)

These details will persist in the container when you run docker run! So you can run the created container without the enviroment variables afterwards. Using Docker Hub application for this management is recommended.
