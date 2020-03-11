#Initzializing
from googleImgDownload import google_images_download
g = google_images_download
query = ""

#Imagesearcher
def googleImgSearcher(query):
    response = g.googleimagesdownload()
    args = {"keywords": query, "limit": 4, "print_urls": True}    
    payload = str(response.download(args))
    arr = []
    arr = (find_between(payload, "[\'", "\']").split(","))
    return arr

#Sanitizes output
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def googleImgSearch(query):
    arr = googleImgSearcher(query)      
    for i in arr:
        if not ("svg" in str(i)):
            return i.strip(' "\'\t\r\n')