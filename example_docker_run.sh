# Run this command to run the most recent docker image, with your relevant details
docker pull tjallew/discord-py-bot:latest

docker run \
-e BOT_TOKEN="bot_token" \
-e COMMAND_PREFIX="!" \
-e DESCRIPTION="Discord.py bot version 3.0 by Tjallo, Invoke !help [command] to see the full command description" \
-e REDDIT_CLIENT_ID="client_id" \
-e REDDIT_CLIENT_SECRET="client_secret" \
-e REDDIT_USER_AGENT="discord_bot" tjallew/discord-py-bot