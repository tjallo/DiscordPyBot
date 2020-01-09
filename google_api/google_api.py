#Initzializing
from google_images_download import google_images_download
g = google_images_download
query = ""

#Imagesearcher
def googleImgSearch(query):
    response = g.googleimagesdownload()
    args = {"keywords": query, "limit": 1, "print_urls": True}    
    payload = str(response.download(args))
    return find_between(payload, "[\'", "\']")

#Sanitizes output
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""