#!/bin/bash

env/bin/pip3 freeze > requirements.txt
docker build --tag discord-py-bot . 