import praw, botSetup,re,os

r = botSetup.login()

subreddit = r.get_subreddit('pythonforengineers')
for submission in subreddit.get_hot(limit=5):
    if re.search("reddit is fun", submission.title, re.IGNORECASE):
        submission.add_comment("Gibb Gibb")

    
