#!/bin/bash
cd /home/tjalle/sambashare/torrent/github/DiscordPyBot/
sudo docker build -t discordbot .
sudo docker run discordbot