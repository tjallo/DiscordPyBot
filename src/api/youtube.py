from requests import get
from youtubesearchpython.__future__ import VideosSearch


class YoutubeAPI:
    def __init__(self) -> None:
        self.YDL_OPTIONS = {"format": "bestaudio", "noplaylist": "True"}

    async def search(self, search_term: str):

        videosSearch = VideosSearch(search_term, limit=5)

        videos = []

        for _ in range(5):
            videos.append(await videosSearch.next())

        return videos
