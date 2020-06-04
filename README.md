
# DiscordPyBot

## Disclaimer


### The flaskserver module is still in development and should be ignored
### This readme is outdated. Haven't bothered to update it yet. (Installation should still be correct.)

***

 At this moment in time, the bot was/is only tested on Ubuntu.

 This is because it has been developed on this platform.
 
 I am in the works of making a Windows compatible version as we speak, but the Ubuntu version has priority.
 (Note; most functions do work on Windows, but they can spit unneccesairy errors, also the tmp file system isnt working on Windows)
 
 

### Tech

DiscordPyBot uses a number of Python libraries to work properly:

* [PRAW](https://pypi.org/project/praw/)
* [wikipedia](https://pypi.org/project/wikipedia/)
* [Discord.py](https://pypi.org/project/discord.py/)
* [google_images_download](https://github.com/hardikvasa/google-images-download) (Forked and fixed Version from Hardikvasa)
* [deeppyer](https://pypi.org/project/deeppyer/)
* [werkzeug](https://pypi.org/project/Werkzeug/)
* [PyNaCl](https://pypi.org/project/PyNaCl/)
* [dataclasses](https://pypi.org/project/dataclasses/)

Special thanks to [quicktype.io](https://app.quicktype.io/), for rapid code generation for JSON to classes.

Use the provided requirements.txt (located in installation files folder) script to install all the PIP libraries for you.
Using ```pip install -r requirements.txt```

###  Installation and Configuration

Make sure that you have 'deeppyer' in your /bin/ folder to so you can run it from the command line (not in /home/.local/bin)

Install all required pip files by running ```pip install -r requirements.txt``` the requirements are located in the installation files folder.

 The only file that needs configuration is the "credentials.py"
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
 * !sourcecode - Get a GitHub link to the bot's source code
 * !imgsearch (query) - Google and post an image
 * !deepfry (imgSearch) - Google and deepfry an image
 * !getmemelist - get top meme's right now on imgflip with corrosponding id, also sends a link for the list with the top 100 memes right now
 * !memegen (id)-(text1)-(text2) - generates a meme using imgflip meme id
 * !destroylibtard - send an inspirational quote
 * !addquote (quote) - add quote to the inspirational quotes list.
 * !gettoptracks (user)-(timespan) - Get LastFM top tracks, date range choices: overall | 7day | 1month | 3month | 6month | 12month
 * !getplaycount (user) - Get playcount of user on LastFM
 * !gettopartists (user)-(timespan) - Get LastFM top tracks, date range choices: overall | 7day | 1month | 3month | 6month | 12month
 * !drink (integer) - play a drinking game, drink the difference

### Planned Updates
 
 * Rework the readme to be more readable
 * More reddit API feature implementations
 * Add some form of music player (spotify and/or youtube)
 * Create a Docker container version of the app
 * ...
