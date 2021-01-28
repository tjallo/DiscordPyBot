import wikipedia

string_parser = lambda input_string: input_string if len(input_string) <= 1995 else input_string[:1995] + "..."

def get_summary(article_name):
    result = ""
    try:
        summary = wikipedia.summary(article_name)
        result = string_parser(summary)
    except:
        result = "Article not found!"

    return result


def get_image(article_name):
    image = ""
    try:
        page = wikipedia.page(article_name)
        image = page.images[0]
    except:
        image="Article not found"

    return image
