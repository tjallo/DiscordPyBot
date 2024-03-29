from os import getcwd
from pathlib import Path
from pytube import YouTube, Search


class YoutubeDownloader:
    def __init__(self) -> None:
        self.save_path = Path(f"{getcwd()}/temp/video")
        self.save_path.mkdir(parents=True, exist_ok=True)

    def get_video_audio(self, url: str):
        """
        Returns path of downloaded video url
        """

        try:
            return YouTube(url).streams.get_audio_only().download(self.save_path)
        except Exception as e:
            print(e)
            return None

    def search(self, query: str):
        s = Search(query)

        return s.results[:5]
            