from resources import config
import os

temp_folder = os.getcwd() + "\\" + config.temp_folder

def run_on_startup():
    temp_cleanup()
    print("Temp folder was cleansed...")

def temp_cleanup():
    cwd = os.getcwd()
    if not os.path.isdir(temp_folder):
        os.mkdir(temp_folder)
    else:
        os.chdir(temp_folder)
        files = os.listdir(temp_folder)
        for file in files:
            os.remove(file)

    os.chdir(cwd)
