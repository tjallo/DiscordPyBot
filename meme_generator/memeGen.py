import requests
import json
import credentials


imgUser = credentials.imgUser
imgPassword = credentials.imgPassword

def getMemeList():
    url = "https://api.imgflip.com/get_memes"	
    headers = {
    'Accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)	
    
    return response.json()

def parseMemeList():
    memeList = getMemeList()['data']['memes']
    memeID = []
    memeName = []

    for i in range(len(memeList)):
        memeID.append(memeList[i]['id'])
        memeName.append(memeList[i]['name'])
    return memeID, memeName


#Sanitizes output
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def createMeme(memeID, text0, text1):
    headers = {
    'Accept-Encoding': 'application/json'
    }
    url = f"https://api.imgflip.com/caption_image?template_id={memeID}&username={imgUser}&password={imgPassword}&text0={text0}&text1={text1}"
    response = requests.request("POST", url, headers=headers)
    
    return find_between(response.text, "{\"url\":\"", "\",\"pa")
    #return find_between(response.text, "page_url\":\"", "\"")

