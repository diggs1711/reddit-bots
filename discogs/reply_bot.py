import praw, botSetup, re, os, discogs_auth

data = {}
r = botSetup.login()
d = discogs_auth.authorize()


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

        results = d.search(submission.title, type='release')
		
        if (results.count != 0):
        	topResult = results[0]
        	artist = topResult.artists[0].name
        	tracklist = topResult.tracklist
        	labels = topResult.labels
        	title = topResult.title
        	rId = topResult.id
        	year = topResult.year
        	release = d.release(rId)
        	tracklist = release.tracklist
        	url = release.data['uri']
        	#use beatiful soup to retrieve price
        	
        	#posts_replied_to.append(submission.id);
        else:
			song = submission.title.split(' - ')[1]
			results = d.search(song, type='release')
			if results.count != 0:
				print "record found"
			else:
				songWithoutLabelOrYear = song.split(' [')[0]
				results = d.search(songWithoutLabelOrYear, type='release')
				print results.count
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
