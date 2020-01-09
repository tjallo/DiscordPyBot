# DiscordPyBot

### Tech

DiscordPyBot uses a number of Python libraries to work properly:

* [PRAW](https://pypi.org/project/praw/)
* [Wikipedia](https://pypi.org/project/wikipedia/)
* [Discord.py](https://pypi.org/project/discord.py/)

### Configuration

 The only file that needs configuration right now is the "credentials.py"
 Edit the "example_crediantials.py" with your own credentials, and rename the file to "credentials.py"

### Running the Bot

Run in the source directory using:
```sh
py ./main.py
```
Or using your own preferred method. Just run main.py

### Current commands

 * !help - See available commands
 * !ping - Pong!
 * !wiki (wikiarticle) - Get a wiki article
 * !imgwiki (wikiarticle) - Get the first image on a Wiki Article
 * !rkarma (redditUserName) - Get an user's total karma on reddit

### Planned Updates
 
 * Add a way to get the first google image for a search
 * Add a way to deepfry the image of the google search
 * More reddit API feature implementations
 * Add some form of music player (spotify and/or youtube)
 * ...