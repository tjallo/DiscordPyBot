from resources import secret
import requests, json

USER = secret.imgflip_usr
PWD = secret.imgflip_pwd


def getPopularMemeIDs():
    req = requests.get("https://api.imgflip.com/get_memes")
    res = json.loads(req.text)["data"]["memes"]
    results = []

    for meme in res:
        results.append([meme["name"], meme["id"]])

    return results


def generateMemeURL(memeID, upperText, bottomText):
    data = {
        "template_id": memeID,
        "username": USER,
        "password": PWD,
        "text0": upperText,
        "text1": bottomText,
    }
    req = requests.post("https://api.imgflip.com/caption_image", data=data)
    res = json.loads(req.text)
    url = res["data"]["url"]

    return url
