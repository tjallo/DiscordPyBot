# DiscordPyBot
## This version is still in development, see v2 branch for working example, and v1 branch for a legacy version


This is a development version!

## How to run
* Make sure you have installed docker
* Enter all the relevant details in the example.env file and rename the file to .env
* Build the Docker image: `docker build --tag discord-py-bot .`
* Run the discord-py-bot image in Docker


## Enviroment vars that need to be set
* COMMAND_PREFIX
* BOT_TOKEN
* DESCRIPTION
* REDDIT_CLIENT_ID
* REDDIT_CLIENT_SECRET
* REDDIT_USER_AGENT

You can set these enviroment variables quite easily in the docker run command, see the example_docker_run.sh file for an example. These enviroment variables will then persist in the container you have created with docker run.