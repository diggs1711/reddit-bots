import praw
import botSetup
import re
import os
import discogs_auth
import discogsObject

data = {}
r = botSetup.login()

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

subreddit = r.get_subreddit('truehouse')

for submission in subreddit.get_hot(limit=5):
    if submission.id not in posts_replied_to:
        results = discogsObject.Search(submission.title)
        if (results.count != 0):
            result = discogsObject.retrieveData(results)
            # use beatiful soup to retrieve price
            print result.title
            # posts_replied_to.append(submission.id);
        else:
            song = submission.title.split(' - ')[1]
            results = discogsObject.Search(song)
            if results.count != 0:
                print "HEllo"
            else:
                songWithoutLabelOrYear = song.split(' [')[0]
                results = discogsObject.Search(songWithoutLabelOrYear)
                print results.count
    
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
