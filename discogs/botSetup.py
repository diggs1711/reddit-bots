import praw

user_agent = ("Discogs App");
REDDIT_USERNAME = "digs1711";
REDDIT_PASS = "oZ5UsxEwe1O1PnLO0y1L";



def login ():
    r = praw.Reddit(user_agent = user_agent);
    r.login(REDDIT_USERNAME, REDDIT_PASS);
    return r;