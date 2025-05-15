import praw

reddit_instance = praw.Reddit(client_id = "<client_id>",client_secret="<client_secret>",user_agent="/u/<username>")

sub_reddit = reddit_instance.subreddit("memes").top(limit=25)
meme_list = []
for memes in sub_reddit:
    meme_list.append(memes.title)

print(meme_list)


