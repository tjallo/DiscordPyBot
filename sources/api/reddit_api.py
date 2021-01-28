import praw
from resources import secret as credentials

reddit = praw.Reddit(
            client_id=credentials.client_id,
            client_secret=credentials.client_secret,
            user_agent=credentials.user_agent,
            username=credentials.username,
            password=credentials.password
        )

    

def get_karma(user):
    try:
        user = reddit.redditor(str(user))
        total_karma = user.link_karma + user.comment_karma
        return f"The user {user} has a total of {total_karma} karma on reddit."
    except:
        return "User not found!"
   