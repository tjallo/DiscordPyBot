from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import shutil
import requests
import os
import deeppyer
import asyncio
from sources.util import file_handler as File
from resources import config
from PIL import Image

def getImageLink(query):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    URL = f"https://duckduckgo.com/?q={query}&atb=v241-4&iax=images&ia=images"
    link = ""
    try:
        driver.get(URL)

        el = driver.find_elements_by_class_name("tile--img__img")
        el[0].click()

        link = driver.find_element_by_class_name("c-detail__btn").get_attribute("href")
    except:
        link = "Image not found!"

    driver.quit()

    return link


def image_downloader(query):
    cwd = os.getcwd()
    image_url = getImageLink(query)
    filename = image_url.split("/")[-1]

    if len(filename) > 14:
        filename = filename[-14:]
    
    if not '.jpeg' in filename or not '.jpg' in filename or not '.gif' in filename or not '.png' in filename or not '.bit' in filename:
        filename = filename + ".jpg"

    result = requests.get(image_url, stream=True)

    if result.status_code == 200:
        result.raw.decode_content = True

    File.temp_cleanup()

    os.chdir(config.temp_folder)

    with open(filename, 'wb+') as f:
        shutil.copyfileobj(result.raw, f)

    fullpath = os.getcwd() + "\\" + filename

    os.chdir(cwd)

    return fullpath


async def deepfryCoroutine(path, savepath):
    img = Image.open(path)
    img = await deeppyer.deepfry(img, flares=False)
    img.save(savepath)

async def deepfry(path, savepath):
    await (deepfryCoroutine(path, savepath))
    return savepath

async def deepfrySearch(query):
    img_path = image_downloader(query)

    savepath = img_path[:-5] + "deepfried" + img_path[-5:]

    await deepfry(img_path, savepath)

    return(savepath)
