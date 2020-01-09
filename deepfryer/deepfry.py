import os

def fryMe(path):
    command = f"deeppyer -o downloads\\fried.jpeg \"{path}\""
    print(os.system(f'cmd /c "{command}"'))

#fryMe("D:\\Users\\tjalw\\Desktop\\devEnv\\DiscordPyBot\\deepfryer\\download.png")