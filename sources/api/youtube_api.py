from youtube_search import YoutubeSearch
from pytube import YouTube

def get_urls_and_titles(query):
    results = YoutubeSearch(query, max_results=5).to_dict()

    url_title_dict = []
    for x in results:
        url_title_dict.append([x['title'], f"https://www.youtube.com{x['url_suffix']}"])

    return url_title_dict

def download_video(url, folderpath):
    return YouTube(url).streams.filter(type="audio").first().download(output_path=folderpath)