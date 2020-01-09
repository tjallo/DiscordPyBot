import wikipedia


def get_article_not_filtered(search):
    result = wikipedia.summary(str(search))
    lnt = len(result)    
    if (lnt > 1990):
        result = result[:lnt-2003]   
        result += "..."
        return result
    else:
        return result

def get_image_not_filtered(search):
    return wikipedia.page(search).images[0]

def get_article(search):
    try:
        return get_article_not_filtered(search)
    except:
        return "Article not found!"

def get_image(search):
    try:
        return get_image_not_filtered(search)
    except:
        return "Image not found!"
