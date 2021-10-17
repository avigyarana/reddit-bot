import praw
import random
import time

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username = "",
    password =

)
subreddit = reddit.subreddit("")

quotes = ["aaa","bbb","ccc"]

for submission in subreddit.hot(limit=10):
    print("****")
    print(submission.title)

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " " in comment_lower:
                print("----")
                print(comment.body)
                random_index = random.randint(0, len(quotes)-1)
                comment.reply(quotes[random_index])
                time.sleep(660)