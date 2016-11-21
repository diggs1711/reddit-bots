import discogs_auth

d = discogs_auth.authorize()

class ResultData(object):
	topResult = {}
	artist = ""
	tracklist = {}
	labels = {}
	title = ""
	rId = 0
	year = 0
	release = {}
	url = ""
	
	def __init__ (self,topResult,artist,tracklist,labels, title, rId, year, release, url):
		self.topResult = topResult
		self.artist = artist
		self.tracklist = tracklist
		self.labels = labels
		self.title = title
		self.rId = rId
		self.year = release
		self.url = url

def retrieveData(results):
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
	
	return ResultData(topResult,artist,tracklist,labels, title, rId, year, release, url)
	
def Search(s):
	return d.search(s, type='release')
	
    
    

