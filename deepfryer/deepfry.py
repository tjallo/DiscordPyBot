import os

def fryMe(path):
    command = f"deeppyer -o downloads\\fried.jpeg \"{path}\""
    print(os.system(f'cmd /c "{command}"'))