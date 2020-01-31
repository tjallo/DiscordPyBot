import requests
from lastfm_api import LastFMTopTracksprettyJSON
import json
import credentials

apiKey = credentials.lastApiKey





def getTopTracks(user, period):
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={user}&api_key={apiKey}&format=json&period={period}&page=1"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    result = LastFMTopTracksprettyJSON.last_fm_from_dict(json.loads(response.text))

    artists = []
    tracks = []
    i = 0

    while (i < 5):
        artists.append(result.toptracks.track[i].artist.name)
        tracks.append(result.toptracks.track[i].name)
        i += 1


    return artists, tracks   

def getPlaycount(user):