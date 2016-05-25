import praw, botSetup,re,os

data = {}
r = botSetup.login()



if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = [];
    
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read();
        posts_replied_to = posts_replied_to.split("\n");
        posts_replied_to = filter(None, posts_replied_to);
        
subreddit = r.get_subreddit('truehouse')

for submission in subreddit.get_hot(limit=5):
    if submission.id not in posts_replied_to:
        print "Bot replying to : ", submission.title
            
        posts_replied_to.append(submission.id);

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")