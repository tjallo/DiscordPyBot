import requests
from lastfm_api import LastFMTopTracksprettyJSON
from lastfm_api import getInfoPretty
from lastfm_api import getTopArtistsPretty
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
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user={user}&api_key={apiKey}&format=json"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    result = getInfoPretty.welcome_from_dict(json.loads(response.text))
    return result.user.playcount

def getTopArtists(user, period):
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getTopArtists&user={user}&api_key={apiKey}&format=json&period={period}&page=1&limit=5"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    result = getTopArtistsPretty.get_top_artists_from_dict(json.loads(response.text))
    artists = []
    for artist in result.topartists.artist:
        artists.append(artist.name)
    return artists

def getWeeklyCount(currentEpoch, fromEpoch, user):

    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks&user=tjallo&api_key=06199ca5111af01e6844cabe763ebf87&format=json&page=1&from={fromEpoch}&to={currentEpoch}"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    jsonText = json.loads(response.text)
    return jsonText['recenttracks']['@attr']['total']
