import praw

reddit_instance = praw.Reddit(client_id = "-pSPiKAER-EyCsC8pdEfxg",client_secret="Q-Mf5eNG2O_tllof1rmkSgmr1ccEZw",user_agent="/u/Spectrum_py")

sub_reddit = reddit_instance.subreddit("memes").top(limit=25)
meme_list = []
for memes in sub_reddit:
    meme_list.append(memes.title)

print(meme_list)


