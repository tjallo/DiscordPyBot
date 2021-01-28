import logging, os
from resources import config

LOGFILENAME = 'last-discord.log'

def start(logger):
    cleanup()
    startLogging(logger)

def cleanup():
    if not os.path.exists('resources/logs'):
        os.mkdir('resources/logs')
    
    files = os.listdir('resources/logs')

    if LOGFILENAME in files:
        os.rename(f'resources/logs/{LOGFILENAME}', f'resources/logs/{len(files)}-discord.log')    

def startLogging(logger):
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename=f'resources/logs/{LOGFILENAME}', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)